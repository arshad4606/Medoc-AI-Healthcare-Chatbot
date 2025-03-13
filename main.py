from langchain_community.llms import Ollama
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable.config import RunnableConfig
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import chainlit as cl

# Load Medical Knowledge Base
def load_medical_knowledge():
    loader = TextLoader("d:/langchain-gemma-ollama-chainlit-main/medical_data.txt", encoding="utf-8")  
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = text_splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)

    retriever = vectorstore.as_retriever()
    return retriever

retriever = load_medical_knowledge()

@cl.on_chat_start
async def on_chat_start():
    elements = [cl.Image(name="image1", display="inline", path="craiyon_102147_white_smiley_in_a_medical_cap.png")]
    await cl.Message(content="Hello there, I am Medoc. How can I help you?", elements=elements).send()

    model = Ollama(model="monotykamary/medichat-llama3:latest")

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You are an AI healthcare assistant named Medoc. You provide reliable medical information but do not diagnose illnesses. "
            "Your responses should be concise, clear, and based on verified healthcare data."
        ),
        ("human", "{question}"),
    ])
    
    runnable = prompt | model | StrOutputParser()
    cl.user_session.set("runnable", runnable)

@cl.on_message
async def on_message(message: cl.Message):
    runnable = cl.user_session.get("runnable")  

    msg = cl.Message(content="")

    async for chunk in runnable.astream(
        {"question": message.content},
        config=RunnableConfig(callbacks=[cl.LangchainCallbackHandler()]),
    ):
        await msg.stream_token(chunk)

    await msg.send()
