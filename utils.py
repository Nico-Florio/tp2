import requests
API_TOKEN = 'Token 8e0fee00a18a82f4e672f4f1239252435727dbfe'


def obtener_patente(ruta_foto: str):        
        regions: list = ['ar', 'us-ca'] 
        with open(ruta_foto) as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),  
                files=dict(upload=fp),
                headers={'Authorization': API_TOKEN})
        patente : str = response.json()['results'][0]['plate']
        return patente