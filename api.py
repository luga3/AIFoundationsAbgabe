import requests
import os

token = os.getenv("GITHUB_TOKEN")

owner = "luga3"
repo = "AIFoundationsAbgabe"

url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
headers = {"Authorization": f"token {token}"}

response = requestsget(url, headers=headers)
if response.status_code != 200:
    raise SystemExit("Fehler beim Abrufen der PRs:", response.status_code, response.text)
pulls = response.json()

for pr in pulls:
    print(f"PR #{pr['number']}: {pr['title']} von {pr['user']['login']}")

#bsp

if not pulls
    print("No pullrequests available, please try again")
else:
    pr_number = pulls[0]["number"]
    comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"

    data = {"body": "-----dummy text-----"}

    comment_response = requests.post(comment_url, headers=headers, json=data)

    if comment_response.status_code == 201:
        print("Kommentar erfolgreich erstellt.")
    else:
        print("Fehler:", comment_response.text)
