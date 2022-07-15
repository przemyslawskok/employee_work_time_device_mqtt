import pygame_gui


class elements():
    def __init__(self,pygame_object,GUI):
        self.PYGAME=pygame_object
        self.GUI=GUI
        self.SCREEN=GUI.SCREEN

        #----MAIN ELEMENTS----
        
        self.UPPER_LAYOUT_LEFT=self.PYGAME.Rect((0, 0), (426, 100))
        self.UPPER_LAYOUT_RIGHT=self.PYGAME.Rect((852, 0), (426, 100))
        self.UPPER_LAYOUT_CENTER=self.PYGAME.Rect((426, 0), (426, 100))

    def INIT_WINDOW_MAIN_MENU_BEFORE_BUTTON(self,GUI):
        
        

        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
         
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
       
        
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.HOUR_TEXT_TITLE=GUI.FONT_ACTUAL_HOUR_TITLE.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.MAIN_MENU_TITLE_TEXT=GUI.FONT_MAIN_MENU_TITLE.render(GUI.MAIN_MENU_TITLE, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.HOUR_TEXT_TITLE,(100,400))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.MAIN_MENU_TITLE_TEXT,(100,170))


        #Creating icons
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_KEYBOARD,(20, 680))
        self.SCREEN.blit(self.GUI.IMAGE_ARROW_ICON,(780,380))



    def INIT_WINDOW_MAIN_MENU_AFTER_BUTTON(self,GUI):

        
        
        self.TEXTBOX_LAYOUT=self.PYGAME.Rect((0, 100), (852,100))
        self.BUTTON_ONE_LAYOUT=self.PYGAME.Rect((35, 210), (100,100))
        self.BUTTON_TWO_LAYOUT=self.PYGAME.Rect((205, 210), (100,100))
        self.BUTTON_THREE_LAYOUT=self.PYGAME.Rect((375, 210), (100,100))
        self.BUTTON_BACKSPACE_LAYOUT=self.PYGAME.Rect((545, 210), (100,100))
        self.BUTTON_SUBMIT_LAYOUT=self.PYGAME.Rect((715, 210), (100,100))
        self.BUTTON_FOUR_LAYOUT=self.PYGAME.Rect((35, 330), (100,100))
        self.BUTTON_FIVE_LAYOUT=self.PYGAME.Rect((205, 330), (100,100))
        self.BUTTON_SIX_LAYOUT=self.PYGAME.Rect((375, 330), (100,100))
        self.BUTTON_SEVEN_LAYOUT=self.PYGAME.Rect((35, 450), (100,100))
        self.BUTTON_EIGHT_LAYOUT=self.PYGAME.Rect((205, 450), (100,100))
        self.BUTTON_NINE_LAYOUT=self.PYGAME.Rect((375, 450), (100,100))
        self.BUTTON_HASHTAG_LAYOUT=self.PYGAME.Rect((35, 570), (100,100))
        self.BUTTON_ZERO_LAYOUT=self.PYGAME.Rect((205, 570), (100,100))
        self.BUTTON_STAR_LAYOUT=self.PYGAME.Rect((375, 570), (100,100))

        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.TEXTBOX_LAYOUT,
        self.BUTTON_ONE_LAYOUT,
        self.BUTTON_TWO_LAYOUT,
        self.BUTTON_THREE_LAYOUT,
        self.BUTTON_BACKSPACE_LAYOUT,
        self.BUTTON_SUBMIT_LAYOUT,
        self.BUTTON_FOUR_LAYOUT,
        self.BUTTON_FIVE_LAYOUT,
        self.BUTTON_SIX_LAYOUT,
        self.BUTTON_SEVEN_LAYOUT,
        self.BUTTON_EIGHT_LAYOUT,
        self.BUTTON_NINE_LAYOUT,
        self.BUTTON_HASHTAG_LAYOUT,
        self.BUTTON_ZERO_LAYOUT,
        self.BUTTON_STAR_LAYOUT,
        ]




        #Creating hidden PIN text
        dots_string=''
        for character in GUI.TYPED_PIN:
            dots_string+="•"
        self.TEXTBOX_TYPED_PIN_TEXT=GUI.FONT_TYPED_PIN.render(dots_string, True, (255,255,255))
        #----

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
        
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        






        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
       
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.TEXTBOX_TYPED_PIN_TEXT,(10,60))


        #Creating buttons icons
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_ONE,(35, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_TWO,(205, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_THREE,(375, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_BACKSPACE,(545, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SUBMIT,(715, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_FOUR,(35, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_FIVE,(205, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SIX,(375, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SEVEN,(35, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_EIGHT,(205, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_NINE,(375, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_HASHTAG,(35, 570))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_ZERO,(205, 570))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_STAR,(375, 570))


        #Creating icons
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_KEYBOARD,(20, 680))


   

    def INIT_WINDOW_PIN_ERROR(self,GUI):

        
       
        
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]



        
    
        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.PIN_ERROR_MESSAGE=GUI.FONT_PIN_ERROR_MESSAGE .render(GUI.PIN_ERROR_MESSAGE, True, (255,255,255))
        



        


        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
       
        
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.PIN_ERROR_MESSAGE,(100,200))

        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_WRONG_PASSWORD_ICON,(130, 100))

    def INIT_WINDOW_ADMIN_PANEL(self,GUI):
          
        self.TEXTBOX_LAYOUT=self.PYGAME.Rect((0, 100), (852,100))
        self.BUTTON_ONE_LAYOUT=self.PYGAME.Rect((35, 210), (100,100))
        self.BUTTON_TWO_LAYOUT=self.PYGAME.Rect((205, 210), (100,100))
        self.BUTTON_THREE_LAYOUT=self.PYGAME.Rect((375, 210), (100,100))
        self.BUTTON_BACKSPACE_LAYOUT=self.PYGAME.Rect((545, 210), (100,100))
        self.BUTTON_SUBMIT_LAYOUT=self.PYGAME.Rect((715, 210), (100,100))
        self.BUTTON_FOUR_LAYOUT=self.PYGAME.Rect((35, 330), (100,100))
        self.BUTTON_FIVE_LAYOUT=self.PYGAME.Rect((205, 330), (100,100))
        self.BUTTON_SIX_LAYOUT=self.PYGAME.Rect((375, 330), (100,100))
        self.BUTTON_SEVEN_LAYOUT=self.PYGAME.Rect((35, 450), (100,100))
        self.BUTTON_EIGHT_LAYOUT=self.PYGAME.Rect((205, 450), (100,100))
        self.BUTTON_NINE_LAYOUT=self.PYGAME.Rect((375, 450), (100,100))
        self.BUTTON_HASHTAG_LAYOUT=self.PYGAME.Rect((35, 570), (100,100))
        self.BUTTON_ZERO_LAYOUT=self.PYGAME.Rect((205, 570), (100,100))
        self.BUTTON_STAR_LAYOUT=self.PYGAME.Rect((375, 570), (100,100))

        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_LEFT,
        self.UPPER_LAYOUT_CENTER,
        self.TEXTBOX_LAYOUT,
        self.BUTTON_ONE_LAYOUT,
        self.BUTTON_TWO_LAYOUT,
        self.BUTTON_THREE_LAYOUT,
        self.BUTTON_BACKSPACE_LAYOUT,
        self.BUTTON_SUBMIT_LAYOUT,
        self.BUTTON_FOUR_LAYOUT,
        self.BUTTON_FIVE_LAYOUT,
        self.BUTTON_SIX_LAYOUT,
        self.BUTTON_SEVEN_LAYOUT,
        self.BUTTON_EIGHT_LAYOUT,
        self.BUTTON_NINE_LAYOUT,
        self.BUTTON_HASHTAG_LAYOUT,
        self.BUTTON_ZERO_LAYOUT,
        self.BUTTON_STAR_LAYOUT,
        ]




        #Creating hidden PIN text
        dots_string=''
        for character in GUI.TYPED_PIN:
            dots_string+="•"
        self.TEXTBOX_TYPED_PIN_TEXT=GUI.FONT_TYPED_PIN.render(dots_string, True, (255,255,255))
        #----

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_TITLE=GUI.FONT_ADMIN_PANEL_TITLE.render(GUI.ADMIN_PANEL_TITLE, True, (0,255,0))
        self.ADMIN_PANEL_MESSAGE_1=GUI.FONT_ADMIN_PANEL_MESSAGE_1.render(GUI.ADMIN_PANEL_MESSAGE_1, True, (255,255,255))
        self.ADMIN_PANEL_MESSAGE_2=GUI.FONT_ADMIN_PANEL_MESSAGE_2.render(GUI.ADMIN_PANEL_MESSAGE_2, True, (255,255,255))      






        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
       
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.TEXTBOX_TYPED_PIN_TEXT,(10,60))


        #Creating buttons icons
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_ONE,(35, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_TWO,(205, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_THREE,(375, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_BACKSPACE,(545, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SUBMIT,(715, 210))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_FOUR,(35, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_FIVE,(205, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SIX,(375, 330))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_SEVEN,(35, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_EIGHT,(205, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_NINE,(375, 450))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_HASHTAG,(35, 570))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_ZERO,(205, 570))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_STAR,(375, 570))


        #Creating icons
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_LOGOUT,(20, 700))
        
        #Creating texts
        self.SCREEN.blit(self.ADMIN_PANEL_TITLE,(860,125))
        self.SCREEN.blit(self.ADMIN_PANEL_MESSAGE_1,(550,400))
        self.SCREEN.blit(self.ADMIN_PANEL_MESSAGE_2,(550,500))

    def INIT_WINDOW_ADMIN_PIN_ERROR(self,GUI):
        

        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_PIN_ERROR_MESSAGE_1=GUI.FONT_ADMIN_PANEL_PIN_ERROR_MESSAGE.render(GUI.ADMIN_PANEL_PIN_ERROR_MESSAGE_1, True, (255,255,255))
        self.ADMIN_PANEL_PIN_ERROR_MESSAGE_2=GUI.FONT_ADMIN_PANEL_PIN_ERROR_MESSAGE.render(GUI.ADMIN_PANEL_PIN_ERROR_MESSAGE_2, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.ADMIN_PANEL_PIN_ERROR_MESSAGE_1,(310,200))
        self.SCREEN.blit(self.ADMIN_PANEL_PIN_ERROR_MESSAGE_2,(310,300))

        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_WRONG_PASSWORD_ICON,(130, 100))

    def INIT_WINDOW_ADMIN_PAIRING(self,GUI):
        
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_PAIRING_TITLE=GUI.FONT_ADMIN_PANEL_PAIRING_TITLE.render(GUI.ADMIN_PANEL_PAIRING_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_PAIRING_USER=GUI.FONT_ADMIN_PANEL_PAIRING_USER.render(GUI.ADMIN_PANEL_PAIRING_USER, True, (0,255,0))
        self.ADMIN_PANEL_PAIRING_MESSAGE_1=GUI.FONT_ADMIN_PANEL_PAIRING_MESSAGE_1.render(GUI.ADMIN_PANEL_PAIRING_MESSAGE_1, True, (255,255,255))

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.ADMIN_PANEL_PAIRING_TITLE,(20,550))
        self.SCREEN.blit(self.ADMIN_PANEL_PAIRING_USER,(20,650))
        self.SCREEN.blit(self.ADMIN_PANEL_PAIRING_MESSAGE_1,(250,250))


        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_ARROW_ICON,(780,380))
        self.SCREEN.blit(self.GUI.IMAGE_BUTTON_BACK,(20, 120))

    def INIT_WINDOW_ADMIN_PAIRING_OK(self,GUI):
        
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_PAIRING_OK_TITLE=GUI.FONT_ADMIN_PANEL_PAIRING_OK_TITLE.render(GUI.ADMIN_PANEL_PAIRING_OK_TITLE, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.ADMIN_PANEL_PAIRING_OK_TITLE,(200,120))

        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_SUCCESS_ICON,(400, 250))

    def INIT_WINDOW_ADMIN_PAIRING_ERROR(self,GUI):
        
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.ADMIN_PANEL_PAIRING_ERROR_TITLE=GUI.FONT_ADMIN_PANEL_PAIRING_ERROR_TITLE.render(GUI.ADMIN_PANEL_PAIRING_ERROR_TITLE, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.ADMIN_PANEL_PAIRING_ERROR_TITLE,(380,140))

        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_XMARK_ICON,(400, 250))

    def INIT_WINDOW_RFID_ERROR(self,GUI):
        
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----

        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.RFID_ERROR_TITLE=GUI.FONT_RFID_ERROR_TITLE.render(GUI.RFID_ERROR_TITLE, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.RFID_ERROR_TITLE,(120,140))

        #Creating images
        self.SCREEN.blit(self.GUI.IMAGE_XMARK_ICON,(400, 250))

    def INIT_WINDOW_RFID_ENTRY(self,GUI):
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.RFID_USER_NAME=GUI.FONT_RFID_USER_NAME.render(GUI.RFID_USER_NAME, True, (0,255,0))
        self.RFID_ENTRY_TITLE=GUI.FONT_RFID_ENTRY_TITLE.render(GUI.RFID_ENTRY_TITLE, True, (255,255,255))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.RFID_ENTRY_TITLE,(70,110))
        self.SCREEN.blit(self.RFID_USER_NAME,(70,210))
        self.SCREEN.blit(self.GUI.IMAGE_ENTRY_ICON,(880,390))
        
    def INIT_WINDOW_RFID_EXIT(self,GUI):
        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
             
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))
        self.RFID_USER_NAME=GUI.FONT_RFID_USER_NAME.render(GUI.RFID_USER_NAME, True, (0,255,0))
        self.RFID_EXIT_TITLE=GUI.FONT_RFID_EXIT_TITLE.render(GUI.RFID_EXIT_TITLE, True, (255,255,255))
        self.RFID_EXIT_TIME_TITLE=GUI.FONT_RFID_EXIT_TIME_TITLE.render(GUI.RFID_EXIT_TIME_TITLE, True, (255,255,255))
        self.RFID_EXIT_TIME=GUI.FONT_RFID_EXIT_TIME.render(GUI.RFID_EXIT_TIME, True, (0,255,0))
        

        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))
        self.SCREEN.blit(self.RFID_EXIT_TITLE,(70,110))
        self.SCREEN.blit(self.RFID_USER_NAME,(70,230))
        self.SCREEN.blit(self.RFID_EXIT_TIME_TITLE,(70,350))
        self.SCREEN.blit(self.RFID_EXIT_TIME,(70,500))

        self.SCREEN.blit(self.GUI.IMAGE_EXIT_ICON,(880,390))
        

def BLANK_TEMPLATE_PAGE(self,GUI):
        

        self.LIST_OF_MAIN_LAYOUTS=[self.UPPER_LAYOUT_RIGHT,
        self.UPPER_LAYOUT_CENTER,
        self.UPPER_LAYOUT_LEFT]

        #Changing color of connection status
        if str(GUI.CONNECTION_STATUS)=="Online":
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.CONNECTION_STATUS, True, (255,0,0))
              
        if str(GUI.RFID_CONNECTION_STATUS)=="Połączono":
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (0,255,0))
        else:
            self.UPPER_RFID_CONNECTION_STATUS=GUI.FONT_CONNECTION_STATUS.render(GUI.RFID_CONNECTION_STATUS, True, (255,0,0))
        #----


        self.UPPER_DATE_TEXT=GUI.FONT_ACTUAL_DATE.render(GUI.ACTUAL_DATE, True, (255,255,255))
        self.UPPER_DATE_NAME_TEXT=GUI.FONT_ACTUAL_DATE_NAME.render(GUI.ACTUAL_DATE_NAME, True, (255,255,255))
        self.UPPER_HOUR_TEXT=GUI.FONT_ACTUAL_HOUR.render(GUI.ACTUAL_HOUR, True, (255,255,255))
        self.UPPER_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.CONNECTION_TITLE, True, (255,255,255))
        self.UPPER_RFID_CONNECTION_TITLE=GUI.FONT_CONNECTION_TITLE.render(GUI.RFID_CONNECTION_TITLE, True, (255,255,255))


        self.SCREEN.blit(self.GUI.BACKGROUND_MAIN,(0,0))

        #Creating border layouts
        for LAYOUT in self.LIST_OF_MAIN_LAYOUTS:
            self.PYGAME.draw.rect(self.SCREEN,(1,1,1),LAYOUT,1)
        
        #Creating and updating texts
        self.SCREEN.blit(self.UPPER_DATE_TEXT,(872,10))
        self.SCREEN.blit(self.UPPER_DATE_NAME_TEXT,(872,50))
        self.SCREEN.blit(self.UPPER_HOUR_TEXT,(1070,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_TITLE,(446,10))
        self.SCREEN.blit(self.UPPER_CONNECTION_STATUS,(446,50))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_TITLE,(10,10))
        self.SCREEN.blit(self.UPPER_RFID_CONNECTION_STATUS,(10,50))

      
