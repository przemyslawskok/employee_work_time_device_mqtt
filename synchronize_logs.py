import mysql.connector
import dane
import sqlite3
import time

def insert_rfid_log_localdb(date,hour,minute,record_type,worker_id):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_RFID (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
def insert_rfid_log_serverdb(date,hour,minute,record_type,worker_id):
    try:
        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="INSERT INTO `logi_rfid` (`DATA`,`GODZINA`,`MINUTA`,`TYP`,`ID_PRACOWNIKA`) VALUES (%s,%s,%s,%s,%s);"
        values=(date,hour,minute,record_type,worker_id)
        kursor.execute(query,values)
        mydb.commit()
        mydb.close()
        print("Log inserted into server database with values: "+str(values))
        return True
    except:
        print("Error: unable to insert RFID log into server database with values: "+str(values))
        return False
def update_rfid_log_localdb(id_log):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="UPDATE LOGI_RFID SET CZY_WYSLANO='TAK' WHERE ID="+str(id_log)+";"
    db.execute(query)
    con.commit()
    con.close()
    print("Log updated in local database with ID="+str(id_log))

def insert_pin_log_localdb(date,hour,minute,record_type,worker_id):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_PIN (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
def insert_pin_log_serverdb(date,hour,minute,record_type,worker_id):
    try:
        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="INSERT INTO `logi_pin` (`DATA`,`GODZINA`,`MINUTA`,`TYP`,`ID_PRACOWNIKA`) VALUES (%s,%s,%s,%s,%s);"
        values=(date,hour,minute,record_type,worker_id)
        kursor.execute(query,values)
        mydb.commit()
        mydb.close()
        print("Log inserted into server database with values: "+str(values))
        return True
    except:
        print("Error: unable to insert PIN log into server database with values: "+str(values))
        return False
def update_pin_log_localdb(id_log):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="UPDATE LOGI_PIN SET CZY_WYSLANO='TAK' WHERE ID="+str(id_log)+";"
    db.execute(query)
    con.commit()
    con.close()
    print("Log updated in local database with ID="+str(id_log))


def synchronize_logs(SYNCHRONIZE_LOGS_DELAY):
    while True:
        
        #Synchronize logs from local database to server database
        
        #check if there are new rfid logs in local database


        print("Synchronizing logs from local database to server database...")  
        #--RFID--
        con=sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_RFID WHERE CZY_WYSLANO='NIE';"
        db.execute(query)
        result=db.fetchall()
        con.commit()
        con.close()
        if len(result)==0:
            print("No new logs in local RFID LOGS table")
        else:
            print("New logs in local RFID LOGS table")
            
            for log in result:
                #insert log into server database
                if insert_rfid_log_serverdb(log[1],log[2],log[3],log[4],log[5]): 
                    #update log in local database
                    update_rfid_log_localdb(log[0])

        #--PIN--

        con=sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_PIN WHERE CZY_WYSLANO='NIE';"
        db.execute(query)
        result=db.fetchall()
        con.commit()
        con.close()
        if len(result)==0:
            print("No new logs in local PIN LOGS table")
        else:
            print("New logs in local PIN LOGS table")
            
            for log in result:
                #insert log into server database
                if insert_pin_log_serverdb(log[1],log[2],log[3],log[4],log[5]): 
                    #update log in local database
                    update_pin_log_localdb(log[0])


        time.sleep(SYNCHRONIZE_LOGS_DELAY)        
if __name__ == "__main__":
    synchronize_logs(2)