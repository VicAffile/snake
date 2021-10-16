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

            for index in [1, 2, 3, 4, 5]:
                curseur.execute("INSERT INTO meilleurs_scores (pseudo, score) VALUES ('Aucun', 0)")
                connexion.commit()

            curseur.close()
            connexion.close()


    def reset(self):

        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()

        for id in [1, 2, 3, 4, 5]:
            curseur.execute("UPDATE meilleurs_scores SET pseudo = ?, score = ? WHERE id = ?;",('Aucun', 0, id,))
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


    def minimum(self):
        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()
        curseur.execute("SELECT id, pseudo, MIN(score) FROM meilleurs_scores;")
        resultat = curseur.fetchone()
        curseur.close()
        connexion.close()
        return resultat


    def classement(self, position):
        classement = [0, 0, 0, 0, 0]
        connexion = sqlite3.connect("bdd/base_de_donnees.db")
        curseur = connexion.cursor()
        curseur.execute("SELECT id, pseudo, MAX(score) FROM meilleurs_scores;")
        classement[0] = curseur.fetchone()
        curseur.execute("SELECT id, pseudo, MAX(score) FROM meilleurs_scores WHERE id != ?;", (classement[0][0], ))
        classement[1] = curseur.fetchone()
        curseur.execute("SELECT id, pseudo, MAX(score) FROM meilleurs_scores WHERE id != ? AND id != ?;", (classement[0][0], classement[1][0], ))
        classement[2] = curseur.fetchone()
        curseur.execute("SELECT id, pseudo, MAX(score) FROM meilleurs_scores WHERE id != ? AND id != ? AND id != ?;", (classement[0][0], classement[1][0], classement[2][0], ))
        classement[3] = curseur.fetchone()
        curseur.execute("SELECT id, pseudo, MAX(score) FROM meilleurs_scores WHERE id != ? AND id != ? AND id != ? AND id != ?;", (classement[0][0], classement[1][0], classement[2][0], classement[3][0], ))
        classement[4] = curseur.fetchone()
        curseur.close()
        connexion.close()
        return classement[position - 1]


    def ajouter(self, pseudo, score):
        dernier = self.minimum()
        if score > dernier[2]:
            connexion = sqlite3.connect("bdd/base_de_donnees.db")
            curseur = connexion.cursor()
            curseur.execute("UPDATE meilleurs_scores SET pseudo = ?, score = ? WHERE id = ?;", (pseudo, score, dernier[0], ))
            connexion.commit()
            curseur.close()
            connexion.close()
