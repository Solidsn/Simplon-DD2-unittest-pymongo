class Film:

  def __init__(self, id):
    self.id = id

  def get_nb_films(db):
    # retourne le nombre de films présents dans la base
    films = db.films

    return films.count()
    
  def get_actors(self, db):
    # retourne la liste des acteurs du film
    actors = []
    for elem in db.films.find_one(self.id)["actors"]:
      actors.append(elem)

    return actors

class Actor:

  def __init__(self, name):
    self.name = name
    self.films = []

  def add_film(self, film):
    self.films.append(film)

  def load(self, db):
    actors = db.actors

    # ajoute l'acteur dans la base de données
    actors.insert_one({"name":self.name})

  def get_nb_actors(db):
    # retourne le nombre d'acteurs présents dans la base

    return 0
    

