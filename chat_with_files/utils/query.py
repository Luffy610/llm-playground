from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

def load_vector_store(persist_path="faiss_index"):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")
    return FAISS.load_local(persist_path, embeddings, allow_dangerous_deserialization=True)

def build_qa_chain(db=None):
    if db:
        retriever = db.as_retriever()
    else:
        retriever = load_vector_store().as_retriever()

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash-preview-04-17",
        temperature=0.3
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        You are an expert assistant. Use the following context to answer the question.
        
        Context:
        {context}
        
        Question:
        {question}
        """
    )

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt}
    )

    return qa