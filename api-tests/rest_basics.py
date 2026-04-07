# rest_basics.py
# ============================================================
# REST API Basics — Tutorial
# Learn the fundamentals of working with REST APIs in Python
# Uses JSONPlaceholder — a free fake API for testing
# Docs: https://jsonplaceholder.typicode.com
# ============================================================

import requests
import json

BASE_URL = "https://jsonplaceholder.typicode.com"


# ---- 1. WHAT IS A REST API ----
# REST = Representational State Transfer
# An API lets your code talk to another service over the internet
# You send a request to a URL and get data back (usually JSON)
#
# The 4 main request types:
#   GET    — fetch/read data
#   POST   — create new data
#   PUT    — update existing data
#   DELETE — remove data


# ---- 2. YOUR FIRST GET REQUEST ----
# Fetch a single post from the API

print("=== GET — Fetch a single post ===")

response = requests.get(f"{BASE_URL}/posts/2")

print(f"Status Code: {response.status_code}")  # 200 = success
print(f"Response: {response.json()}")


# ---- 3. UNDERSTANDING STATUS CODES ----
# The status code tells you if the request worked or not
#
# 2xx — Success
#   200 — OK (request worked)
#   201 — Created (new item created)
#
# 4xx — Client errors (something wrong with your request)
#   400 — Bad Request
#   401 — Unauthorised (need to log in)
#   403 — Forbidden (not allowed)
#   404 — Not Found
#
# 5xx — Server errors (something wrong on their end)
#   500 — Internal Server Error

print("\n=== Checking Status Codes ===")

response = requests.get(f"{BASE_URL}/posts/1")

if response.status_code == 200:
    print("✓ Success!")
elif response.status_code == 404:
    print("✗ Not found!")
else:
    print(f"Something went wrong: {response.status_code}")


# ---- 4. READING THE RESPONSE ----
# response.json()    — parses the JSON into a Python dict
# response.text      — returns raw response as a string
# response.status_code — the HTTP status code

print("\n=== Reading the Response ===")

response = requests.get(f"{BASE_URL}/posts/1")
data = response.json()

print(f"Type: {type(data)}")         # dict
print(f"ID:     {data['id']}")
print(f"Title:  {data['title']}")
print(f"Body:   {data['body']}")
print(f"UserID: {data['userId']}")


# ---- 5. GET MULTIPLE ITEMS ----
# Fetch a list of items — returns a list of dicts

print("\n=== GET — Fetch multiple posts ===")

response = requests.get(f"{BASE_URL}/posts")
posts = response.json()

print(f"Total posts returned: {len(posts)}")
print("\nFirst 3 posts:")
for post in posts[:3]:
    print(f"  [{post['id']}] {post['title']}")


# ---- 6. QUERY PARAMETERS ----
# Filter or modify results by adding params to your request
# This is like adding ?userId=1 to the URL

print("\n=== GET with Query Parameters ===")

params = {"userId": 1}
response = requests.get(f"{BASE_URL}/posts", params=params)
posts = response.json()

print(f"Posts by userId 1: {len(posts)}")
for post in posts:
    print(f"  - {post['title']}")


# ---- 7. POST REQUEST ----
# Send data to the API to create a new item
# Pass your data as json= and it handles the rest

print("\n=== POST — Create a new post ===")

new_post = {
    "title": "My Python REST Tutorial",
    "body": "Learning how to use REST APIs with Python and requests",
    "userId": 1
}

response = requests.post(f"{BASE_URL}/posts", json=new_post)
created = response.json()

print(f"Status Code: {response.status_code}")   # 201 = created
print(f"New post ID:  {created['id']}")
print(f"Title:        {created['title']}")


# ---- 8. PUT REQUEST ----
# Update an existing item — replaces the whole object

print("\n=== PUT — Update a post ===")

updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "This content has been updated",
    "userId": 1
}

response = requests.put(f"{BASE_URL}/posts/1", json=updated_post)
print(f"Status Code: {response.status_code}")   # 200 = success
print(f"Updated post: {response.json()}")


# ---- 9. DELETE REQUEST ----
# Remove an item from the API

print("\n=== DELETE — Remove a post ===")

response = requests.delete(f"{BASE_URL}/posts/1")
print(f"Status Code: {response.status_code}")   # 200 = deleted
print("Post deleted successfully")


# ---- 10. HEADERS ----
# Headers pass extra info with your request
# Common uses: content type, API keys, auth tokens

print("\n=== Request with Headers ===")

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.get(f"{BASE_URL}/posts/1", headers=headers)
print(f"Status Code: {response.status_code}")
print(f"Content-Type sent: {headers['Content-Type']}")


# ---- 11. PRETTY PRINTING JSON ----
# json.dumps() formats JSON to be human readable
# indent=2 adds spacing

print("\n=== Pretty Printed JSON ===")

response = requests.get(f"{BASE_URL}/users/1")
data = response.json()
print(json.dumps(data, indent=2))


# ---- 12. TIMEOUT ----
# Always set a timeout so your script doesn't hang forever
# timeout=5 means give up after 5 seconds

print("\n=== Request with Timeout ===")

response = requests.get(f"{BASE_URL}/posts/1", timeout=5)
print(f"Status Code: {response.status_code}")


# ---- 13. ERROR HANDLING ----
# Wrap requests in try/except to handle failures gracefully
# raise_for_status() raises an exception for 4xx and 5xx codes

print("\n=== Error Handling ===")

try:
    response = requests.get(f"{BASE_URL}/posts/1", timeout=5)
    response.raise_for_status()
    data = response.json()
    print(f"✓ Success: {data['title']}")

except requests.exceptions.Timeout:
    print("✗ Request timed out — server took too long")

except requests.exceptions.ConnectionError:
    print("✗ Connection error — check your internet connection")

except requests.exceptions.HTTPError as e:
    print(f"✗ HTTP error: {e}")

except requests.exceptions.RequestException as e:
    print(f"✗ Something went wrong: {e}")


# ---- 14. PUTTING IT ALL TOGETHER ----
# A clean reusable function that fetches and prints a post

print("\n=== Reusable Function ===")

def get_post(post_id):
    try:
        response = requests.get(f"{BASE_URL}/posts/{post_id}", timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching post {post_id}: {e}")
        return None

post = get_post(1)
if post:
    print(f"Title: {post['title']}")
    print(f"Body:  {post['body']}")