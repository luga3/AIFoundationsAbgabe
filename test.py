import os
from openai import OpenAI

# Deinen API Key einsetzen
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Beispiel: Chat-Anfrage an GPT-5
antwort = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {"role": "system", "content": "Du bist ein hilfreicher Assistent."},
        {"role": "user", "content": "Sag Hi"}
    ]
)

print(antwort.choices[0].message.content)

