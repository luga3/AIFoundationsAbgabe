import requests

# Dein persönlicher GitHub Access Token
token = ""

# Repository-Daten
owner = "luga3"
repo = "AIFoundationsAbgabe"

# Beispiel: Alle offenen Pull Requests abrufen
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
headers = {"Authorization": f"token {token}"}

response = requests.get(url, headers=headers)
pulls = response.json()

for pr in pulls:
    print(f"PR #{pr['number']}: {pr['title']} von {pr['user']['login']}")

# Beispiel: Kommentar zu einem Pull Request hinzufügen
pr_number = pulls[0]["number"]  # z.B. den ersten PR nehmen
comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

data = {"body": "Danke fuer deinen Beitrag! Ich schaue mir das gleich an."}

comment_response = requests.post(comment_url, headers=headers, json=data)

if comment_response.status_code == 201:
    print("Kommentar erfolgreich erstellt.")
else:
    print("Fehler:", comment_response.status_code, comment_response.text)
