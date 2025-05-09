import requests

DEEPSEEK_API_KEY = "sk-e0050819e4c14cd68b393de848a27f77"

def query_deepseek(prompt: str) -> dict:
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful nutrition assistant. Only answer nutrition or food-related health questions in a very short and concise way (max 100 words) from openfoodfacts only. Do not give general health or medical advice."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print("❌ DeepSeek error:", e)
        return {"error": str(e)}
