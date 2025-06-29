from langchain.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings

def vectorise_text(chunks, persist_path="faiss_index"):
    embedding = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    db = FAISS.from_texts(chunks, embedding)
    db.save_local(persist_path)
    return db
