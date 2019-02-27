from pymongo import MongoClient
from MongoDB import *

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo
films = db.films

actors = {}
#boucle pour ajouter un acteur(key) et ses films(value) joué dans un dico (actors)
for film in films.find():#prendre chaque dico dans la collection films et nommé ce dico "film"
	for actor in film.get("actors"):#prendre chaque acteur du film
		actor = actor.replace("\n","").replace(".","").strip()
		if actor not in actors: # si l'acteur n'est pas une key du dictionnaire 'actors'
			actors[actor]=[]#je créer une key avec le nom de l'acteur et je met pour value une liste
		actors[actor].append(film.get("title"))#je met le nom du film ("title") dans la liste de l'acteur


for actor in actors:
	name = Actor(actor)
	for film in actors[actor]:
		name.add_film(film)
	name.load(db)

