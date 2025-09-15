from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()  # 👈 this must exist

# Allow CORS for frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this in production to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

def get_chatbot_response(user_message: str) -> str:
    message = user_message.lower()
    if "hello" in message or "hi" in message:
        return "Hello! Welcome to Total Technology System. How can I assist you today?"
    elif "services" in message:
        return "We specialize in IT solutions like software development, cloud, AI/ML, and cybersecurity, as well as GIS services such as mapping, spatial analysis, remote sensing, and GPS surveying. Which service interests you?"
    elif "it" in message and "services" in message:
        return "Our IT services include software development, cloud solutions, AI/ML, and cybersecurity. We also offer IT consulting. What specific IT need do you have?"
    elif "gis" in message or "mapping" in message:
        return "Our GIS services cover mapping, spatial analysis, remote sensing, GPS surveying, and data visualization. For example, we can help with urban planning or environmental monitoring. May I have your email to share more details?"
    elif "quote" in message or "project" in message:
        return "I'd be happy to help with a quote. Could you please share your name, email, and a brief description of your project requirements?"
    elif "email" in message or "contact" in message:
        return "Please provide your email address, and our team will follow up with you shortly."
    else:
        return "I'm here to help with our IT and GIS services. If you have a specific question, feel free to ask. Otherwise, I'll connect you with our expert team for further assistance."

@app.get("/")
def read_root():
    return {"message": "Hello, TTS Chatbot is running 🚀"}

@app.post("/chat")
async def chat(request: ChatRequest):
    response = get_chatbot_response(request.message)
    return JSONResponse(content={"response": response})
