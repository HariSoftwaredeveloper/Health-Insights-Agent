# 🏥 HIA - Health Intelligence Agent

A Streamlit-based medical report analysis application that leverages Azure OpenAI to provide intelligent insights from uploaded PDF medical reports.

## ✨ Features

- **PDF Upload & Processing**: Upload medical reports (PDF format, max 20MB)
- **Text Extraction**: Automatic text extraction from PDF documents using pdfplumber
- **AI-Powered Analysis**: Intelligent medical report analysis using Azure OpenAI
- **User-Friendly Interface**: Clean and intuitive Streamlit web interface
- **Authentication Ready**: Built-in authentication service structure (expandable)

## 🚀 Tech Stack

- **Frontend**: Streamlit
- **AI/ML**: Azure OpenAI (GPT-4)
- **PDF Processing**: pdfplumber
- **Database**: Supabase (authentication ready)
- **Configuration**: python-dotenv
- **Language**: Python 3.8+

## 📋 Prerequisites

- Python 3.8 or higher
- Azure OpenAI account with API access
- Supabase account (for authentication features)
- Git

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/HIA.git
   cd HIA
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   Edit `.env` file with your credentials:
   ```env
   # Supabase Configuration
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key

   # Azure OpenAI Configuration
   AZURE_OPENAI_API_KEY=your_azure_openai_api_key
   AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
   AZURE_OPENAI_API_VERSION=your_api_version
   AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4o
   ```

## 🏃‍♂️ Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run src/main.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

## 📁 Project Structure

```
HIA/
├── src/
│   ├── auth/
│   │   ├── __init__.py
│   │   └── auth_service.py      # Authentication service
│   ├── config/
│   │   ├── __init__.py
│   │   └── app_config.py        # Application configuration
│   ├── services/
│   │   ├── __init__.py
│   │   └── ai_service.py        # Azure OpenAI service
│   ├── utils/
│   │   ├── __init__.py
│   │   └── pdf_extractor.py     # PDF text extraction
│   └── main.py                  # Main Streamlit application
├── .env                         # Environment variables
├── .gitignore
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## 🔧 Configuration

### Azure OpenAI Setup
1. Create an Azure OpenAI resource in the Azure portal
2. Deploy a GPT-4 model
3. Copy the endpoint, API key, and deployment name to your `.env` file

### Supabase Setup (Optional)
1. Create a new Supabase project
2. Copy the URL and anon key to your `.env` file
3. Configure authentication providers as needed

## 📊 Usage

1. **Upload a PDF**: Use the sidebar to upload a medical report (PDF format)
2. **View Extracted Text**: Preview the extracted text from your PDF
3. **Get AI Analysis**: Click "Analyze Report with AI" to receive intelligent insights
4. **Review Results**: View the formatted AI analysis with health insights

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This application is for educational and demonstration purposes only. The AI-generated insights should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.

## 🐛 Issues

If you encounter any issues or have suggestions, please [open an issue](https://github.com/yourusername/HIA/issues).

## 📞 Contact

[Your Name] - [Your Email] - [Your GitHub Profile]

---

**Note**: Make sure to replace `yourusername` in the repository URLs with your actual GitHub username.
