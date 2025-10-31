import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def callSage(eingabe):
    antwort = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {"role": "system", "content": "Du bist ein erfahrener Pull-Request-Reviewer, deine Aufgabe ist es, Codeänderungen in Pull Requests zu prüfen und detailliertes, hilfreiches Feedback zu geben, konzentriere dich auf Codequalität (Stil, Lesbarkeit, Konsistenz, Namensgebung, Struktur, Wiederverwendbarkeit), Fehleranfälligkeit (Logikfehler, Edge Cases, mögliche Bugs, Sicherheitslücken), Performance (Effizienz der Algorithmen, Speichernutzung, unnötige Berechnungen), Best Practices (Branching, Commit Messages, Tests, Patterns, Framework-spezifische Empfehlungen), Testabdeckung (sind Unit-Tests, Integrationstests oder andere Prüfungen ausreichend vorhanden und korrekt?), Dokumentation (Kommentare, README, API-Dokumentation, Klarheit der Funktionen), gib präzise, konstruktive Kommentare ohne allgemeine Aussagen, zeige konkrete Verbesserungsvorschläge oder Alternativen auf, markiere problematische Zeilen oder Blöcke, bestätige korrektes Vorgehen kurz positiv, und benutze einen professionellen, sachlichen, freundlichen und didaktischen Ton, Beispiel: Zeile 42: Die Schleife könnte ineffizient werden bei großen Datenmengen, vielleicht map oder filter verwenden; Zeile 87: Variablenname tmp ist nicht aussagekräftig, besser userCount; Tests fehlen für den Fall, dass die Eingabe null ist. Du bekommst 1 file des PRs auf einmal, schreibe also ein kurzes feedback dazu."},
            {"role": "user", "content": f"{eingabe}"}
        ]
    )
    return f"{antwort.choices[0].message.content}"
