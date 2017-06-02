import requests
import json,random

def getSportNews(sport):
    link = "https://skysportsapi.herokuapp.com/sky/getnews/"+ sport +"/v1.0"
    r = requests.get(link)
    data = r.json()
    return data

def getTeamNews(sport, team):
    link = "https://skysportsapi.herokuapp.com/sky/"+ sport +"/getteamnews/"+ team +"/v1.0"
    r = requests.get(link)
    data = r.json()
    return data

def choice_without_repetition(lst):
    i = 0
    while True:
        i = (i + random.randrange(1, len(lst))) % len(lst)
        yield lst[i]


opt = input("Enter 0 or 1: ")

if opt == 0:
    sport = raw_input("Enter the name of sport: ")
    news = getSportNews(sport)
    for i in range(3):
        rand_news = news[random.SystemRandom().randrange(len(news))]
        print rand_news['shortdesc']
else:
    team = raw_input("Enter team name: ")
    sport = raw_input("Enter sport name: ")
    news = getTeamNews(sport, team)
    for i in range(3):
        rand_news = news[random.SystemRandom().randrange(len(news))]
        print rand_news['shortdesc']
