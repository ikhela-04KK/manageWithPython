# je vais mettre en place des modules pour permettre de manipulaer cette  base de donnée
# me concentrer sur cette base donnée 
import sqlite3
from email_slicer import mail_slicer
0
class Manages: 
    # dans ces cas si je voie l'utilisation de with conn , c'est 
    # mise en place de la base de donnée 
    connection = sqlite3.Connection("text.db")
    manage = connection.cursor()
     
    # toutes les tables dans une liste 
    list_table = ["apartment", "user_apartment_wishlist,worksite","floor_plan","restaurant", "plaza","grocery,park"]
    

    # ! la prochaine fois essaye de faire de telle sorte que dès qu'on rentre un mail il puisse utiliser l'email slicer 
    # ! comment sont nommées les variables dans les propriétés 
    #! est ce obligé de creer des variables dans le contructeur 
    #! pourquoi sauvagarder  les fichiers sql pour une entreprise : est ce pour les migrations ou est ce juste pour faire des requêtes 
    # def __init__(self):
    with manage:
        def email_slicer(self):
            emails=[]
            user=[]
            select_tab = self.manage.execute("select email_address from user")
            long_user = select_tab.fetchall()
            for i,der in enumerate(long_user, start = 1): # ! affiche une erreur lorqu'il n' y pas de fetchall() et que tu fais un len
                emails.append(der)
                user.append(mail_slicer(der[0])) # * der[0] pour capturer le mail et le faire dans le mail_slicer
            for j in range(len(long_user)):
                update_user=self.manage.execute("""UPDATE user SET user_names=:user_names WHERE email_address=:email_address""",
                {'email_address':emails[j][0].strip(),'user_names':user[j][0]})
                """
                j = pour retenir le tuple , mais le tuple il y'as une virgule et le mail
                j[0] = pour capturer l'email
                user = une liste de tuple de deux valeurs : le  user et le domaine 
                user[j] = pour couple de tuple 
                user[j][0] = pour le user uniquement
                user[j][1] = pour le domaine 
                """
                update_mail=self.manage.execute("""UPDATE user SET domaine=:domaine WHERE email_address=:email_address""",
                {'email_address':emails[j][0].strip(),'domaine':user[j][1]}
                                            )
                # conn.commit()
    with manage:
        def drop_table(self):
            for tables in self.list_table:
                self.manage.execute(f"DROP TABLE IF EXISTS {tables}")
        # creation des indexes pour faciliter l'utilisation de la table


