import requests
import os
from assistent import callSage

token = os.getenv("GITHUB_TOKEN")

owner = "luga3"
repo = "AIFoundationsAbgabe"
pr_number = 6

repo_url = f"https://api.github.com/repos/{owner}/{repo}"
pr_url = repo_url + "/pulls"
pr_files_url = pr_url + f"/{pr_number}/files"
headers = {"Authorization": f"token {token}"}

def comment_files():
    file_response = requests.get(pr_files_url, headers=headers)
    files = file_response.json()

    for file in files:
        sage_answer = callSage(f"Changes in {file['filename']}: " + file.get("patch", f"No changes in {file['filename']}"))
        post_comment(sage_answer)

def post_comment(comment):
    comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    data = {"body": comment}

    comment_response = requests.post(comment_url, headers=headers, json=data)

    if comment_response.status_code == 201:
        print("Kommentar erfolgreich erstellt.")
    else:
        print("Fehler:", comment_response.status_code, comment_response.text)


if __name__ == "__main__":
    comment_files()
