from django.shortcuts import render


def home(request):

  if request.user.is_authenticated():

    api = request.user.get_cheddar_api()
    accounts = api.accounts()['accounts']

    return render(request, 'app/dashboard.html', {
      "accounts": accounts
    })

  else:
    return render(request, 'app/home.html')

def account(request, account_id):

  api = request.user.get_cheddar_api()
  account = api.account(account_id)
  transactions = api.transactions(account_id)["transactions"]

  return render(request, 'app/account.html', {
    "account": account,
    "transactions": transactions
  })
