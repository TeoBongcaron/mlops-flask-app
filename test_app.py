import requests

response = requests.post(
    "http://localhost:8080/predict",
    json={"weight": 180}
)

print("Status:", response.status_code)
print("Body:", response.text)
