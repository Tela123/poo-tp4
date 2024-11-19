import sqlite3 #1 j'importe
print(sqlite3.sqlite_version)
connexion=sqlite3.connect("ma_db.db")#2 je connecte
# print("Base de donnees cree")
curseur=connexion.cursor()
curseur.execute('''
                create table if not exists utilisateur(
                    id integer Primary key autoincrement,
                    nom text not null,
                    age integer not null,
                    email text not null unique
                )
                ''')
print("table cree avec succes")
nom="tela"
age=19
email="telanita@gmail.com"
curseur.execute('''
                INSERT INTO utilisateur(nom, age, email)
                VALUES(?,?,?)
                ''',(nom, age,email))
# curseur.execute('''
#                 INSERT INTO utilisateur(nom, age, email)
#                 VALUES('tela',19,'hgijk@bvn')
#                 ''')
print("Donnees enregistrees avec succes utilisateur")

curseur.execute('''
                UPDATE utilisateur
                SET email='telane@jhh.ss'
                WHERE id=1
                ''')
print("Donnees mises a jour avec succes utilisateur")

curseur.execute('SELECT * FROM utilisateur')
resultats=curseur.fetchall()
print(resultats)

for ligne in resultats:
    print(type(ligne))
    print(ligne)

    
connexion.commit()
connexion.close()#3 je ferme