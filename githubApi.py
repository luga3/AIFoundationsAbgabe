import requests
import os
from sage import call_sage

token = os.getenv("GITHUB_TOKEN")

owner = input("Type Account Name: ")
repo = input("Type Repository Name: ")
pr_number = input("Type PR number: ")

url_pr_files = f"https://api.github.com/repos/{owner}/{repo}/pulls/{pr_number}/files"

headers = {"Authorization": f"token {token}"}

def comment_all_files():
    file_response = requests.get(url_pr_files, headers=headers)
    files = file_response.json()

    for file in files:
        create_comment(file)
        
def create_comment(file):
    file_name = file['filename']
    sage_answer = call_sage(f"Changes in {file_name}: " + file.get("patch", f"No changes in {file['filename']}"))
    post_comment(sage_answer, file_name)

def post_comment(comment, file_name):
    comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{pr_number}/comments"
    
    data = {"body": f"Sage reviewed {file_name}\n\n" + comment}

    comment_response = requests.post(comment_url, headers=headers, json=data)
    if comment_response.status_code == 201:
        print(f"Comment posted for file: {file_name}")
    else:
        print("Error, comment was dismissed:", comment_response.status_code, comment_response.text)

def start_codeSage():
    comment_all_files()
