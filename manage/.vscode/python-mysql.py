import mysql.connector
import sys

sql_create = """CREATE TABLE IF NOT EXISTS Produits (
                    ref int(6) NOT NULL, 
                    nom varchar(100) DEFAULT NULL, 
                    stock int(4) DEFAULT NULL,
                    prix float(5,2) DEFAULT NULL,
                    PRIMARY KEY(ref), 
                    CHECK (stock>=0)
               );
               """
try:
    conn = mysql.connector.connect(host="127.0.0.1",   user="root", password="@Ikhela-04KK-SIJ2023", database="magasin")
    cursor = conn.cursor()
    # cursor.execute(sql_create_1)
    cursor.execute(sql_create)
    conn.commit()


    try:
    # creation d'une table 

    # insertion des donnnées 
        reference = (554871 , "configure de fraise 250g", 10, 4.8)
        cursor.execute("""INSERT INTO Produits (ref , nom , stock , prix) VALUES(?, ? , ? , ?)""", reference)

        # insertion des données à partir du dictionnaire 
        # reference = {'ref': 543154, 'nom':"Gelée de coing 300g", 'stock':5, 'prix':3.75}

        # cursor.execute("""INSERT INTO Produits (ref , nom , stock, prix) VALUES(%(ref)d , "%(nom)s", %(stock)d, %(prix)f""", reference)
        conn.commit()
        
    except:
        conn.rollback()
    # acceder à dees données d'une base de donnée 

    


    

    
    

    # la gestion des erreurs est indispensables dans le cas de gestion des serveurs html

except mysql.connector.errors.InterfaceError as e:
        print("Error %d: %s" %(e.args[0], e.args[1]))
        sys.exit(1)
    
finally:
    cursor.execute("SELECT * FROM Produits")
    print(1)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        #On ferme la connexion
    if conn:
        conn.close()

