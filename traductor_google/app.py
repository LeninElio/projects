import os
import time
from google.cloud import translate_v3beta1 as translate
from dotenv import load_dotenv


load_dotenv('private/.env')
PROJECT_ID = os.getenv('PROJECT_ID')


def traducir_documento(
        project_id: str,
        file_path: str,
        nombre: str,
    ) -> translate.TranslationServiceClient:
    """
    Traduce un documento usando Translation API V3.
    """

    client = translate.TranslationServiceClient()
    location = "us-central1"
    parent = f"projects/{project_id}/locations/{location}"

    with open(file_path, "rb") as document:
        document_content = document.read()

    document_input_config = {
        "content": document_content,
        "mime_type": "application/pdf",
    }

    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": "es",
            "document_input_config": document_input_config,
        }
    )

    with open(f'./data/es_{nombre}.pdf', 'wb') as salida:
        salida.write(response.document_translation.byte_stream_outputs[0])

    print(f"Lenguaje detectado - {response.document_translation.detected_language_code}")

    return response


if __name__ == '__main__':
    for i in range(1, 27):
        NOMBRE = f'parte{i}'
        PATH = f'./data/{NOMBRE}.pdf'
        traducir_documento(PROJECT_ID, PATH, NOMBRE)
        print('-' * 30)
        print(f'{i}.- Archivo {NOMBRE} traducido.')
        print('==> Espera de 5 segundos.')
        print('-' * 30)
        time.sleep(5)
