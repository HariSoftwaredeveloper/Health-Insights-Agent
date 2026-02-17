import os
from openai import AzureOpenAI
from src.config.app_config import AppConfig

class AIService:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=AppConfig.AZURE_OPENAI_API_KEY,
            api_version=AppConfig.AZURE_OPENAI_API_VERSION,
            azure_endpoint=AppConfig.AZURE_OPENAI_ENDPOINT
        )

    def analyze_medical_report(self, text_content: str, history: list = None):
        """
        Analyzes medical text using the configured Azure model.
        """
        system_prompt = (
            "You are an advanced medical assistant AI. "
            "Analyze the following medical report text and provide personalized health insights. "
            "Format the output clearly with headers."
        )

        messages = [{"role": "system", "content": system_prompt}]
        
        # Add context history if available
        if history:
            messages.extend(history)
            
        messages.append({"role": "user", "content": f"Analyze this report:\n\n{text_content}"})

        try:
            response = self.client.chat.completions.create(
                model=AppConfig.AZURE_DEPLOYMENT_NAME,
                messages=messages,
                temperature=0.7,
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error connecting to AI service: {str(e)}"
