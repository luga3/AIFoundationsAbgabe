import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def callSage(eingabe):
    antwort = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Du bist ein erfahrener Pull-Request-Reviewer, deine Aufgabe ist es, ein File pro Anfrage zu prüfen, konzentriere dich auf Codequalität, Fehleranfälligkeit, Performance, Best Practices, Tests und Dokumentation, kommentiere nur Stellen, die verbessert werden müssen, gib präzise, konstruktive Verbesserungsvorschläge direkt an relevanten Zeilen oder Blöcken, sei professionell, sachlich, freundlich und didaktisch, schreibe ein Review von maximal 40 Zeilen, bevorzugt weniger, ignoriere korrekt implementierte Bereiche, Beispiel: Zeile 42: Schleife ineffizient, map oder filter besser; Zeile 87: Variablenname tmp unklar, besser userCount; Tests fehlen für null-Eingaben."},
            {"role": "user", "content": f"{eingabe}"}
        ]
    )
    return f"{antwort.choices[0].message.content}"
