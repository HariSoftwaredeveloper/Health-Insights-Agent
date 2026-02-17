import streamlit as st
from src.auth.auth_service import AuthService
from src.services.ai_service import AIService
from src.utils.pdf_extractor import extract_text_from_pdf
from src.config.app_config import AppConfig

# Page Config
st.set_page_config(
    page_title="HIA - Health Intelligence Agent",
    page_icon="🏥",
    layout="wide"
)

# Initialize Services
if 'auth_service' not in st.session_state:
    st.session_state.auth_service = AuthService()
if 'ai_service' not in st.session_state:
    st.session_state.ai_service = AIService()

def main():
    st.title("🏥 Medical Report Analysis AI")

    # Simple Session Check (Expand this for full auth flow)
    # For demo purposes, we skip the full login UI rendering here
    # but the service is initialized.
    
    with st.sidebar:
        st.header("Upload Report")
        uploaded_file = st.file_uploader(
            "Upload PDF (Max 20MB)", 
            type=['pdf']
        )
        
    if uploaded_file:
        if uploaded_file.size > AppConfig.MAX_FILE_SIZE_MB * 1024 * 1024:
            st.error("File size exceeds 20MB limit.")
            return

        with st.spinner("Extracting text from PDF..."):
            text_content, error = extract_text_from_pdf(uploaded_file)
            
        if error:
            st.error(f"Error reading PDF: {error}")
        elif text_content:
            st.success("PDF processed successfully!")
            
            with st.expander("View Extracted Text"):
                st.text(text_content[:1000] + "...") # Preview

            if st.button("Analyze Report with AI"):
                with st.spinner("Generating insights via Azure OpenAI..."):
                    analysis = st.session_state.ai_service.analyze_medical_report(
                        text_content
                    )
                    st.markdown("### 🩺 AI Analysis")
                    st.markdown(analysis)
    else:
        st.info("Please upload a medical report (PDF) to begin.")

if __name__ == "__main__":
    main()