from collections  import defaultdict
import string
import re


with open('./data/texto.txt', 'r', encoding='utf-8') as archivo:
    texto = archivo.read()

    regex = re.compile(f'[{re.escape(string.punctuation)}]')

    contar_signos = defaultdict(int)
    for signo in regex.findall(texto):
        contar_signos[signo] += 1

    print(contar_signos)

    cantidad = regex.sub('', texto)

    contador_palabra = defaultdict(int)
    for palabra in cantidad.split():
        contador_palabra[palabra] += 1

    print(dict(contador_palabra))
