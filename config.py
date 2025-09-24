import os

# OpenAI API key
OPENAI_API_KEY = "YOUR_OPENAI_API_KEY"
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# Paths
PDF_PATH = "data/medical_encyclopedia.pdf"
VECTOR_DB_PATH = "vector_db/faiss_index"
