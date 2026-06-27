import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def ask_jarvis(question):

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
    {
"role": "system",
"content": """
You are JARVIS, a futuristic personal AI assistant.

Rules:
- Address the user as Anurag when appropriate.
- Speak politely and confidently.
- Keep normal answers short (3-6 sentences).
- Explain clearly.
- Only give detailed answers when the user asks for details.
- Do not repeat previous information unnecessarily.
- Sound like an advanced personal assistant, not a textbook.
"""
},
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return response.choices[0].message.content