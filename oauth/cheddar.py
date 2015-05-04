"""
Cheddar OAuth2 backend, docs at:
    http://docs.cheddarcard.com/
"""
from social.backends.oauth import BaseOAuth2


class CheddarOAuth2(BaseOAuth2):
    name = 'cheddar'
    AUTHORIZATION_URL = 'http://api.cheddarcard.com/oauth/authorize/'
    ACCESS_TOKEN_METHOD = 'POST'
    ACCESS_TOKEN_URL = 'http://api.cheddarcard.com/oauth/token/'
    REDIRECT_STATE = False

    def get_user_details(self, response):
        """Return user details from Cheddar account"""
        email = response['email']
        username = response['email']
        return {'username': username,
                'email': email}

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json('http://api.cheddarcard.com/v0.1/user', headers={
            'Authorization': 'Bearer %s' % access_token
        })
