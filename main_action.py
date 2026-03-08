import os
import json
from app.github_service import get_pr_diff, post_comment
from app.reviewer import review_code

def main():
    # GitHub Action provides the path to the event payload
    event_path = os.getenv("GITHUB_EVENT_PATH")
    if not event_path:
        print("Error: GITHUB_EVENT_PATH not found. This script should run in a GitHub Action.")
        return

    with open(event_path, "r") as f:
        event_payload = json.load(f)

    # Extract repository and PR information
    repo_name = os.getenv("GITHUB_REPOSITORY")
    pr_number = event_payload.get("pull_request", {}).get("number")

    if not pr_number:
        print("Error: Could not find PR number in event payload.")
        return

    print(f"Reviewing PR #{pr_number} in {repo_name}...")

    try:
        # 1. Fetch the diff
        diff = get_pr_diff(repo_name, pr_number)
        
        # 2. Get AI review
        print("Requesting AI review from Groq...")
        review_text = review_code(diff)
        
        # 3. Post the review as a comment
        print("Posting review comment to GitHub...")
        post_comment(repo_name, pr_number, review_text)
        
        print("Successfully posted AI review!")
        
    except Exception as e:
        print(f"Failed to complete AI review: {e}")

if __name__ == "__main__":
    main()
