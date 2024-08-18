from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
    
    def chat_gpt(self, prompt):
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content.strip()

def generate_response_from_logs(relevant_logs, api_key):
    client = OpenAIClient(api_key)
    combined_logs = "\n".join(relevant_logs)
    
    prompt = (
        f"Apache loglarına göre şu soruyu yanıtla: \n\n{combined_logs}\n\n"
        f"Bu log verilerini kullanarak doğru ve ilgili bir yanıt ver."
    )
    
    return client.chat_gpt(prompt)
