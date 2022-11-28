import os
# import whisper (revisar esto)
import requests

API_TOKEN = 'Token 8e0fee00a18a82f4e672f4f1239252435727dbfe'


def obtener_patente(ruta_foto: str, primer_intento = True):        
    try:
        regions: list = ['ar', 'us-ca'] 
        with open(ruta_foto) as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(regions=regions),  
                files=dict(upload=fp),
                headers={'Authorization': API_TOKEN})
        patente : str = response.json()['results'][0]['plate']
        return patente
    except:
        if primer_intento:
            directorio = os.path.dirname(os.path.abspath(__file__))
            ruta_absoluta_foto = directorio + ruta_foto
            return obtener_patente(ruta_absoluta_foto, False)

# COMENTO ESTO PORQUE NO ME PRMITE CORRER EL PROGRAMA MAIN ( Error con el whisper a pesar de ya estar descargado)  
# def obtener_texto_audio(ruta_audio: str) -> list:
#         directorio = os.path.dirname(os.path.abspath(__file__))
#         ruta_absoluta_audio = directorio.strip() + "\\"+  ruta_audio.strip()
#         audio_texto = []
#         model = whisper.load_model("base")
#         audio = whisper.load_audio(ruta_absoluta_audio)
#         audio = whisper.pad_or_trim(audio)
#         mel = whisper.log_mel_spectrogram(audio).to(model.device)
#         # probs = model.detect_language(mel)
#         options = whisper.DecodingOptions(fp16 = False)
#         result = whisper.decode(model, mel, options)
#         audio_texto.append(result.text)
#         return " ".join(audio_texto)