import requests
from scr.model.model import OauthResponse
from scr.service import OauthService


from scr.util.jsonConverter import jsonToNameListConvert

urlApiGenerateNames ="http://127.0.0.1:8000"


async def getNames():
    ouathResponse: OauthResponse = await OauthService.callOauth()


    headers = {
        "Authorization": ouathResponse.token_type + " " + ouathResponse.access_token,
        "Content-Type": "application/json"
    }
    response = requests.get(urlApiGenerateNames + "/names-generator/get-names", headers=headers)
    if response.status_code == 200:
        data = response.json()
        return jsonToNameListConvert(data)
    else:
       print(f"Erro na requisição: {response.status_code}")
       raise Exception("Falha ao buscar nomes ")
