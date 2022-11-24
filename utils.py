API_TOKEN = 'Token 8e0fee00a18a82f4e672f4f1239252435727dbfe'
import requests
from pprint import pprint


regions = ['mx', 'us-ca'] # Change to your country
with open(r'imgs\023.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': API_TOKEN})
pprint(response.json())



# Calling with a custom engine configuration
import json
with open(r'imgs\020.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=['us-ca'], config=json.dumps(dict(region="strict"))),  # Optional
        files=dict(upload=fp),
        headers={'Authorization': API_TOKEN})