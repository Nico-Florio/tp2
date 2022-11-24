API_TOKEN = 'Token 8e0fee00a18a82f4e672f4f1239252435727dbfe'
import requests

regions: list = ['ar', 'us-ca'] 
with open(r'imgs\023.png', 'rb') as fp:
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  
        files=dict(upload=fp),
        headers={'Authorization': API_TOKEN})
    
plate_number : str = response.json()['results'][0]['plate']
print(plate_number)
