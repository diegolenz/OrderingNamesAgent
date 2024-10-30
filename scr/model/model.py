
class OauthResponse:
    def __init__(self, access_token, token_type):
        self.access_token = access_token
        self.token_type = token_type
    access_token: str
    token_type: str