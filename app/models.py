from cheddarpy import Cheddar
from django.contrib.auth.models import User 
from django.db import models

# monkey patch this on, sloppy but it works
def get_cheddar_api(self):
  access_token = self.social_auth.all()[0].extra_data['access_token']
  return Cheddar(access_token)

User.get_cheddar_api = get_cheddar_api

# TODO use a custom/proxy user model
