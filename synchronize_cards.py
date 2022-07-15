import mysql.connector
import dane
import time
import sqlite3

def insert_rfid_owner_localdb(rfid,id_pracownika):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="DELETE FROM RFID_OWNERS WHERE RFID='"+str(rfid)+"';"
    db.execute(query)
    con.commit()
    query="INSERT INTO RFID_OWNERS (RFID,ID_PRACOWNIKA) VALUES ('"+str(rfid)+"','"+str(id_pracownika)+"');"
    db.execute(query)
    con.commit()
    con.close()
    print("RFID owner inserted")

def insert_rfid_owner_serverdb(rfid,id_pracownika):
    try:
    #delete previous records from database with this id

        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="DELETE FROM `rfid_uzytkownicy` WHERE `RFID`='"+str(rfid)+"';"
        kursor.execute(query)
        mydb.commit()
        mydb.close()
        print("RFID owner deleted from server database with RFID: "+str(rfid))


        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="INSERT INTO `rfid_uzytkownicy` (`RFID`,`ID_PRACOWNIKA`) VALUES ('"+str(rfid)+"','"+str(id_pracownika)+"');"
        kursor.execute(query)
        mydb.commit()
        mydb.close()
        print("RFID owner inserted into server database with RFID: "+str(rfid))
        return True
    except:
        mydb.close()
        return False
  
def synchronize_rfid_owners(synchronize_rfid_owners_delay):
    while True:
        
        print("Synchronizing RFID owners")


        #getting all the RFID owners from the local database
        con=sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT RFID,ID_PRACOWNIKA FROM RFID_OWNERS;"
        db.execute(query)
        result=db.fetchall()
        con.close()

        #creating a dictionary with the data from the database
        #example output {'12312312321':20}
        local_dictionary_of_rfid_owners={}
        for rfid in result:
            local_dictionary_of_rfid_owners[str(rfid[0])]=str(rfid[1])
        
        
        #check if the RFID owner pair is in the server database
        
        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="SELECT `RFID`,`ID_PRACOWNIKA` FROM `rfid_uzytkownicy`;"
        kursor.execute(query)
        result=kursor.fetchall()
        mydb.close()

        #creating a dictionary with the data from the database
        #example output {'12312312321':20}
        dictionary_of_rfid_owners={}
        for rfid in result:
            dictionary_of_rfid_owners[str(rfid[0])]=str(rfid[1])
        

        for key in local_dictionary_of_rfid_owners:
            if key not in dictionary_of_rfid_owners:
                print("RFID owner not in server database, inserting...")
                insert_rfid_owner_serverdb(key,local_dictionary_of_rfid_owners[key])
            elif local_dictionary_of_rfid_owners[key]!=dictionary_of_rfid_owners[key]:
                print("RFID owner in server database, but with different ID_PRACOWNIKA, updating...")
                insert_rfid_owner_serverdb(key,local_dictionary_of_rfid_owners[key])





        print("Synchronizing RFID owners finished")
        time.sleep(synchronize_rfid_owners_delay)


#synchronize_rfid_owners(3)


