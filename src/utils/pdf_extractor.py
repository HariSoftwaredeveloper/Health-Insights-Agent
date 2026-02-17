import pdfplumber
import io

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a Streamlit UploadedFile object.
    """
    text = ""
    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return None, str(e)
    
    return text, None
