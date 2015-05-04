from cheddarpy import Cheddar
from django.shortcuts import render


def home(request):

  if request.user.is_authenticated():

    access_token = request.user.social_auth.all()[0].extra_data['access_token']    
    api = Cheddar(access_token)
    account = api.accounts()

    return render(request, 'app/dashboard.html', {
      "accounts": accounts
    })

  else:
    return render(request, 'app/home.html')
