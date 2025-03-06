![image](https://github.com/user-attachments/assets/7d9ae2da-41c2-45a9-8b99-39870f260c3b)# Medoc-AI-Healthcare-Chatbot
Medoc is an AI Healthcare Chatbot is designed to provide users with general health guidance based on their symptoms. It asks symptom-related questions, suggests home remedies, and advises when to consult a doctor. The chatbot ensures high accuracy, low latency (under 8 seconds response time), and minimal token usage (≤5000 tokens per request)

Detailed view: 
     Medoc AI Healthcare Chatbot is an AI-powered conversational assistant that helps users with health-related queries. It asks symptom-based questions, provides general health guidance, suggests home remedies, and advises when to consult a doctor. The chatbot is not a diagnostic tool but serves as a preliminary guide for users seeking basic health information.

This project is optimized for:
	
 •	High Accuracy: Delivers precise and relevant health guidance.
	
 •	Low Latency: Ensures response time within 3-4 seconds and does not exceed 8 seconds.
	
 •	Minimal Token Usage: Uses ≤5000 tokens per request to optimize efficiency.

Features

 It has the knowledge of the  following subjects 
![image](https://github.com/user-attachments/assets/3c1e43a7-1161-4f18-bc36-341621084183)
 
 Symptom-Based Querying
	
 •	Engages users by asking relevant health-related questions.
	
 •	Helps users identify possible causes for their symptoms.

 General Health Guidance
	
 •	Provides non-diagnostic suggestions, including self-care tips and home remedies.
	
 •	Recommends when to seek professional medical attention.

 Optimized for Accuracy and Efficiency
	
 •	Uses Retrieval-Augmented Generation (RAG) to fetch the most relevant responses.
	
 •	Reduces hallucinations and enhances factual accuracy.
	
 •	Implements embedding-based ranking for better response selection.

 Chainlit-Based UI
	
 •	The chatbot is implemented with Chainlit for an interactive conversational experience.
	
 •	Provides a clean, fast, and efficient user interface.

 Implementation in VS Code
	
 •	Developed and executed in VS Code instead of Jupyter Notebook.
	
 •	Allows real-time interaction with the chatbot in a code-friendly environment.

Implementation Details

  Technology Stack
	
 •	Programming Language: Python
	
 •	Frameworks & Libraries:
	
 •	NLP & AI: MediChat LLaMA 3
	
 •	UI/UX: Chainlit
	
 •	Data Handling: Pandas, NumPy
	
 •	Optimization: FAISS for embedding-based retrieval
	
 •	Execution Environment: VS Code

System Workflow
	
1. User Query Input
	
 •	The chatbot receives the user’s symptoms or health-related question.
2. Symptom Analysis
	
 •	Uses an AI model to analyze the symptoms and ask follow-up questions.
 
3. Retrieval-Augmented Generation (RAG) Optimization
	
 •	Searches a structured database for relevant responses.
	
 •	Uses embeddings to rank and retrieve the most accurate answer.
 
4. Response Generation
	
 •	The chatbot provides a concise, fact-based response.
	
 •	If necessary, suggests home remedies or medical consultation.

5. Chainlit UI Integration
	
 •	The response is displayed interactively using Chainlit.

 RAG Optimization for Improved Accuracy
	
 •	Retrieval Step: Extracts the most relevant data using FAISS and embeddings.
	
 •	Augmentation Step: Enhances the response with additional context.
	
 •	Generation Step: Uses MediChat LLaMA 3 to generate a natural-language response.

 Performance Optimization
	
 •	Latency Reduction: Ensures responses are generated in under 8 seconds.
	
 •	Token Efficiency: Limits token usage to ≤5000 tokens per request.
	
 •	Data Structuring: Uses optimized indexing for faster retrieval.


If any query feel free to contact me, email:arshaa4606@gmail.com
