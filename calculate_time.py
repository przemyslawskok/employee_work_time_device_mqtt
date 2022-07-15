import time_configuration as CONFIGURE
import sqlite3
import datetime
from datetime import timedelta


def sort_tuples_by_time(tuples):
    tuples.sort(key=lambda x: x[0])
    return tuples

def sort_dict_by_date(dictionary):
    sorted_dictionary = {}
    for key in sorted(dictionary, key=lambda k: datetime.datetime.strptime(k, '%Y-%m-%d'), reverse=True):
        sorted_dictionary[key] = sort_tuples_by_time(dictionary[key])
    return sorted_dictionary



def check_ID_of_last_record(worker_id):
    try:
        
        today = datetime.date.today()
        two_days_ago = today - datetime.timedelta(days=2)
        two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")
        today_str = today.strftime("%Y-%m-%d")
        dictionary_of_dates = {}

        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND DATA BETWEEN '{}' AND '{}' ".format(worker_id,two_days_ago_str,today_str)
        db.execute(query)
        result=db.fetchall()
        con.close()
        for record in result:
            hour_str=str(str(record[2])+":"+str(record[3]))
            if record[1] in dictionary_of_dates:
                dictionary_of_dates[record[1]].append((hour_str,record[4],record[0]))
            else:
                dictionary_of_dates[record[1]]=[(hour_str,record[4],record[0])]
            
        for key in dictionary_of_dates:
            dictionary_of_dates[key]=sort_tuples_by_time(dictionary_of_dates[key])

        sorted_dictionary=sort_dict_by_date(dictionary_of_dates)

        id_of_last_record=""
        for key in sorted_dictionary:

            id_of_last_record=sorted_dictionary[key][-1][-1]
            break 
        if id_of_last_record:
            return id_of_last_record
        else:
            return "BRAK"
    except:
        print("Error in check_ID_of_last_record")
        return "BRAK"

def calculate_work_time(worker_id,GUI):
    try:
        """
        Calculate the work time for a worker.
        """
        #Get the start time
        last_id=check_ID_of_last_record(worker_id)
        if last_id=="BRAK":
            return "BRAK"
        else:
            con = sqlite3.connect('database.db')
            db = con.cursor()
            query = "SELECT GODZINA,MINUTA FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND ID = {}".format(worker_id,last_id)
            db.execute(query)
            result = db.fetchall()
            con.close()
            print(result)
            start_time_HOUR=result[0][0]
            start_time_MINUTE=result[0][1]
            start_time=timedelta(hours=start_time_HOUR,minutes=start_time_MINUTE)

            #Get the end time
            # end_time_HOUR = GUI.ACTUAL_HOUR_RECORD
            # end_time_MINUTE = GUI.ACTUAL_MINUTE_RECORD
            end_time_HOUR = 15
            end_time_MINUTE = 29
            end_time = timedelta(hours=end_time_HOUR,minutes=end_time_MINUTE)
        
            #Calculate the work time
            work_time = end_time - start_time
            amount_of_hours=work_time.seconds//3600
            amount_of_minutes=(work_time.seconds//60)%60
            print(amount_of_hours,amount_of_minutes)

            work_time_string=""

            if amount_of_hours>0:
                work_time_string=str(amount_of_hours)
            else:
                work_time_string="0"
            if amount_of_minutes>0:
                
                if amount_of_hours>0 and amount_of_minutes<=int(CONFIGURE.LOW_LIMIT): 
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

print(calculate_work_time(38,1))