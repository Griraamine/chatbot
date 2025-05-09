from fastapi import FastAPI
from pydantic import BaseModel
from deepseek import query_deepseek
from openfoodfacts import search_product

app = FastAPI()

class Query(BaseModel):
    question: str

@app.post("/chatbot")
def chatbot(query: Query):
    try:
        ai_response = query_deepseek(query.question)
        message = ai_response.get("choices", [{}])[0].get("message", {}).get("content", "")
        return {"response": message}
    except Exception as e:
        print("🔥 ERROR:", e)
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
