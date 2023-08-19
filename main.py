import requests
from graph import Graph
from algopy2 import queue


def get_top():
    res=[]
    
    e = open("./rappeurs.txt",'r')
    for l in e:
        if l!="":
            res.append(l[:-1])
    return res
top=get_top()


def get_artists_feats(artist_name):
    # Recherche de l'artiste

    search_url = f"https://api.deezer.com/search/artist?q={artist_name}&limit=1"
    response = requests.get(search_url)


    artist_data = response.json()['data'][0]

    artist_id = artist_data['id']
    artist_name = artist_data['name']
    # Récupération des chansons de l'artiste
    songs_url = f"https://api.deezer.com/artist/{artist_id}/top?limit=1000"
    response = requests.get(songs_url)
    res=[]
    songs_data = response.json()['data']
    for s in songs_data:
        for i in s['contributors']:
            if i['name'] != artist_name:
                if i not in res and i in top:
                    res.append(i,s["title"])
    return res

def print_graph(graph):
    for i in range(len(graph.adjList)):
        print(graph.labels[i], end=" : ")
        for j in graph.adjList[i]:
            print(graph.labels[j], end=", ")
        print()
    print("====================================")



for i in top:
    print(i)
    search_url = f"https://api.deezer.com/search/artist?q={i}&limit=1"
    if len(search_url) != 0
        response = requests.get(search_url)


        artist_data = response.json()['data'][0]

        artist_id = artist_data['id']
        artist_name = artist_data['name']
        i=artist_name
print(top)