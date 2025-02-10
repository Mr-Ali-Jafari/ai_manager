import requests
from typing import Optional, Dict, Any

class PyAIManager:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        """
        Initializes the PyAIManager class.

        :param api_key: API key for authentication
        :param base_url: Base URL of the AI service
        """
        self.api_key = api_key
        self.base_url = base_url

    def get_ai_response(
        self,
        prompt: str,
        model: str,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Sends a request to the AI API and returns the response.

        :param prompt: The user input text
        :param model: The AI model to use
        :param api_key: Optional API key (overrides class-level key)
        :param base_url: Optional base URL (overrides class-level URL)
        :param kwargs: Additional parameters for the API request
        :return: The AI-generated response or an error message
        """
        api_key = api_key or self.api_key
        base_url = base_url or self.base_url

        if not api_key:
            return "Error: API key is missing."
        if not base_url:
            return "Error: Base URL is missing."
        if not model:
            return "Error: Model name must be specified."

        try:
            url = f"{base_url}/chat/completions"
            headers = {
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                **kwargs
            }

            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"].strip()
            else:
                return f"API Error: {response.text}"

        except Exception as e:
            return f"API Connection Error: {str(e)}"

