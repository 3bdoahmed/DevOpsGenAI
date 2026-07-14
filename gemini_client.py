from google import genai

# class to interact with the Gemini API
class GeminiClient:
# constructor to initialize the GeminiClient with an API key
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)
# method to receive prompt and respond with generated content from the Gemini API
    def generate(self, prompt):
        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text