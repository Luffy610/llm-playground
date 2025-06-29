import fitz
import pandas as pd


def load_pdf(file_path:str):
    docs = fitz.open(file_path)
    text = ""
    for page in docs:
        text += page.get_text() + "\n"
    docs.close()
    return text

def load_csv(file_path:str):
    df = pd.read_csv(file_path)
    text = df.to_string(index=False)
    return text


