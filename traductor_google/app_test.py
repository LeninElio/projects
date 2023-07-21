import os
from google.cloud import translate
from dotenv import load_dotenv


load_dotenv('private/.env')
PROJECT_ID = os.getenv('PROJECT_ID')


def traducir(texto):
    """Traduce un texto a un idioma dado.
    """
    cliente = translate.TranslationServiceClient()
    parent = f"projects/{PROJECT_ID}/locations/global"

    response = cliente.translate_text(
        request={
            "parent": parent,
            "contents": [texto],
            "mime_type": "text/plain",
            "source_language_code": "es",
            "target_language_code": "ru",
        }
    )

    return response.translations[0].translated_text

traducir = traducir("Este código imprime la siguiente salida: Hola mundo")
print(traducir)
