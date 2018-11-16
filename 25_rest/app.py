# Derek Song
# SoftDev1 pd8
# K26 -- Getting More REST
# 2018 - 11 - 16

from flask import Flask, render_template
import urllib, json

app = Flask(__name__)

@app.route("/")
def home():

    #oxford dictionary
    app_id='de9afc70'
    app_key='fe2edc1a976f63e88441f47ae69a3fb5'
    language='en'
    word='toxic'

    # accessing and reading api
    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/'  + language + '/'  + word.lower()
    u = requests.get(url, headers={'app_id':app_id, 'app_key':app_key})

    #converting the json object string into a dict
    info = json.loads(u.text)
    print ("-----OXFORD------")
    print (info)
    print ("-----------------")

    word=info["results"][0]["id"],
    definition=info["results"][0]["lexicalEntries"][0]["entries"][0]['senses'][0]['definitions'][0]

    #MTA

    # accessing and reading api
    url = 'http://mtaapi.herokuapp.com/stop?id=120S'
    u = urllib.request.urlopen(url)

    #converting the json object string into a dict
    info = json.loads(u.read())
    print ("-----MTA------")
    print (info)
    print ("-----------------")

    station = info['result']['name']
    latitude = info['result']['lat']
    longitude = info['result']['lon']

    #THE MET

    # accessing and reading api
    url = 'https://collectionapi.metmuseum.org/public/collection/v1/objects/1865'
    u = urllib.request.urlopen(url)

    #converting the json object string into a dict
    info = json.loads(u.read())
    print ("-----THE MET------")
    print (info)
    print ("-----------------")

    title = info['title']
    picture = info['primaryImage']
    location = info['department']

    #passing in api values to template
    return render_template("index.html",
                           word=word[0],
                           definition=definition,
                           station=station,
                           latitude=latitude,
                           longitude=longitude,
                           title=title,
                           picture=picture,
                           location=location,
                           )


if __name__ == "__main__":
    app.debug = True
    app.run()
