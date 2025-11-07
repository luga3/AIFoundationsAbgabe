import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def call_sage(eingabe):
    with open("configuration.txt", "r", encoding="utf-8") as f:
        configuration_text = f.read()
    
    antwort = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": f"{configuration_text}"},
            {"role": "user", "content": f"{eingabe}"}
        ]
    )
    return f"{antwort.choices[0].message.content}"
