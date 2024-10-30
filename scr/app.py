import asyncio

import Levenshtein

from scr.service import GeneratedNameService


def organizar_por_similaridade(nomes):
    nome_base = nomes[0]
    outros_nomes = nomes[1:]

    nomes_ordenados = sorted(outros_nomes, key=lambda nome: Levenshtein.distance(nome_base, nome))

    return nome_base, nomes_ordenados



async def main():
    nomes = await GeneratedNameService.getNames()

    nome_base, nomes_ordenados = organizar_por_similaridade(nomes)

    for nome in nomes_ordenados:
        print(nome)

asyncio.run(main())









