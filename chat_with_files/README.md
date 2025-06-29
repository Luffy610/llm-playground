# 📄 Chat with Your Files – Local RAG Assistant using Gemini & FAISS

Interact with your own PDF or CSV files using Retrieval-Augmented Generation (RAG) and Gemini (Google's LLM). This Streamlit-powered assistant allows you to upload documents, generate embeddings on the fly, and ask questions in a natural chat interface.

## 🚀 Features

- ✅ Upload PDF or CSV files

- ✅ Automatic text extraction, chunking, and embedding

- ✅ Vector search using FAISS

- ✅ Answer questions using Gemini Pro

- ✅ Lightweight, private, and local-friendly setup

- ✅ Clean chat interface with memory

## 🧱 Tech Stack

| Component      | Library                        |
| -------------- | ------------------------------ |
| File Parsing   | `pandas`, `pymupdf`            |
| Text Splitting | `langchain.text_splitter`      |
| Embedding      | `GoogleGenerativeAIEmbeddings` |
| Vector Store   | `FAISS` (`faiss-cpu`)          |
| LLM            | `ChatGoogleGenerativeAI`       |
| Interface      | `Streamlit`                    |

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/your-username/chat-with-your-files.git
cd chat-with-your-files

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

```

## 🔑 Setup Google Gemini API Key

1. Get your key from: https://makersuite.google.com/app/apikey

2. Create a .env file in the project root:

```env
GOOGLE_API_KEY=your-google-api-key-here
```

## ▶️ Run the App
```bash
streamlit run app.py
```

## 📁 Project Structure
```bash
chat-with-files/
├── app.py                       # Streamlit UI
├── loaders/
│   ├── file_loader.py           # File loading logic
├── utils/
│   └── text_splitter.py         # Chunking logic
│   └── embedding.py             # Embedding logic
│   └── query.py                 # Query logic
├── .env                        # Gemini API key
└── requirements.txt
```

## 💡 How It Works

1. User uploads a .pdf or .csv

2. The file is read, parsed, and converted into plain text

3. Text is split into overlapping chunks

4. Chunks are embedded using Gemini's embedding model

5. Stored in a FAISS index for retrieval

6. When the user asks a question, the app:
   - Retrieves relevant chunks from the FAISS index
   - Passes context and question to Gemini Pro
   - Displays the LLM's response in the chat

## 🔒 Privacy & Local Usage

- All file processing and vector generation is local

- Only the LLM call (Gemini) uses an external API

- For a fully local LLM setup, you can swap in llama-cpp, GPT4All, etc.

## ✨ Future Enhancements

- ✅ Add .ipynb notebook support

- 🔄 Export chat as markdown

- 🧠 Add memory per document

- 📚 Handle large files with streaming chunking

- 🕵️ Detect table vs paragraph chunks automatically

# 🧑‍💻 Author

Built with ❤️ by Dhruv Kotwani
