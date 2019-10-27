from twython import Twython

APP_KEY = '4yQnOGIKjycuKIIxgPHdPrpIf'
APP_SECRET = '3CK6YFrqWflpk9dW8nk2KpIrDeQZIjGJJWpN1PlfTGT2dLmpaW'
twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)


# store access token permanently in database
ACCESS_TOKEN = twitter.obtain_access_token()

# use the following to make calls for search, etc.
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

results = twitter.search(q="python", result_type='popular')

for _result in results:
    print(_result)
