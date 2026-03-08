from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

g = Github(os.getenv("GITHUB_ACCESS_TOKEN"))

import requests

def get_pr_diff(repo_name, pr_number):
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    
    # Fetch the diff content
    response = requests.get(pr.diff_url)
    return response.text

def post_comment(repo_name, pr_number, comment):

    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)

    pr.create_issue_comment(comment)
