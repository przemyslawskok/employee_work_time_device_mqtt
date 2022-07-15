import _thread
import backend_functions as bf

class backend():
    
    def __init__(self,pygame_object,GUI):
        self.PYGAME=pygame_object
        self.GUI=GUI
        self.SCREEN=GUI.SCREEN
        self.FUNCTIONS=bf
        self.TIME=bf.calculate_time(GUI)
        self.MQTT=bf.rfid_mqtt(self.PYGAME,self.GUI.RFID_APPLIED_ENTRY,GUI)

        #function to create tables in database if doesn't exist
        bf.create_tables()

        #Delays
        self.SYNCHRONIZE_CARDS_DELAY=100
        self.SYNCHRONIZE_USERS_DELAY=30
        self.SYNCHRONIZE_LOGS_DELAY=20

        _thread.start_new_thread(self.FUNCTIONS.check_connection_status,(GUI,))
        _thread.start_new_thread(self.FUNCTIONS.synchronize_rfid_owners,(self.SYNCHRONIZE_CARDS_DELAY,))
        _thread.start_new_thread(self.FUNCTIONS.synchronize_users,(self.SYNCHRONIZE_USERS_DELAY,))
        _thread.start_new_thread(self.FUNCTIONS.synchronize_logs,(self.SYNCHRONIZE_LOGS_DELAY,))
        _thread.start_new_thread(self.FUNCTIONS.check_rfid_connection_status,(GUI,))
        
        print("Backend app started")



        
        
        
    
    