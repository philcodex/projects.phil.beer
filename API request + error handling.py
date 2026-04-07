import requests
import json

url = "https://api.github.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data))  # print JSON for jq
    else:
        print(json.dumps({
            "error": f"Request failed with status {response.status_code}"
        }))

except requests.exceptions.RequestException as e:
    print(json.dumps({
        "error": str(e)
    }))