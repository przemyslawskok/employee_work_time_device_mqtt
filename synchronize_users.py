import mysql.connector
import dane
import time
import sqlite3
def synchronize_users(synchronize_users_delay):
    while True:
        try:
            print("Synchronizing users")
            mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
            kursor=mydb.cursor()
            query="SELECT `ID`,`PIN`,`NAZWA` FROM `uzytkownicy` WHERE `TYP`='pracownik' and `AKTYWNOSC`='1'"
            kursor.execute(query)
            result=kursor.fetchall()
            mydb.close()

            

            #creating a dictionary with the data from the database in form {'ID_PRACOWNIKA':['PIN','NAZWA']}
            dictionary_of_users={}
            for user in result:
                dictionary_of_users[user[0]]=[user[1],user[2]]
            

            
            con=sqlite3.connect('database.db')
            db=con.cursor()

            for key in dictionary_of_users:
                query="SELECT * FROM OWNERS WHERE ID_PRACOWNIKA='"+str(key)+"';"
                db.execute(query)
                result=db.fetchall()
            

                #if there is no entry in the database for this user, we need to create one
                if len(result)==0:
                    query="INSERT INTO OWNERS (ID_PRACOWNIKA,PIN,NAZWA) VALUES ('"+str(key)+"','"+str(dictionary_of_users[key][0])+"','"+str(dictionary_of_users[key][1])+"');"
                    db.execute(query)
                    con.commit()
                    print("New entry in the database for user with ID: "+str(key)+" and NAME: "+str(dictionary_of_users[key][1]))

                #checking if the PIN or name in the database is different from the one in the dictionary
                
                elif str(result[0][2])!=str(dictionary_of_users[key][0]) or str(result[0][3])!=str(dictionary_of_users[key][1]):
                    query="UPDATE OWNERS SET PIN='"+str(dictionary_of_users[key][0])+"',NAZWA='"+str(dictionary_of_users[key][1])+"' WHERE ID_PRACOWNIKA='"+str(key)+"';"
                    db.execute(query)
                    con.commit()
                    print("Updated entry in the database for user with ID: "+str(key)+" and NAME: "+str(dictionary_of_users[key][1]))
                    

            
            con.close()
            

        except:
            print("Error while synchronizing users, continuing...")
            
        print("Synchronizing users finished")
        time.sleep(synchronize_users_delay)


synchronize_users(5)