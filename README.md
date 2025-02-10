# PY AI Manager

A Python library to connect to AI APIs.

## Installation

```bash
pip install py-ai-manager

```


# Usage:
```py
from py_ai_manager.core import PyAIManager

ai = PyAIManager(api_key="your_api_key", base_url="https://api.example.com")
response = ai.get_ai_response("Hello, how are you?", model="custom-model")
print(response)

```
