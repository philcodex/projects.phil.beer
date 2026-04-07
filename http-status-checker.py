import requests

def check_url(url):
    try:
        response = requests.get(url, timeout=5)

        if response.status_code == 200:
            return f"{url} → OK (200)"
        else:
            return f"{url} → ERROR ({response.status_code})"

    except requests.exceptions.RequestException as e:
        return f"{url} → FAILED ({e})"


# Get URLs from user input
urls = []
print("Enter URLs to check (press Enter without typing to finish):")
while True:
    url = input("Enter URL: ").strip()
    if not url:
        break
    # Add https:// if no protocol is specified
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
    urls.append(url)

# Check each URL
if urls:
    for url in urls:
        result = check_url(url)
        print(result)
else:
    print("No URLs entered.")