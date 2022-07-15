import pygame
import pygame_gui
import gui_elements as elements
import gui_functions as functions
import backend_functions
import backend_app as backend
import _thread
import time
import winsound



class gui():

    def __init__(self):

        winsound.Beep(500,2000)
        pygame.init()   

        #Variables to store local information
        self.ACTUAL_DATE='2022-08-06'
        self.ACTUAL_DATE_NAME='Środa'
        self.ACTUAL_HOUR="12:30"
        self.CONNECTION_TITLE="Stan poł. z internetem:"
        self.CONNECTION_STATUS="Online"
        self.RFID_CONNECTION_TITLE="Stan czytnika:"
        self.RFID_CONNECTION_STATUS="Rozłączono"
        self.RECORD_TYPE_ENTRY="Wejście"
        self.RECORD_TYPE_EXIT="Wyjście"
        self.TYPED_PIN=""
        self.ACTUAL_ID=""
        self.MAIN_MENU_TITLE="Przyłóż identyfikator"
        self.PIN_ERROR_MESSAGE="Logowanie nieudane"
        self.ADMIN_PANEL_TITLE="Tryb administratora"
        self.ADMIN_PANEL_MESSAGE_1="Wprowadź PIN użytkownika"
        self.ADMIN_PANEL_MESSAGE_2="w celu sparowania identyfikatora."
        self.ADMIN_PANEL_PIN_ERROR_MESSAGE_1="Nie znaleziono użytkownika"
        self.ADMIN_PANEL_PIN_ERROR_MESSAGE_2="przypisanego do tego PINU."
        self.ADMIN_PANEL_PAIRING_TITLE="Tryb parowania dla użytkownika:"
        self.ADMIN_PANEL_PAIRING_USER="Laskowska Katarzyna"
        self.ADMIN_PANEL_PAIRING_MESSAGE_1="Przyłóż nowy identyfikator"
        self.ADMIN_PANEL_PAIRING_OK_TITLE="Zapisano identyfikator!"
        self.ADMIN_PANEL_PAIRING_ERROR_TITLE="Wystąpił błąd."
        self.RFID_ERROR_TITLE="Nie znaleziono użytkownika."
        self.RFID_USER_NAME="Laskowska Katarzyna"
        self.RFID_ENTRY_TITLE="Witaj"
        self.RFID_EXIT_TITLE="Żegnaj"
        self.RFID_EXIT_TIME_TITLE="Łączny czas:"
        self.RFID_EXIT_TIME="Błąd"
        
        

        #BACKEND VARIABLES
        self.ACTUAL_HOUR_RECORD=''
        self.ACTUAL_MINUTE_RECORD=''
         
        self.SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        #self.SCREEN = pygame.display.set_mode((1200,800))
    
        self.BACKGROUND_COLOR="#454443"
        self.BACKGROUND_MAIN=pygame.Surface((self.SCREEN.get_size()))
        #self.BACKGROUND_MAIN=pygame.Surface((800,600))
        


        #GUI library items
        self.MANAGER_GUI = pygame_gui.UIManager((self.SCREEN.get_size()))
        self.CLOCK_GUI=pygame.time.Clock()

        self.IMAGE_BUTTON_ONE=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_one.png')
        self.IMAGE_BUTTON_TWO=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_two.png')
        self.IMAGE_BUTTON_THREE=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_three.png')
        self.IMAGE_BUTTON_BACKSPACE=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_backspace.png')
        self.IMAGE_BUTTON_SUBMIT=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_submit.png')
        self.IMAGE_BUTTON_FOUR=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_four.png')
        self.IMAGE_BUTTON_FIVE=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_five.png')
        self.IMAGE_BUTTON_SIX=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_six.png')
        self.IMAGE_BUTTON_SEVEN=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_seven.png')
        self.IMAGE_BUTTON_EIGHT=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_eight.png')
        self.IMAGE_BUTTON_NINE=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_nine.png')
        self.IMAGE_BUTTON_HASHTAG=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_hashtag.png')
        self.IMAGE_BUTTON_ZERO=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_zero.png')
        self.IMAGE_BUTTON_STAR=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_star.png')
        self.IMAGE_BUTTON_KEYBOARD=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_keyboard.png')
        self.IMAGE_BUTTON_LOGOUT=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_logout.png')
        self.IMAGE_BUTTON_BACK=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/buttons_images/button_back.png')
        
        self.IMAGE_ARROW_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/arrow_icon.png')
        self.IMAGE_WRONG_PASSWORD_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/wrong_password_icon.png')
        self.IMAGE_SUCCESS_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/success_icon.png')
        self.IMAGE_XMARK_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/xmark_icon.png')
        self.IMAGE_ENTRY_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/entry_icon.png')
        self.IMAGE_EXIT_ICON=pygame.image.load(r'C:/Users/User/Desktop/Kopia_RFID/images/exit_icon.png')
        

        self.FONT_ACTUAL_DATE = pygame.font.SysFont('arial', 30,bold=True)
        self.FONT_ACTUAL_DATE_NAME = pygame.font.SysFont('arial', 30,bold=True)
        self.FONT_ACTUAL_HOUR = pygame.font.SysFont('arial', 68,bold=True)
        self.FONT_ACTUAL_HOUR_TITLE = pygame.font.SysFont('arial', 200,bold=True)
        self.FONT_CONNECTION_TITLE = pygame.font.SysFont('arial', 30,bold=True)
        self.FONT_CONNECTION_STATUS = pygame.font.SysFont('arial', 30,bold=True)
        self.FONT_MAIN_MENU_TITLE = pygame.font.SysFont('arial', 110,bold=True)
        self.FONT_RECORD_DETAILS = pygame.font.SysFont('arial', 20,bold=True)
        self.FONT_RECORD_NAME = pygame.font.SysFont('arial', 35,bold=True)
        self.FONT_TYPED_PIN = pygame.font.SysFont('arial',150,bold=True)
        self.FONT_PIN_ERROR_MESSAGE = pygame.font.SysFont('arial',110,bold=True)
        self.FONT_ADMIN_PANEL_TITLE = pygame.font.SysFont('arial',35,bold=True)
        self.FONT_ADMIN_PANEL_MESSAGE_1 = pygame.font.SysFont('arial',50,bold=True)
        self.FONT_ADMIN_PANEL_MESSAGE_2 = pygame.font.SysFont('arial',40,bold=True)
        self.FONT_ADMIN_PANEL_PIN_ERROR_MESSAGE = pygame.font.SysFont('arial',50,bold=True)
        self.FONT_ADMIN_PANEL_PAIRING_TITLE = pygame.font.SysFont('arial',50,bold=True)
        self.FONT_ADMIN_PANEL_PAIRING_USER = pygame.font.SysFont('arial',75,bold=True)
        self.FONT_ADMIN_PANEL_PAIRING_MESSAGE_1 = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_ADMIN_PANEL_PAIRING_OK_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_ADMIN_PANEL_PAIRING_ERROR_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_RFID_ERROR_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_RFID_ENTRY_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_RFID_USER_NAME = pygame.font.SysFont('arial',90,bold=True)
        self.FONT_RFID_EXIT_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_RFID_EXIT_TIME_TITLE = pygame.font.SysFont('arial',80,bold=True)
        self.FONT_RFID_EXIT_TIME = pygame.font.SysFont('arial',180,bold=True)
        
        self.BEEP_FREQUENCY=2500
        self.BEEP_TIME=300
       
        #Delays
        self.WINDOW_PIN_ERROR_DELAY=1.7
        self.WINDOW_ADMIN_PIN_ERROR_DELAY=2.5
        self.WINDOW_RFID_DELAY=2.5
        self.RFID_DELAY=3.5
        self.RFID_CONNECTION_STATUS_DELAY=25

        #Title and mouse configurations
        pygame.display.set_caption("Aplikacja RFID")
        pygame.mouse.set_visible(False)

        #Custom events to handle user actions
        self.CLICKED_SUBMIT_BUTTON=pygame.USEREVENT + 1
        self.CLICKED_SHOW_KEYBOARD_BUTTON=pygame.USEREVENT + 2
        self.CLICKED_HIDE_KEYBOARD_BUTTON=pygame.USEREVENT + 3
        self.CLICKED_LOGOUT_BUTTON=pygame.USEREVENT + 4
        self.CLICKED_BACK_BUTTON=pygame.USEREVENT + 5
        self.RFID_APPLIED_ENTRY=pygame.USEREVENT + 6
        self.RFID_APPLIED_EXIT=pygame.USEREVENT + 7
        self.RFID_APPLIED_PARRIED=pygame.USEREVENT + 8

        #Variables to control windows
        self.WINDOW_MAIN_MENU_BEFORE_BUTTON=True #done
        self.WINDOW_MAIN_MENU_AFTER_BUTTON=False #done
        self.WINDOW_RFID_ENTRY=False #done
        self.WINDOW_RFID_EXIT=False #done
        self.WINDOW_RFID_ERROR=False #done
        self.WINDOW_PIN_ERROR=False #done
        self.WINDOW_ADMIN_PANEL=False #done
        self.WINDOW_ADMIN_PIN_ERROR=False #done 
        self.WINDOW_ADMIN_PAIRING=False #done
        self.WINDOW_ADMIN_PAIRING_OK=False #done
        self.WINDOW_ADMIN_PAIRING_ERROR=False #done


        #thread to control window variables      
        _thread.start_new_thread(self.screen_menager,())
        



        #Variable to control main program loop
        
        self.BACKEND=backend.backend(pygame,self)
        self.RUN=True
        self.init_gui()


    def init_gui(self):
        while self.RUN:

           
            self.ELEMENTS=elements.elements(pygame,self)
            

            if self.WINDOW_MAIN_MENU_BEFORE_BUTTON:
                self.BACKGROUND_COLOR="#454443"

                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_MAIN_MENU_BEFORE_BUTTON(self)
                pygame.display.update()


            elif self.WINDOW_MAIN_MENU_AFTER_BUTTON:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_MAIN_MENU_AFTER_BUTTON(self)
                pygame.display.update()


            elif self.WINDOW_PIN_ERROR:
                self.BACKGROUND_COLOR="#1f1f1f"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_PIN_ERROR(self)
                pygame.display.update()
                

            elif self.WINDOW_ADMIN_PANEL:
                self.BACKGROUND_COLOR="#066969"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_ADMIN_PANEL(self)
                pygame.display.update()
            
            elif self.WINDOW_ADMIN_PIN_ERROR:
                self.BACKGROUND_COLOR="#043636"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_ADMIN_PIN_ERROR(self)
                pygame.display.update()
            
            elif self.WINDOW_ADMIN_PAIRING:
                self.BACKGROUND_COLOR="#078f8f"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_ADMIN_PAIRING(self)
                pygame.display.update()
            
            elif self.WINDOW_ADMIN_PAIRING_OK:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_ADMIN_PAIRING_OK(self)
                pygame.display.update()

            elif self.WINDOW_ADMIN_PAIRING_ERROR:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_ADMIN_PAIRING_ERROR(self)
                pygame.display.update()

            elif self.WINDOW_RFID_ERROR:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_RFID_ERROR(self)
                pygame.display.update()
            
            elif self.WINDOW_RFID_ENTRY:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_RFID_ENTRY(self)
                pygame.display.update()

            elif self.WINDOW_RFID_EXIT:
                self.BACKGROUND_COLOR="#454443"
                self.BACKGROUND_MAIN.fill(pygame.Color(self.BACKGROUND_COLOR))
                self.check_events()
                self.ELEMENTS.INIT_WINDOW_RFID_EXIT(self)
                pygame.display.update()

    def screen_menager(self):
        while True:
            time.sleep(100)
            print(f"""
            self.WINDOW_MAIN_MENU_BEFORE_BUTTON:{self.WINDOW_MAIN_MENU_BEFORE_BUTTON}
            self.WINDOW_MAIN_MENU_AFTER_BUTTON:{self.WINDOW_MAIN_MENU_AFTER_BUTTON}
            self.WINDOW_PIN_ERROR:{self.WINDOW_PIN_ERROR}
            self.WINDOW_ADMIN_PANEL:{self.WINDOW_ADMIN_PANEL}
            self.WINDOW_ADMIN_PIN_ERROR:{self.WINDOW_ADMIN_PIN_ERROR}
            self.WINDOW_ADMIN_PAIRING:{self.WINDOW_ADMIN_PAIRING}
            self.WINDOW_ADMIN_PAIRING_OK:{self.WINDOW_ADMIN_PAIRING_OK}
            self.WINDOW_ADMIN_PAIRING_ERROR:{self.WINDOW_ADMIN_PAIRING_ERROR}

            """)
            
    def check_events(self):
        for event in pygame.event.get():
            


            #----MAIN MENU EVENTS----
            
            if self.WINDOW_MAIN_MENU_BEFORE_BUTTON==True:
                if event.type == pygame.FINGERDOWN:
                    typed_character=functions.CHECK_BUTTONS_MAIN_BEFORE_BUTTON(round(event.x,2),round(event.y,2))
                    
                    functions.CONTROL_PIN(pygame,self,typed_character)

                elif event.type==self.CLICKED_SHOW_KEYBOARD_BUTTON:

                    functions.CHANGE_SCREEN('WINDOW_MAIN_MENU_AFTER_BUTTON',pygame,self)
                
                elif event.type==self.RFID_APPLIED_ENTRY:


                    winsound.Beep(self.BEEP_FREQUENCY,self.BEEP_TIME)
                    worker_id=backend_functions.check_rfid_owner(str(event.id))

                    if worker_id:
                        type_of_last_record=backend_functions.check_type_of_last_record(worker_id)
                        
                        if type_of_last_record=='WEJSCIE':
                            self.RFID_EXIT_TIME=str(backend_functions.calculate_work_time(str(worker_id),self))
                            self.RFID_USER_NAME=backend_functions.check_name(worker_id)
                            backend_functions.insert_rfid_log_localdb(str(self.ACTUAL_DATE),str(self.BACKEND.TIME.hour),str(self.BACKEND.TIME.minute),"WYJSCIE",str(worker_id))
                            functions.CHANGE_SCREEN('WINDOW_RFID_EXIT',pygame,self)
                            _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self,self.WINDOW_RFID_DELAY))
                        else:
                            self.RFID_USER_NAME=backend_functions.check_name(worker_id)
                            backend_functions.insert_rfid_log_localdb(str(self.ACTUAL_DATE),str(self.BACKEND.TIME.hour),str(self.BACKEND.TIME.minute),"WEJSCIE",str(worker_id))
                            functions.CHANGE_SCREEN('WINDOW_RFID_ENTRY',pygame,self)
                            _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self,self.WINDOW_RFID_DELAY))
                    else:
                        functions.CHANGE_SCREEN('WINDOW_RFID_ERROR',pygame,self)
                        _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self,self.WINDOW_RFID_DELAY))



                    
            elif self.WINDOW_MAIN_MENU_AFTER_BUTTON==True:
                
                if event.type == pygame.FINGERDOWN:

                    typed_character=functions.CHECK_BUTTONS_MAIN_AFTER_BUTTON(round(event.x,2),round(event.y,2))
                    functions.CONTROL_PIN(pygame,self,typed_character)

                elif event.type==self.CLICKED_HIDE_KEYBOARD_BUTTON:

                    functions.CHANGE_SCREEN('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self)

                elif event.type==self.CLICKED_SUBMIT_BUTTON:
                    
                    if self.TYPED_PIN=="*405##":

                        functions.CHANGE_SCREEN('WINDOW_ADMIN_PANEL',pygame,self)

                    else:
                        login=backend_functions.user_login(self.TYPED_PIN)
                        if login:
                            self.RFID_USER_NAME=str(login[1])
                            type_of_last_record=backend_functions.check_type_of_last_record(str(login[0]))
                            if type_of_last_record=="WEJSCIE":
                                self.RFID_EXIT_TIME=str(backend_functions.calculate_work_time(str(login[0]),self))
                                functions.CHANGE_SCREEN('WINDOW_RFID_EXIT',pygame,self)
                                backend_functions.insert_pin_log_localdb(str(self.ACTUAL_DATE),str(self.BACKEND.TIME.hour),str(self.BACKEND.TIME.minute),"WYJSCIE",str(login[0]))
                                _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self,self.WINDOW_RFID_DELAY))
                            else:
                                functions.CHANGE_SCREEN('WINDOW_RFID_ENTRY',pygame,self)
                                backend_functions.insert_pin_log_localdb(str(self.ACTUAL_DATE),str(self.BACKEND.TIME.hour),str(self.BACKEND.TIME.minute),"WEJSCIE",str(login[0]))
                                _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self,self.WINDOW_RFID_DELAY))
                            


                        else:
                            functions.CHANGE_SCREEN('WINDOW_PIN_ERROR',pygame,self)
                            _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_MAIN_MENU_AFTER_BUTTON',pygame,self,self.WINDOW_PIN_ERROR_DELAY))
                
            #----ADMIN PANEL EVENTS----

            elif self.WINDOW_ADMIN_PANEL==True:
                if event.type == pygame.FINGERDOWN:
                    typed_character=functions.CHECK_BUTTONS_ADMIN_PANEL(round(event.x,2),round(event.y,2))
                    functions.CONTROL_PIN(pygame,self,typed_character)
                    
                elif event.type==self.CLICKED_LOGOUT_BUTTON:
                    
                    functions.CHANGE_SCREEN('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self)
                   
                elif event.type==self.CLICKED_SUBMIT_BUTTON:

                    #Find user's pin in database

                    login=backend_functions.user_login(self.TYPED_PIN)
                    if login:
                        self.ACTUAL_ID=str(login[0])
                        self.ADMIN_PANEL_PAIRING_USER=str(login[1])
                        functions.CHANGE_SCREEN('WINDOW_ADMIN_PAIRING',pygame,self)
                    else:
                        functions.CHANGE_SCREEN('WINDOW_ADMIN_PIN_ERROR',pygame,self)
                        _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_ADMIN_PANEL',pygame,self,self.WINDOW_ADMIN_PIN_ERROR_DELAY))
           
                



            elif self.WINDOW_ADMIN_PAIRING:
                if event.type == pygame.FINGERDOWN:

                    typed_character=functions.CHECK_BUTTONS_ADMIN_PAIRING(round(event.x,2),round(event.y,2))

                    functions.CONTROL_PIN(pygame,self,typed_character)
                elif event.type==self.RFID_APPLIED_ENTRY:
    
                    winsound.Beep(self.BEEP_FREQUENCY,self.BEEP_TIME)
                    
                    if backend_functions.insert_rfid_owner_localdb(str(event.id),str(self.ACTUAL_ID)):
                        functions.CHANGE_SCREEN('WINDOW_ADMIN_PAIRING_OK',pygame,self)
                        _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_ADMIN_PANEL',pygame,self,self.WINDOW_ADMIN_PIN_ERROR_DELAY))
                    else:
                        functions.CHANGE_SCREEN('WINDOW_ADMIN_PAIRING_ERROR',pygame,self)
                        _thread.start_new_thread(functions.CHANGE_SCREEN,('WINDOW_ADMIN_PANEL',pygame,self,self.WINDOW_ADMIN_PIN_ERROR_DELAY))
   






            if event.type == self.CLICKED_BACK_BUTTON:

                functions.CHANGE_SCREEN('WINDOW_MAIN_MENU_BEFORE_BUTTON',pygame,self)

            if event.type == pygame.KEYDOWN:
                #if schortcut CTRL+Q is clicked - quit
                if event.unicode=="\x11":
                    self.RUN = False
                    pygame.quit()

            
            






aplikacja=gui()