import requests
import os
from assistent import call_sage

token = os.getenv("GITHUB_TOKEN")

owner = "luga3"
repo = "AIFoundationsAbgabe"
pr_number = input("Type PR number: ")

repo_url = f"https://api.github.com/repos/{owner}/{repo}"
pr_url = repo_url + "/pulls"
pr_files_url = pr_url + f"/{pr_number}/files"
headers = {"Authorization": f"token {token}"}

def comment_all_files():
    file_response = requests.get(pr_files_url, headers=headers)
    files = file_response.json()

    for file in files:
        comment_fiel(file)
        
def comment_fiel(file):
    file_name = file['filename']
    sage_answer = call_sage(f"Changes in {file_name}: " + file.get("patch", f"No changes in {file['filename']}"))
    post_comment(sage_answer, file_name)

def post_comment(comment, file_name):
    comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    data = {"body": f"Sage reviewed {file_name}\n" + comment}

    comment_response = requests.post(comment_url, headers=headers, json=data)

    if comment_response.status_code == 201:
        print(f"Comment posted for file: {file_name}")
    else:
        print("Fehler:", comment_response.status_code, comment_response.text)


if __name__ == "__main__":
    comment_all_files()
