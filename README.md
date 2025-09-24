A RAG (Retrieval-Augmented Generation) chatbot for medical queries, integrated with a PDF medical encyclopedia.
The backend is built using FastAPI and LangChain, with OpenAI GPT for responses.

Features

Loads a PDF medical encyclopedia as context.

Splits PDF into chunks and stores embeddings in a FAISS vector database.

Uses RAG approach: retrieves relevant context and answers queries.

Maintains user-specific chat history using LangChain memory.

Returns answers and top source snippets.

Ready for integration with Seva frontend.
