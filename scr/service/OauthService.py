import requests

from scr.util.jsonConverter import jsonToOauthResponseConvert

urlApiGenerateNames ="http://127.0.0.1:8000/"
user= "teste4"
password= "teste"


async def callOauth():

    json = {
        "username": "teste4",
        "password": "teste"
    }
    response = requests.post(urlApiGenerateNames + "/auth/token", data=json)
    print(response)
    if response.status_code == 200:
        data =  response.json()
        return jsonToOauthResponseConvert(data)
    else:
       print(f"Erro na requisição: {response.status_code}")
       raise Exception("Falha ao inserir usuario ")