import sqlite3















# def check_rfid_owner(rfid):
#     #Function to check RFID owner
#     #Return ID of worker if RFID is found
#     #Return false if RFID is not found
#     try:
#         con = sqlite3.connect('database.db')
#         db=con.cursor()
#         query="SELECT * FROM RFID_OWNERS WHERE RFID='{}' ".format(rfid)
#         db.execute(query)
#         result=db.fetchall()
#         con.close()

#         if len(result)==0:
#             return False
#         else:
#             return (result[0][2])
#     except:
#         return False
   



# print(check_rfid_owner(rfid='465749620732'))