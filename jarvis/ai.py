import os

from dotenv import load_dotenv
from groq import Groq
from duckduckgo_search import DDGS


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def web_search(query):

    results = []


    with DDGS() as ddgs:

        for result in ddgs.text(query, max_results=3):

            results.append(result["body"])


    return "\n".join(results)




def ask_jarvis(question):


    response = client.chat.completions.create(


        model="llama-3.1-8b-instant",


        messages=[


            {

                "role": "system",

                "content": """
You are JARVIS, a futuristic personal AI assistant.

Personality:
- Speak politely and naturally.
- Address the user as Anurag when appropriate.
- Keep normal answers short.
- Explain clearly.
- Sound like an advanced assistant.
"""
            },


            {

                "role": "user",

                "content": question

            }


        ]

    )


    return response.choices[0].message.content