from google.cloud import translate

def traducir(texto):
    """Traduce un texto a un idioma dado.
    """
    # archivo = '../private/traductorapi.json'
    # os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = archivo
    # $env:GOOGLE_APPLICATION_CREDENTIALS="D:\Proyectos\projects\private\traductorapi.json"

    cliente = translate.TranslationServiceClient()
    parent = "projects/traductorapi-393015/locations/global"

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
