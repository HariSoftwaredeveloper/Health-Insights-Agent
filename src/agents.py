import concurrent.futures
from openai import AzureOpenAI
from src.config import Config

class MedicalAgentSystem:
    def __init__(self):
        self.client = AzureOpenAI(
            api_key=Config.API_KEY,
            api_version=Config.API_VERSION,
            azure_endpoint=Config.ENDPOINT
        )

    def _call_gpt(self, system_prompt, user_content):
        """Helper function to call Azure OpenAI"""
        try:
            response = self.client.chat.completions.create(
                model=Config.DEPLOYMENT_NAME,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_content}
                ],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

    def cardiologist_agent(self, report):
        prompt = """
        You are an expert Cardiologist. 
        Focus: Detect cardiac issues such as arrhythmias or structural abnormalities.
        Output: Provide an assessment and specific recommendations (tests, monitoring).
        """
        return self._call_gpt(prompt, report)

    def psychologist_agent(self, report):
        prompt = """
        You are an expert Psychologist.
        Focus: Identify psychological conditions (e.g., panic disorder, anxiety).
        Output: Provide an assessment and specific recommendations (therapy, stress management).
        """
        return self._call_gpt(prompt, report)

    def pulmonologist_agent(self, report):
        prompt = """
        You are an expert Pulmonologist.
        Focus: Assess respiratory causes for symptoms (e.g., asthma, breathing disorders).
        Output: Provide an assessment and specific recommendations (lung function tests, exercises).
        """
        return self._call_gpt(prompt, report)

    def summary_agent(self, report, card_res, psych_res, pulm_res):
        """Synthesizes the findings from all specialists."""
        prompt = """
        You are a Chief Medical Officer. 
        Review the original report and the findings from the Cardiologist, Psychologist, and Pulmonologist.
        
        Task:
        1. Synthesize the findings.
        2. List exactly THREE possible health issues with reasoning based on the specialists' input.
        3. Provide a final cohesive conclusion.
        """
        combined_input = f"""
        ORIGINAL REPORT: {report}
        
        CARDIOLOGIST FINDINGS: {card_res}
        PSYCHOLOGIST FINDINGS: {psych_res}
        PULMONOLOGIST FINDINGS: {pulm_res}
        """
        return self._call_gpt(prompt, combined_input)

    def analyze_case(self, report):
        """Runs the 3 specialist agents in parallel using Threading."""
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # Schedule the 3 agents to run at the same time
            future_card = executor.submit(self.cardiologist_agent, report)
            future_psych = executor.submit(self.psychologist_agent, report)
            future_pulm = executor.submit(self.pulmonologist_agent, report)

            # Wait for results
            card_res = future_card.result()
            psych_res = future_psych.result()
            pulm_res = future_pulm.result()

        # Run the summarizer (sequential, needs previous inputs)
        summary = self.summary_agent(report, card_res, psych_res, pulm_res)

        return {
            "cardiologist": card_res,
            "psychologist": psych_res,
            "pulmonologist": pulm_res,
            "summary": summary
        }
