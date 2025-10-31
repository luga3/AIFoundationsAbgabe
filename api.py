import requests
import os

# Dein persönlicher GitHub Access Token
token = os.getenv("GITHUB_TOKEN")

# Repository-Daten
owner = "luga3"
repo = "AIFoundationsAbgabe"

# Beispiel: Alle offenen Pull Requests abrufen
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
headers = {"Authorization": f"token {token}"}

response = requests.get(url, headers=headers)
if response.status_code != 200:
    raise SystemExit("Fehler beim Abrufen der PRs:", response.status_code, response.text)
pulls = response.json()

for pr in pulls:
    print(f"PR #{pr['number']}: {pr['title']} von {pr['user']['login']}")

#bsp

if not pulls:
    print("no pullrequests available")
else:
    pr_number = pulls[0]["number"]
    comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

    data = {"body": "Danke fuer deinen Beitrag! Ich schaue mir das gleich an."}

    comment_response = requests.post(comment_url, headers=headers, json=data)

    if comment_response.status_code == 201:
        print("Kommentar erfolgreich erstellt.")
    else:
        print("Fehler:", comment_response.status_code, comment_response.text)
