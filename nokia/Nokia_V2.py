while (True):

    main_menu = """
        List of menu function

        Press 1 for Phone book
        Press 2 for Message
        Press 3 for Chat  
        Press 4 for Call register
        Press 5 for Tone
        Press 6 for Setting 
        Press 7 for Call divert
        Press 8 for Games
        Press 9 for Calculate
        Press 10 for Reminder
        Press 11 for Clock
        Press 12 for Profiles
        Press 13 for SIM services

        Enter 0 to Exit

        """     
    print(main_menu)
    main_menu_list = int(input("main menu"))

    match main_menu_list:

        case 1 :
            print("Phone book")
            while(True):

                
                phone_book = """

                press 1 to Search 
                press 2 to ServiceNos
                press 3 to Addname
                press 4 to Erase
                press 5 to Edit
                press 6 to Assigntone
                press 7 to Send b'card
                press 8 to Option 
                press 9 to Speed dials
                press 10 to Voice tags

                Enter 0 to Exit

		        """
                print(phone_book)
                phone_book_list = int(input("phone book"))

                match phone_book_list:
                    case 1: 
                        print("Search")
                    case 2:
                        print("Service Nos") 
                    case 3: 
                        print("Add name")
                    case 4: 
                        print("Erase")  
                    case 5: 
                        print("Edit") 
                    case 6: 
                        print("Assign tone")
                    case 7: 
                        print("Send b'card")
                    case 8:

                        print("option")
                        while(True):
                            print("option")

                            option = """
                            press 1 : Type of view
                            press 2 : Memmory status

                            Enter 0 to Exit

                            """

                            print(option)
                    
                            option_list = int(input("option"))

                            match option_list:
                                case 1: 
                                    print("Type of view")
                                case 2:
                                    print("Memory status")
                                case 0: break
                                case _: 
                                    print("invalid")                     
                            

                    case 9: 
                        print("Speed dials")
                    case 10:            
                        print("Voice tags") 
                    case 0: break
                    case _: 
                        print("invalid")
                

        case 2 : 
            print("Message")
            while(True):
               
                message= """
                press 1 write message
                press 2 Inbox
                press 3 Outbox 
                press 4 Picture message
                press 5 Template 
                press 6 Smileys
                press 7 Message setting
                press 8 Info service 
                press 9 Voice mailbox number
                press 10 Service command editor
                Enter 0 to Exit

                """  
                print (message)
                message_list = int(input("message"))

                match message_list: 
                    case 1: 
                        print("Write message")
                    case 2:
                        print("Inbox") 
                    case 3: 
                        print("Outbox")
                    case 4: 
                        print("Picture message")  
                    case 5: 
                        print("Template") 
                    case 6: 
                        print("Smileys")
                    case 7: 
                        print("Message setting")
                        while(True):
                            print("message setting")
                            print()

                            message_setting = """ 

                            press 1 : Set
                            press 2 : Command 

                            Enter 0 to Exit

                            """ 
                            print(message_setting)
                            message_setting_list = int(input("message_setting"))

                            match message_setting_list:
                                case 1: 
                                    print("Set") 
                                case 2: 
                                    print("Command")
                                case 0: break
                                case _: 
                                    print("invalid message")

                    case 8: 
                        print("Info service")
                    case 9: 
                        print("Voice mailbox number")
                    case 10: 
                        print("Service command editor") 
                    case 0: break
                    case _: 
                        print("invalid input")


        case 3 : 
            print("Chat Menu")

        case 4 : 
            print("call_register")
            while(True):

                call_register = """
                press 1 Missed call
                press 2 Recieved call
                press 3 Dialled number
                press 4 Erase recent call lists
                press 5 Show call duration
                press 6 Show call costs
                press 7 Call cost settings
                press 8 Prepaid credit
                Enter 0 to Exit

                """ 
                print(call_register)
                call_register_list = int(input("call register list"))

                match call_register_list:
                    case 1: 
                        print("Missed call")
                    case 2: 
                        print("Recieved call")
                    case 3: 
                        print("Dialled number")
                    case 4: 
                        print("Erase recent call lists")
                    case 5: 
                        print("Show call duration")
                        while(True):
                            print("Show call duration")
                            

                            show_call_duration = """
                            press 1 Last call duration
                            press 2 All calls' duration
                            press 3 Received calls
                            press 4 Dialled calls duration
                            press 5 Clear times
                            Enter 0 to Exit

                            """

                            print(show_call_duration)
                            show_call_duration_list = int(input("show call duration"))

                            match show_call_duration_list:

                                case 1: 
                                    print("Last call duration")
                                case 2: 
                                    print("All calls' duration")
                                case 3: 
                                    print("Received calls")
                                case 4: 
                                    print("Dialled calls duration")
                                case 5: 
                                    print("Clear times")
                                case 0: break
                                case _: 
                                    print("Invalid")

                    case 6: 
                        print("Show call costs")
                        while(True): 

                            show_call_cost = """
                            press 1 Last cost 
                            press 2 All call's cost
                            press 3 Clear counter
                            Enter 0 to Exit

                            """
                            print(show_call_cost)
                            show_call_cost_list = int(input("show call cost"))
				
                            match show_call_cost_list:

                                case 1: 
                                    print("Last cost")
                                case 2: 
                                    print("All call's cost")
                                case 3: 
                                    print("Clear counter")
                                case 0: break     
                                case _: 
                                    print("Invalid")  

                    case 7:
                        print("Call cost settings")
                        while(True): 
                     
                            call_cost_settings = """

                            press 1 Call cost limit 
                            press 2 Show cost in
                            Enter 0 to Exit

                            """
                            print(call_cost_settings)

                            call_cost_setting_list = int (input("call cost settings"))

                            match call_cost_setting_list:
                                case 1: 
                                    print("Call cost limit")
                                case 2: 
                                    print("Show cost in") 
                                case 0: break
                                case _: 
                                    print("Error")

                    case 8: 
                        print("Prepaid credit")

                    case 0: break

                    case _: 
                        print("Error") 
            


        case 5 : 
            print("Tone Menu")
            while(True):
                #print("Tone Menu")

                tone_menu = """

                press 1 to Ringing tone 
                press 2 to Ringing volume
                press 3 to Incoming call alert
                press 4 to Composer
                press 5 to Message alert tone
                press 6 to Warning and game tone
                press 7 to Vibrating alert 
                press 8 to Screen Saver 
                Enter 0 to Exit

                """

                print(tone_menu)
                tone_menu_list = int (input("tone menu list"))

                match tone_menu_list:

                    case 1:
                        print("Ringing tone")
                    case 2: 
                        print("Ringing volume") 
                    case 3: 
                        print("Incoming call alert") 
                    case 4: 
                        print("Composer")
                    case 5: 
                        print(" Message alert tone")
                    case 6: 
                        print("Warning and game tone")
                    case 7: 
                        print("Vibrating alert") 
                    case 8: 
                        print("Screen Saver")
                    case 0: break

                    case _: 
                        print("error")



        case 6 :
            print("Setting Menu")
            while(True):

                setting_menu = """

                press 1 to Call setting 
                press 2 to Phone setting
                press 3 to Security setting
                press 4 to Restore factory setting
                Enter 0 to Exit

                """

                print(setting_menu)
                setting_menu_list = int(input("setting menu list"))

                match setting_menu_list:
                    case 1: 
                        print("Call setting")
                        while(True):

                            call_setting_menu = """

                            press 1 to Automatic radical
                            press 2 to Speed dailing
                            press 3 to Call waiting 
                            press 4 to Own number sending
                            press 5 to Phone line in use
                            press 6 to Automatic answer
                            Enter 0 to Exit

                            """   
                            print(call_setting_menu)
                            call_setting_menu_list = int(input("call setting menu"))

                            match call_setting_menu_list:

                                case 1:
                                    print("Automatic radical")
                                case 2: 
                                    print("Speed dailing")
                                case 3: 
                                    print("Call waiting")
                                case 4: 
                                    print("Own number sending")
                                case 5: 
                                    print("Phone line in use")
                                case 6: 
                                    print("Automatic answer")
                                case 0: break
                                case _: 
                                    print("error")

                    case 2: 
                        print("Phone setting") 
                        while(True):
    
                            phone_setting_menu = """

                            press 1 to language
                            press 2 to Call info display
                            press 3 to Welcome note
                            press 4 to Network selection
                            press 5 to Lights
                            press 6 to Confirms SIM service action
                            Enter 0 to Exit

                            """

                            print(phone_setting_menu)
                            phone_setting_menu_list = int(input("phone_setting_menu"))

                            match phone_setting_menu_list:
                                case 1:
                                    print("language")
                                case 2: 
                                    print("Call info display") 
                                case 3: 
                                    print("Welcome note") 
                                case 4: 
                                    print("Network selection")
                                case 5: 
                                    print("Lights") 
                                case 6: 
                                    print("Confirms SIM service action")
                                case 0: break
                                case _: 
                                    print("error")

                    case 3: 
                        print("Security setting")
                        while(True):

                            security_setting_menu = """

                            press 1 to Phone security
                            press 2 to PIN code
                            press 3 to Call baring service
                            press 4 to Fixed dialling
                            press 5 to Closed user group
                            press 6 to Change access code
                            Enter 0 to Exit

                            """

                            print(security_setting_menu)
                            security_setting_menu_list = int(input("security_setting_menu"))

                            match security_setting_menu_list: 
                                case 1: 
                                    print("Phone security")
                                case 2: 
                                    print("PIN code") 
                                case 3: 
                                    print("Call baring service") 
                                case 4: 
                                    print("Fixed dialling")
                                case 5: 
                                    print(" Closed user group")
                                case 6: 
                                    print("Change access code")
                                case 0: break        
                                case _: 
                                    print("error")
                    case 4: 
                        print("Restore factory setting") 
                    case 0: break
                    case _: 
                        print("error")

        case 7: 
            print("Call divert Menu")
        case 8:
            print("Games Menu")
        case 9: 
            print("Calculator Menu")
        case 10: 
            print("Reminder Menu")
        case 11: 
            print("Clock Menu")
            while(True):

                clock_menu = """

                press 1 to Alarm clock 
                press 2 to Clock setting
                press 3 to Date setting
                press 4 to Stop watch
                press 5 to Countdown
                press 6 to Auto update of date and time
                Enter 0 to Exit

		        """   
                
                print(clock_menu)
                clock_menu_list = int(input("clock_menu"));

                match clock_menu_list: 

                    case 1:
                        print("Alarm clock")
                    case 2: 
                        print("Clock setting")
                    case 3: 
                        print("Date setting") 
                    case 4: 
                        print("Stop watch")
                    case 5:  
                        print("Countdown") 
                    case 6: 
                        print(" Auto update of date and time")
                    case 0: break
                    case _: 
                        print("error")

        case 12: 
            print("Profile Menu") 
        case 13: 
            print("SIM service Menu") 
        case 0: 
            break
        case _:
            print("Invalid") 


           
                 


           
            
              
