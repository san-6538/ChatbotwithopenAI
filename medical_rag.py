from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import config

# 1. Load FAISS vector store
embeddings = OpenAIEmbeddings(openai_api_key=config.OPENAI_API_KEY)
vector_store = FAISS.load_local(config.VECTOR_DB_PATH, embeddings)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

# 2. Chat model
chat_model = ChatOpenAI(
    temperature=0,
    openai_api_key=config.OPENAI_API_KEY,
    model_name="gpt-3.5-turbo"
)

# 3. User-specific RAG chain
user_chains = {}

def get_user_chain(user_id: str):
    if user_id not in user_chains:
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        chain = ConversationalRetrievalChain.from_llm(
            llm=chat_model,
            retriever=retriever,
            memory=memory,
            return_source_documents=True
        )
        user_chains[user_id] = chain
    return user_chains[user_id]
