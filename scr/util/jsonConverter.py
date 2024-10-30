import json

from scr.model.model import OauthResponse


def jsonToOauthResponseConvert(data: str):
    jsonDump = json.dumps(data)
    loadJson = json.loads(jsonDump)

    oauthResponse = OauthResponse(**loadJson)
    return oauthResponse

def jsonToNameListConvert(data: str):
    listNames = list()
    for itemName in data:
        listNames.append(itemName['name'])
    return listNames
