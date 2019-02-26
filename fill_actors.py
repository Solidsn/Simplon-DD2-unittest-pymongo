from pymongo import MongoClient
from MongoDB import *

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo
films = db.films
unique_actors = []

for elem in db.films.find():
	for el in elem["actors"]:
		actor = el.replace("\n","").strip()
		if actor not in unique_actors:
			unique_actors.append(actor)
for actor in unique_actors:
	name = Actor(actor)
	name.load(db)
