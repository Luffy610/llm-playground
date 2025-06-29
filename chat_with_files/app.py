from dotenv import load_dotenv
load_dotenv()
import streamlit as st
from chat_with_files.loaders.file_loader import load_pdf, load_csv
from chat_with_files.utils.text_splitter import split_text
from chat_with_files.utils.embedding import vectorise_text
from chat_with_files.utils.query import build_qa_chain

st.set_page_config(page_title="Chat with File", layout="wide")
st.title("📄 Chat with Your File (PDF or CSV)")

uploaded_file = st.file_uploader("Upload a PDF or CSV", type=["pdf", "csv"])

if uploaded_file:
    file_type = uploaded_file.name.split(".")[-1]
    st.info(f"Processing {uploaded_file}")

    if file_type=="pdf":
        with open(f"{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.read())
        raw_text = load_pdf(uploaded_file.name)
    elif file_type == "csv":
        with open(f"{uploaded_file.name}", "wb") as f:
            f.write(uploaded_file.read())
        raw_text = load_csv(uploaded_file.name)
    else:
        st.error("Unsupported file type.")
        st.stop()

    chunks = split_text(text=raw_text)
    db = vectorise_text(chunks)
    qa_chain = build_qa_chain(db=db)
    st.success("✅ File processed. Ask your questions!")

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.chat_input("Ask something about the file....")
    if user_input:
        response = qa_chain.run(user_input)
        st.session_state.chat_history.append(("Human", user_input))
        st.session_state.chat_history.append(("AI", response))

    for role, message in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(message)