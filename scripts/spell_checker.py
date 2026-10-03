from urllib import response

from ipykernel.jsonutil import json_clean
import requests
import json

api_key = "API_KEY"  # Replace with your actual API key

sample_text = "Ths is a smple txt with sme speling errors."

data = {"text": sample_text}
params = {
    "mkt": "en-US",
    "mode": "proofing",
    }

headers = {
    "Ocp-Apim-Subscription-Key": api_key,
    "Content-Type": "application/x-www-form-urlencoded"
    }
response = response.post(endpoint, headers=headers, params=params, data=data)
json_response = response.json()
print(json.dump(json_response, indent=4))