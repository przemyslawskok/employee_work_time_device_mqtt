import sqlite3
import datetime
def check_ID_of_last_record(worker_id):
    try:
        
        today = datetime.date.today()
        two_days_ago = today - datetime.timedelta(days=2)
        two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")
        today_str = today.strftime("%Y-%m-%d")
        print(today_str,two_days_ago_str)

        dictionary_of_dates = {}

        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND DATA BETWEEN '{}' AND '{}' ".format(worker_id,two_days_ago_str,today_str)
        db.execute(query)
        result=db.fetchall()
        print(result)
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

def check_type_of_last_record(worker_id):
    try:
        
        today = datetime.date.today()
        two_days_ago = today - datetime.timedelta(days=2)
        two_days_ago_str = two_days_ago.strftime("%Y-%m-%d")
        today_str = today.strftime("%Y-%m-%d")
        print(today_str,two_days_ago_str)

        dictionary_of_dates = {}

        con = sqlite3.connect('database.db')
        db=con.cursor()
        query="SELECT * FROM LOGI_ALL WHERE ID_PRACOWNIKA = {} AND DATA BETWEEN '{}' AND '{}' ".format(worker_id,two_days_ago_str,today_str)
        db.execute(query)
        result=db.fetchall()
        print(result)
        con.close()
        for record in result:
            hour_str=str(str(record[2])+":"+str(record[3]))
            if record[1] in dictionary_of_dates:
                dictionary_of_dates[record[1]].append((hour_str,record[4]))
            else:
                dictionary_of_dates[record[1]]=[(hour_str,record[4])]
            
        for key in dictionary_of_dates:
            dictionary_of_dates[key]=sort_tuples_by_time(dictionary_of_dates[key])

        sorted_dictionary=sort_dict_by_date(dictionary_of_dates)

        id_of_last_record=""
        for key in sorted_dictionary:
            print(key)
            print(sorted_dictionary[key][-1])
            last_type_of_record=sorted_dictionary[key][-1][-1]
            break 
        if last_type_of_record:
            return last_type_of_record
        else:
            return "BRAK"
    except:
        print("Error in check_type_of_last_record")
        return "BRAK"

def sort_tuples_by_time(tuples):
    tuples.sort(key=lambda x: x[0])
    return tuples

def sort_dict_by_date(dictionary):
    sorted_dictionary = {}
    for key in sorted(dictionary, key=lambda k: datetime.datetime.strptime(k, '%Y-%m-%d'), reverse=True):
        sorted_dictionary[key] = sort_tuples_by_time(dictionary[key])
    return sorted_dictionary




print(check_ID_of_last_record(10))
print(check_ID_of_last_record(38))
print(check_type_of_last_record(30))

