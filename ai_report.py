import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_report(titles):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    text = "\n".join(titles)

    payload = {
        "model": "openai/gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": f"""
Analyze these 10 AI news headlines:

{text}

Return ONLY:

Overall Summary:
(5-6 lines max)

Overall Highlights:
- point 1
- point 2
- point 3
- point 4
- point 5
"""
            }
        ]
    }

    res = requests.post(url, headers=headers, json=payload)
    return res.json()["choices"][0]["message"]["content"]