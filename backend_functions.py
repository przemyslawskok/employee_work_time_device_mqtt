import time

from datetime import datetime
from datetime import timedelta
import datetime as dt
import _thread
import requests
import sqlite3
import mysql.connector
import dane
import paho.mqtt.client as mqtt
import time_configuration as CONFIGURE


#--RFID + MQTT--
class rfid_mqtt():
    def __init__(self,pygame,rfid_event,GUI):
        self.PYGAME=pygame
        self.RFID_EVENT=rfid_event
        self.GUI=GUI
        time.sleep(dane.mqtt_start_delay)
        self.done=0
        while self.done==0:
            try:
                self.client = mqtt.Client()
                self.client.on_connect = self.on_connect
                self.client.on_message = self.on_message
                self.client.connect(dane.broker_address, int(dane.broker_port), 60)
                self.client.subscribe(dane.broker_topic_main,2)
                self.done=1
            except:
                continue
        
        _thread.start_new_thread(self.reconnect_subscribe,())
        _thread.start_new_thread(self.reconnect_mqtt,())
        _thread.start_new_thread(self.client.loop_start,())
    def reconnect_subscribe(self):
        while True:
            time.sleep(dane.mqtt_subscribe_delay)
            try:
                self.client.subscribe(dane.broker_topic_main,2)
                print("MQTT subscribed")
            except:
                print("MQTT reconnect subscribe error") 
                continue
    def on_message(self, client, userdata, msg):
        if msg.topic == dane.broker_topic:
            self.PYGAME.event.post(self.PYGAME.event.Event(self.RFID_EVENT,id=str(msg.payload.decode("utf-8"))))
            print("MQTT message received")
            print("RFID APPLIED: "+msg.payload.decode("utf-8"))
        elif msg.topic == str(dane.broker_topic_active):
            print("MQTT message active received")
            self.GUI.RFID_CONNECTION_STATUS_DELAY=20
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
    def reconnect_mqtt(self):
        while True:
            time.sleep(dane.mqtt_reconnect_delay)
            try:
                print("MQTT reconnect started")
                
                _thread.start_new_thread(self.client.loop_stop,())
                
                self.client = mqtt.Client()
                self.client.on_connect = self.on_connect
                self.client.on_message = self.on_message
                self.client.connect(dane.broker_address, int(dane.broker_port), 60)

                
                _thread.start_new_thread(self.client.loop_start,())
                print("MQTT reconnected")
            except:
                print("MQTT reconnect error")
                continue



#--LOCAL DATABASE--

def create_tables():
    
    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE LOGI_ALL (
                ID INTEGER PRIMARY KEY,
                DATA DATE(255) NOT NULL,
                GODZINA INT(255) NOT NULL, 
                MINUTA INT(255) NOT NULL, 
                TYP TEXT(255) NOT NULL,
                ID_PRACOWNIKA INT(255) NOT NULL,
                CZY_WYSLANO TEXT(255) NOT NULL
            );"""

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'LOGI_ALL' created!")
    except:
        print("Table 'LOGI_ALL' exists!")
    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE LOGI_RFID (
                ID INTEGER PRIMARY KEY,
                DATA DATE(255) NOT NULL,
                GODZINA INT(255) NOT NULL, 
                MINUTA INT(255) NOT NULL, 
                TYP TEXT(255) NOT NULL,
                ID_PRACOWNIKA INT(255) NOT NULL,
                CZY_WYSLANO TEXT(255) NOT NULL
            );"""

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'LOGI_RFID' created!")
    except:
        print("Table 'LOGI_RFID' exists!")


    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE LOGI_PIN (
                ID INTEGER PRIMARY KEY,
                DATA DATE(255) NOT NULL,
                GODZINA INT(255) NOT NULL, 
                MINUTA INT(255) NOT NULL, 
                TYP TEXT(255) NOT NULL,
                ID_PRACOWNIKA INT(255) NOT NULL,
                CZY_WYSLANO TEXT(255) NOT NULL
            );"""

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'LOGI_PIN' created!")
    except:
        print("Table 'LOGI_PIN' exists!")

    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE LOGI_MESSAGES (
                ID INTEGER PRIMARY KEY,
                DATA DATE(255) NOT NULL,
                GODZINA INT(255) NOT NULL, 
                MINUTA INT(255) NOT NULL, 
                TYP TEXT(255) NOT NULL,
                ID_PRACOWNIKA INT(255) NOT NULL,
                CZYM_ZALOGOWANO TEXT(255) NOT NULL,
                CZY_WYSLANO TEXT(255) NOT NULL
            );"""

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'LOGI_MESSAGES' created!")
    except:
        print("Table 'LOGI_MESSAGES' exists!")

    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE RFID_OWNERS (
                ID INTEGER PRIMARY KEY,
                RFID INT(255) NOT NULL,
                ID_PRACOWNIKA INT(255) 
            ); """

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'RFID_OWNERS' created!")
    except:
        print("Table 'RFID_OWNERS' exists!")

    try:
        con=sqlite3.connect('database.db')
        db=con.cursor()
        zapytanie=""" CREATE TABLE OWNERS (
                ID INTEGER PRIMARY KEY,
                ID_PRACOWNIKA INT(255) NOT NULL,
                PIN TEXT(255) NOT NULL,
                NAZWA TEXT(255) NOT NULL
            ); """

        db.execute(zapytanie)
        con.commit()
        con.close()
        print("Table 'OWNERS' created!")
    except:
        print("Table 'OWNERS' exists!")

def insert_rfid_owner_localdb(rfid,id_pracownika):
    try:
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
        return True
    except:
        return False
def insert_rfid_log_localdb(date,hour,minute,record_type,worker_id):
    minute='{:02}'.format(int(minute))
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_ALL (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local LOGI_ALL table")
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_RFID (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local RFID table")
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_MESSAGES (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZYM_ZALOGOWANO,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','RFID','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local MESSAGES table")

def update_rfid_log_localdb(id_log):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="UPDATE LOGI_RFID SET CZY_WYSLANO='TAK' WHERE ID="+str(id_log)+";"
    db.execute(query)
    con.commit()
    con.close()
    print("Log updated in local database with ID="+str(id_log))
def insert_pin_log_localdb(date,hour,minute,record_type,worker_id):
    minute='{:02}'.format(int(minute))
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_ALL (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local LOGI_ALL table")
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_PIN (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local PIN table")
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="INSERT INTO LOGI_MESSAGES (DATA,GODZINA,MINUTA,TYP,ID_PRACOWNIKA,CZYM_ZALOGOWANO,CZY_WYSLANO) VALUES ('"+date+"','"+hour+"','"+minute+"','"+record_type+"','"+worker_id+"','PIN','NIE');"
    db.execute(query)
    con.commit()
    con.close()
    print("Log inserted in local MESSAGES table")
def update_pin_log_localdb(id_log):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="UPDATE LOGI_PIN SET CZY_WYSLANO='TAK' WHERE ID="+str(id_log)+";"
    db.execute(query)
    con.commit()
    con.close()
    print("Log updated in local database with ID="+str(id_log))
def update_all_log_localdb(id_log):
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="UPDATE LOGI_ALL SET CZY_WYSLANO='TAK' WHERE ID="+str(id_log)+";"
    db.execute(query)
    con.commit()
    con.close()
    print("Log updated in local database with ID="+str(id_log))
def check_pin(pin):
    #function to check if PIN is correct
    #if yes return id_worker
    #if no return false
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="SELECT ID_PRACOWNIKA FROM OWNERS WHERE PIN='"+str(pin)+"';"
    db.execute(query)
    result=db.fetchall()
    con.close()
    if len(result)>0:
        return result[0][0]
    else:
        return False
def check_name(worker_id):
    #function to get name of worker from database
    #if yes return name
    #if no return false
    con=sqlite3.connect('database.db')
    db=con.cursor()
    query="SELECT NAZWA FROM OWNERS WHERE ID_PRACOWNIKA='"+str(worker_id)+"';"
    db.execute(query)
    result=db.fetchall()
    con.close()
    if len(result)>0:
        return result[0][0]
    else:
        return False
def user_login(pin):

    #function to check if PIN is correct
    #if yes return list [id_worker,name]
    #if no return false
    worker_id=check_pin(pin)
    if worker_id:
        return [worker_id,check_name(worker_id)]
    else:
        return False
def check_type_of_last_record(worker_id):
      
    today = datetime.now()
    two_days_ago = today - timedelta(days=2)
    two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")
    today_str = today.strftime("%Y-%m-%d")
    try:
        
        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND DATA BETWEEN '{}' AND '{}' ORDER BY ID DESC LIMIT 1".format(worker_id,two_days_ago_str,today_str)
        db.execute(query)
        result=db.fetchall()
        print(result)
        con.close()
        if len(result)>0:
            return str(result[0][4])
        else:
            return "WYJSCIE"

    except: 
        return "WYJSCIE"

def check_ID_of_last_record(worker_id):
    #function to get ID of last record from database
    #if yes return id
    #if no return false
        
    today = datetime.now()
    two_days_ago = today - timedelta(days=2)
    two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")
    today_str = today.strftime("%Y-%m-%d")
    try:
        
        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT ID FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND DATA BETWEEN '{}' AND '{}' ORDER BY ID DESC LIMIT 1".format(worker_id,two_days_ago_str,today_str)
        db.execute(query)
        result=db.fetchall()
        con.close()
        if len(result)>0:
            return str(result[0][0])
        else:
            return "BRAK"

    except: 
        return "BRAK"

def check_rfid_owner(rfid):
    #Function to check RFID owner
    #Return ID of worker if RFID is found
    #Return false if RFID is not found
    try:
        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM RFID_OWNERS WHERE RFID='{}' ".format(rfid)
        db.execute(query)
        result=db.fetchall()
        con.close()

        if len(result)==0:
            return False
        else:
            return (result[0][2])
    except:
        return False
   


        



#--SERVER DATABASE--

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
        print("Error while inserting RFID owner into server database")
        return False
def insert_rfid_log_serverdb(date,hour,minute,record_type,worker_id):
    try:
        minute='{:02}'.format(int(minute))
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
def insert_pin_log_serverdb(date,hour,minute,record_type,worker_id):
    try:
        minute='{:02}'.format(int(minute))
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
def insert_all_log_serverdb(date,hour,minute,record_type,worker_id):
    try:
        minute='{:02}'.format(int(minute))
        mydb = mysql.connector.connect(user=dane.uzytkownik_baza, password=dane.haslo_baza,
                                        host=dane.ip_baza,
                                        port=dane.port_baza,
                                        database=dane.nazwa_baza)
        kursor=mydb.cursor()
        query="INSERT INTO `logi_all` (`DATA`,`GODZINA`,`MINUTA`,`TYP`,`ID_PRACOWNIKA`) VALUES (%s,%s,%s,%s,%s);"
        values=(date,hour,minute,record_type,worker_id)
        kursor.execute(query,values)
        mydb.commit()
        mydb.close()
        print("Log inserted into server database with values: "+str(values))
        return True
    except:
        print("Error: unable to insert ALL log into server database with values: "+str(values))
        return False



#--THREADS TO SYNCHRONIZE DATA--

def synchronize_rfid_owners(SYNCHRONIZE_CARDS_DELAY):
    while True:
        try:
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
        except:
            print("Error while synchronizing RFID owners")

        print("Synchronizing RFID owners finished")
        time.sleep(SYNCHRONIZE_CARDS_DELAY)
def synchronize_users(SYNCHRONIZE_USERS_DELAY):
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
                dictionary_of_users[str(user[0])]=[str(user[1]),str(user[2])]
            

            
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
        time.sleep(SYNCHRONIZE_USERS_DELAY)
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

        #--ALL--
        con=sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_ALL WHERE CZY_WYSLANO='NIE';"
        db.execute(query)
        result=db.fetchall()    
        con.commit()
        con.close()
        if len(result)==0:
            print("No new logs in local ALL LOGS table")
        else:
            print("New logs in local A;; LOGS table")
            
            for log in result:
                #insert log into server database
                if insert_all_log_serverdb(log[1],log[2],log[3],log[4],log[5]): 
                    #update log in local database
                    update_all_log_localdb(log[0])


        time.sleep(SYNCHRONIZE_LOGS_DELAY)



#--OTHER--

class calculate_time():
    year=0
    month=0
    day=0
    hour=0
    minute=0
    def __init__(self,gui):
        self.GUI=gui
        _thread.start_new_thread(self.calculate_time,())
    def calculate_time(self):
        print("Checking time thread started")
        while True:
            actual_time=datetime.now()
            self.year=actual_time.year
            self.month='{:02}'.format(actual_time.month)
            self.day='{:02}'.format(actual_time.day)
            self.hour=actual_time.hour
            self.minute='{:02}'.format(actual_time.minute)
            self.update_time()
            time.sleep(1)
    def update_time(self):
        self.GUI.ACTUAL_HOUR=str(self.hour)+":"+str(self.minute)
        self.GUI.ACTUAL_DATE=str(str(self.year)+"-"+str(self.month)+"-"+str(self.day))
        self.GUI.ACTUAL_DATE_NAME=self.which_day(self.GUI.ACTUAL_DATE)
        self.GUI.ACTUAL_HOUR_RECORD=str(self.hour)
        self.GUI.ACTUAL_MINUTE_RECORD=str(self.minute)
        
        
    def which_day(self,date):
        #Checking name of day
        day_obj=datetime.strptime(str(date),'%Y-%m-%d')
        day_id=day_obj.strftime('%w')
        day_name=""
        if day_id=="1":
            day_name="Poniedziałek"
        elif day_id=="2":
            day_name="Wtorek"
        elif day_id=="3":
            day_name="Środa"
        elif day_id=="4":
            day_name="Czwartek"
        elif day_id=="5":
            day_name="Piątek"
        elif day_id=="6":
            day_name="Sobota"
        elif day_id=="0":
            day_name="Niedziela"
        
        return day_name  
def check_connection_status(GUI):
    print("Checking connection status thread started")
    while True:
        time.sleep(10)
        url = "http://www.google.com"
        timeout = 1
        try:
            request = requests.get(url, timeout=timeout)
            GUI.CONNECTION_STATUS="Online"
        except (requests.ConnectionError, requests.Timeout) as exception:
            GUI.CONNECTION_STATUS="Offline"
def check_rfid_connection_status(GUI):
    print("Checking RFID connection status thread started")
    while True:
        time.sleep(1)
        GUI.RFID_CONNECTION_STATUS_DELAY-=1
        if GUI.RFID_CONNECTION_STATUS_DELAY<=0:
            GUI.RFID_CONNECTION_STATUS="Rozłączono"
        else:
            GUI.RFID_CONNECTION_STATUS="Połączono"




def sort_tuples_by_time(tuples):
    tuples.sort(key=lambda x: x[0])
    return tuples
def sort_dict_by_date(dictionary):

    sorted_dictionary = {}
    for key in sorted(dictionary, key=lambda k: datetime.strptime(k, '%Y-%m-%d'), reverse=True):
        sorted_dictionary[key] = sort_tuples_by_time(dictionary[key])
    return sorted_dictionary
def calculate_work_time(worker_id,GUI):
    try:
        """
        Calculate the work time for a worker.
        """
        #Get the start time
        last_id=check_ID_of_last_record(worker_id)
        print(last_id)
        if last_id=="BRAK":
            return "BRAK"
        else:
            con = sqlite3.connect('database.db')
            db = con.cursor()
            query = "SELECT GODZINA,MINUTA FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND ID = {}".format(worker_id,last_id)
            db.execute(query)
            result = db.fetchall()
            
            con.close()
            start_time_HOUR=result[0][0]
            start_time_MINUTE=result[0][1]
            start_time=timedelta(hours=start_time_HOUR,minutes=start_time_MINUTE)

            #Get the end time
            end_time_HOUR = int(GUI.ACTUAL_HOUR_RECORD)
            end_time_MINUTE = int(GUI.ACTUAL_MINUTE_RECORD)
            end_time = timedelta(hours=end_time_HOUR,minutes=end_time_MINUTE)
        
            #Calculate the work time
            work_time = end_time - start_time
            amount_of_hours=work_time.seconds//3600
            amount_of_minutes=(work_time.seconds//60)%60

            work_time_string=""

            if amount_of_hours>0:
                work_time_string=str(amount_of_hours)
            else:
                work_time_string="0"
            if amount_of_minutes>0:
                
                if amount_of_minutes>=0 and amount_of_minutes<=int(CONFIGURE.LOW_LIMIT): 
                    work_time_string=work_time_string+",0h"
                elif amount_of_minutes>=int(CONFIGURE.LOW_LIMIT) and amount_of_minutes<=int(CONFIGURE.HIGH_LIMIT):
                    work_time_string=work_time_string+",5h"
                else:
                    work_time_string=str(amount_of_hours+1)+"h"

            else:
                work_time_string=work_time_string+",0h"
            return work_time_string
    except:
        print("Error in calculate_work_time")
        return False


      
            

