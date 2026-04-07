# github_api.py
# ============================================================
# GitHub API — Tutorial
# Fetch public data from GitHub using the GitHub REST API
# ============================================================

import requests

BASE_URL = "https://api.github.com"
USERNAME = "philcodex"  # change this to any GitHub username


# ---- 1. GET USER PROFILE ----

response = requests.get(f"{BASE_URL}/users/{USERNAME}")
data = response.json()

print("=== GitHub User Profile ===")
print(f"Name:       {data.get('name')}")
print(f"Username:   {data.get('login')}")
print(f"Bio:        {data.get('bio')}")
print(f"Followers:  {data.get('followers')}")
print(f"Following:  {data.get('following')}")
print(f"Public Repos: {data.get('public_repos')}")
print(f"Profile URL:  {data.get('html_url')}")


# ---- 2. GET USER REPOSITORIES ----

response = requests.get(f"{BASE_URL}/users/{USERNAME}/repos")
repos = response.json()

print("\n=== Public Repositories ===")
for repo in repos:
    print(f"- {repo['name']} | {repo['description']}")


# ---- 3. GET A SPECIFIC REPO ----

REPO_NAME = "Learn-Python"
response = requests.get(f"{BASE_URL}/repos/{USERNAME}/{REPO_NAME}")
repo = response.json()

print(f"\n=== Repo: {REPO_NAME} ===")
print(f"Description: {repo.get('description')}")
print(f"Stars:       {repo.get('stargazers_count')}")
print(f"Forks:       {repo.get('forks_count')}")
print(f"Language:    {repo.get('language')}")
print(f"URL:         {repo.get('html_url')}")


# ---- 4. CHECK RATE LIMIT ----
# GitHub allows 60 requests/hour unauthenticated

response = requests.get(f"{BASE_URL}/rate_limit")
limit = response.json()

print("\n=== API Rate Limit ===")
print(f"Limit:     {limit['rate']['limit']}")
print(f"Remaining: {limit['rate']['remaining']}")