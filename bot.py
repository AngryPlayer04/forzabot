import json
import tweepy
import time


#Autenticação do bot

auth = tweepy.OAuthHandler('jteCxTGMao6r4SRtlrkxzLbeY','IP3bdt6J4U7NHEp3iI4z2516BkwPXLJsDmsXMiJ3KcNf9t3DWp') 
auth.set_access_token('1437949410990858244-Q0K85I54SqYjbIv7ATRGGDszILxEqS', 'LwcZUhBAj6ioVVQdDHoMzBezrPHnEXhQY9bWnyeO7BEjX')

api = tweepy.API(auth)

try: 
    api.verify_credentials()
    print ("Autenticado!")

except:
    print("Não autenticado!")

#Criação do objeto da API

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


#Retweet

search = '#ForzaHorizon4', '#ForzaHorizon', '#Forza','#ForzaPhotography', '#ForzaHorizon5'
numberT = 1

for tweet in tweepy.Cursor(api.search, search).items(numberT):
    try:
        print('Retweet feito')
        tweet.retweet()
        time.sleep(86400)
    except tweepy.TweepError as e:
        raise e.reason
    except StopIteration:
        break





