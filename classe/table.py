import sqlite3


class Table:

    def __init__(self):

        self.nom = "meilleurs_scores"

    def initialisation(self):
        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()
        curseur.executescript("""
            CREATE TABLE IF NOT EXISTS meilleurs_scores(
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                pseudo TEXT,
                score INTEGER
            )
        """)
        connexion.commit()
        connexion.close()


    def remplissage(self):

        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()
        curseur.execute("SELECT COUNT(*) FROM meilleurs_scores;")
        resultat = curseur.fetchone()
        curseur.close()
        connexion.close()

        if resultat[0] < 5:

            connexion = sqlite3.connect("bdd/base_de_donnees.db")
            curseur = connexion.cursor()

            for score in [1, 2, 3, 4, 5]:
                curseur.execute("INSERT INTO meilleurs_scores (pseudo, score) VALUES ('Aucun', 0)")
                connexion.commit()

            curseur.close()
            connexion.close()


    def reset(self):

        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()

        for score in [1, 2, 3, 4, 5]:
            curseur.execute("DELETE FROM meilleurs_scores WHERE id = ?;", (score,))
            connexion.commit()

        curseur.close()
        connexion.close()


    def afficher(self, id):
        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()
        curseur.execute("SELECT * FROM meilleurs_scores WHERE id = ?;", (id, ))
        resultat = curseur.fetchone()
        curseur.close()
        connexion.close()
        return resultat