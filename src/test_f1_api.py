import requests

response = requests.get("https://f1api.dev/api/seasons")

print(response.json()["championships"])