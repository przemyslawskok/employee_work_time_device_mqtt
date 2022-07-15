import time

def CHECK_BUTTONS_MAIN_AFTER_BUTTON(x,y):
    #Function to check which button is clicked, return the value of button
    #SPECIAL BUTTONS:
    # Submit = return "SUBMIT"
    # Backspace = return "BACKSPACE"
    # Keyboard = return "HIDE_KEYBOARD"
    

    if x>0.04 and x<0.1 and y>0.26 and y<0.38:
        return "1"
    elif x>0.16 and x<0.24 and y>0.26 and y<0.38:
        return "2"
    elif x>0.3 and x<0.37 and y>0.26 and y<0.38:
        return "3"
    elif x>0.43 and x<0.50 and y>0.26 and y<0.38:
        return "BACKSPACE"
    elif x>0.56 and x<0.63 and y>0.26 and y<0.38:
        return "SUBMIT"
    elif x>0.04 and x<0.1 and y>0.43 and y<0.53:
        return "4"
    elif x>0.16 and x<0.24 and y>0.43 and y<0.53:
        return "5"
    elif x>0.3 and x<0.37 and y>0.43 and y<0.53:
        return "6"
    elif x>0.04 and x<0.1 and y>0.57 and y<0.66:
        return "7"
    elif x>0.16 and x<0.24 and y>0.57 and y<0.66:    
        return "8"
    elif x>0.3 and x<0.37 and y>0.57 and y<0.66:
        return "9"
    elif x>0.04 and x<0.1 and y>0.71 and y<0.84:
        return "#"
    elif x>0.16 and x<0.24 and y>0.71 and y<0.84:  
        return "0"
    elif x>0.3 and x<0.37 and y>0.71 and y<0.84:
        return "*"
    elif x>0.01 and x<0.1 and y>0.88 and y<0.95:
        return "HIDE_KEYBOARD"
    else:
        return "EMPTY_SPACE"

def CHECK_BUTTONS_MAIN_BEFORE_BUTTON(x,y):
    #Function to check which button is clicked, return the value of button
    #SPECIAL BUTTONS:
    # Keyboard = return "HIDE_KEYBOARD"

    if x>0.01 and x<0.1 and y>0.88 and y<0.95:
        return "SHOW_KEYBOARD"
    else:
        return "EMPTY_SPACE"


def CHECK_BUTTONS_ADMIN_PANEL(x,y):
    #Function to check which button is clicked, return the value of button
    #SPECIAL BUTTONS:
    # Submit = return "SUBMIT"
    # Backspace = return "BACKSPACE"
    # Logout = return "LOGOUT"

    if x>0.04 and x<0.1 and y>0.26 and y<0.38:
        return "1"
    elif x>0.16 and x<0.24 and y>0.26 and y<0.38:
        return "2"
    elif x>0.3 and x<0.37 and y>0.26 and y<0.38:
        return "3"
    elif x>0.43 and x<0.50 and y>0.26 and y<0.38:
        return "BACKSPACE"
    elif x>0.56 and x<0.63 and y>0.26 and y<0.38:
        return "SUBMIT"
    elif x>0.04 and x<0.1 and y>0.43 and y<0.53:
        return "4"
    elif x>0.16 and x<0.24 and y>0.43 and y<0.53:
        return "5"
    elif x>0.3 and x<0.37 and y>0.43 and y<0.53:
        return "6"
    elif x>0.04 and x<0.1 and y>0.57 and y<0.66:
        return "7"
    elif x>0.16 and x<0.24 and y>0.57 and y<0.66:    
        return "8"
    elif x>0.3 and x<0.37 and y>0.57 and y<0.66:
        return "9"
    elif x>0.04 and x<0.1 and y>0.71 and y<0.84:
        return "#"
    elif x>0.16 and x<0.24 and y>0.71 and y<0.84:  
        return "0"
    elif x>0.3 and x<0.37 and y>0.71 and y<0.84:
        return "*"
    elif x>0.01 and x<0.2 and y>0.88 and y<0.95:
        return "LOGOUT"
    else:
        return "EMPTY_SPACE"


def CHECK_BUTTONS_ADMIN_PAIRING(x,y):
    #Function to check which button is clicked, return the value of button
    #SPECIAL BUTTONS:
    # Keyboard = return "HIDE_KEYBOARD"

    if x>0.01 and x<0.15 and y>0.10 and y<0.23:
        return "BACK"
    else:
        return "EMPTY_SPACE"


def CONTROL_PIN(PYGAME,GUI,typed_character):
    if typed_character=="EMPTY_SPACE":
        return False
    elif typed_character=="BACKSPACE":
        GUI.TYPED_PIN=GUI.TYPED_PIN[:-1]
    elif typed_character=="SUBMIT":
        PYGAME.event.post(PYGAME.event.Event(GUI.CLICKED_SUBMIT_BUTTON))
    elif typed_character=="SHOW_KEYBOARD":
        PYGAME.event.post(PYGAME.event.Event(GUI.CLICKED_SHOW_KEYBOARD_BUTTON))
    elif typed_character=="HIDE_KEYBOARD":
        PYGAME.event.post(PYGAME.event.Event(GUI.CLICKED_HIDE_KEYBOARD_BUTTON))
    elif typed_character=="LOGOUT":
        PYGAME.event.post(PYGAME.event.Event(GUI.CLICKED_LOGOUT_BUTTON))
    elif typed_character=="BACK":
        PYGAME.event.post(PYGAME.event.Event(GUI.CLICKED_BACK_BUTTON))
    else:

        if len(GUI.TYPED_PIN)>8:
            return False
        else:
            GUI.TYPED_PIN+=typed_character
            print(GUI.TYPED_PIN)

def CHANGE_SCREEN(WINDOW_STRING,PYGAME,GUI,DELAY=0):
    
    if WINDOW_STRING=="WINDOW_MAIN_MENU_BEFORE_BUTTON":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=True

        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''

    elif WINDOW_STRING=="WINDOW_MAIN_MENU_AFTER_BUTTON":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False

        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=True
        
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_ADMIN_PANEL":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False

        GUI.WINDOW_ADMIN_PANEL=True

        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False
        
        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_PIN_ERROR":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False

        GUI.WINDOW_PIN_ERROR=True

        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_ADMIN_PIN_ERROR":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False

        GUI.WINDOW_ADMIN_PIN_ERROR=True

        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_ADMIN_PAIRING":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        
        GUI.WINDOW_ADMIN_PAIRING=True
        
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_RFID_ENTRY":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False

        GUI.WINDOW_RFID_ENTRY=True

        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_RFID_EXIT":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False

        GUI.WINDOW_RFID_EXIT=True

        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''
    elif WINDOW_STRING=="WINDOW_RFID_ERROR":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False

        GUI.WINDOW_RFID_ERROR=True

        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False
        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''

    elif WINDOW_STRING=="WINDOW_ADMIN_PAIRING_OK":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False

        GUI.WINDOW_ADMIN_PAIRING_OK=True

        GUI.WINDOW_ADMIN_PAIRING_ERROR=False

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''

    elif WINDOW_STRING=="WINDOW_ADMIN_PAIRING_ERROR":
        time.sleep(DELAY)

        GUI.WINDOW_MAIN_MENU_BEFORE_BUTTON=False
        GUI.WINDOW_MAIN_MENU_AFTER_BUTTON=False
        GUI.WINDOW_RFID_ENTRY=False
        GUI.WINDOW_RFID_EXIT=False
        GUI.WINDOW_RFID_ERROR=False
        GUI.WINDOW_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PANEL=False
        GUI.WINDOW_ADMIN_PIN_ERROR=False
        GUI.WINDOW_ADMIN_PAIRING=False
        GUI.WINDOW_ADMIN_PAIRING_OK=False

        GUI.WINDOW_ADMIN_PAIRING_ERROR=True

        GUI.ACTUAL_ID=''
        GUI.TYPED_PIN=''