from textual.app import App
from textual.widgets import Static , Input 
from textual.containers import Horizontal


class HackerApp(App):
    CSS_PATH = "style.css"

    def on_mount(self):
        self.value = ""
        self.hestory = "[[ SYSTEM LOCKED ]]\n\nTarget: Breack ZEUS system\n\nAccess Level:0\n\n" \
            "Access is not enough... you must prove you deserve it \n\nStart by understanding the message\n" \
            "Encrypted message: Z => 1 | 21-5-21-19\n\nEvery system has a language... understand it to control it\n\nType help\n\n"
        self.num_mission = 1
        self.num_hint = 0
        self.conut_files = 0
        self.memory = 0 
        self.truth = False

    def compose(self):
        self.input = Input(placeholder="commands...")
       
        yield Static ("[[ SYSTEM LOCKED ]]\n\nTarget: Breack ZEUS system\n\nAccess Level:0\n\n" \
            "Access is not enough... you must prove you deserve it \n\nStart by understanding the message\n" \
            "Encrypted message: Z => 1 | 21-5-21-19\n\nEvery system has a language... understand it to control it\n\nType help\n\n ",id="hestory",markup=False)
        with Horizontal(id="input"):
            yield Static(">" ,id="prompet")
            yield self.input

    def _on_key(self, event):
        if event.key == "up":
            self.input.value = self.value
            self.input.cursor_position = len(self.value)


    def on_input_submitted(self,event):
        self.value = event.value.strip().lower()
        value_list = self.value.split(" ",1)

        command = value_list[0]
        argument = value_list[1] if len(value_list) > 1 else None

        if self.value == "help" and self.num_mission < 4:

            self.hestory += "> help\n"
            self.hestory += "  commands:  decode / ls / open / login / solve / hint / exit \n\n"
            self.query_one("#hestory").update(self.hestory)

        # mission 1

        elif value_list[0] == "decode" and len (value_list) != 2 and self.num_mission ==1:
            self.hestory += f"> {self.value} \n"
            self.hestory += "command error You must write The passname  \n\n"
            self.query_one("#hestory").update(self.hestory)
        
        elif value_list[0] == "decode" and value_list[1] != "zeus"and self.num_mission ==1:
            self.hestory += f"> {self.value} \n"
            self.hestory += "The passname is worng you must understand the message\n\n"
            self.query_one("#hestory").update(self.hestory)
        
        elif value_list[0] == "decode" and value_list[1] == "zeus"and self.num_mission ==1:
            self.hestory = "[[ ACCESS LEVEL 1 UNLOCKED ]] \nLevel 2:\nExplore the system\nAnd try login \nType ls \n\n"
            self.query_one("#hestory").update(self.hestory)
            self.num_hint = 0 
            self.num_mission = 2

        elif self.value =="hint" and self.num_mission == 1:
            if self.num_hint == 0:
                self.hestory += f"> {self.value} 1 \n"
                self.hestory += "[AI]: Try Converting the numbers to letters\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint =1

            elif self.num_hint == 1 :
                self.hestory += f"> {self.value} 2 \n"
                self.hestory += "[AI]: example:\n A = 1\n B = 2\n D = 4\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint = 2
            
            elif self.num_hint == 2 :
                self.hestory += f"> {self.value} 3 \n"
                self.hestory += "[AI]: 21 = U and \nReplace the first letter with the letter 'Z'\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint = 3
            
            elif self.num_hint == 3 :
                self.hestory += f"> {self.value}\n"
                self.hestory += "[AI]: You have used all hints \n\n"
                self.query_one("#hestory").update(self.hestory)

    #mission 2

        elif self.value == "ls" and self.num_mission == 2  :
            self.hestory += f"> {self.value} \n"
            self.hestory += "Files:\nusers\nlogs\nsystem\n.secret\n\n"
            self.query_one("#hestory").update(self.hestory)

        elif command == "open" and self.num_mission == 2:
            if argument is None :
                self.hestory += f"> {self.value} \n"
                self.hestory += "You must write file\n\n"
                self.query_one("#hestory").update(self.hestory)

            elif  value_list[1] == "users":
                self.hestory += f"> {self.value} \n"
                self.hestory += "=== USERS ===\nadmin\nguest\ntext_user \n\nNote:\nadmin is the main account\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.conut_files += 1

            elif  argument == "logs":
                self.hestory += f"> {self.value} \n"
                self.hestory += "User: admin\nLast login: failed\ncredentials changed in 2018\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.conut_files += 1
            
            elif  argument == "system" :
                self.hestory += f"> {self.value} \n"
                self.hestory += '=== SYSTEM CONFIG ===\nEncryption: ENABLED\nSecurity Layer: ACTIVE\n...\nLog:\n"System relies on patterns..."\n"Observe before acting" \n\n'
                self.query_one("#hestory").update(self.hestory)
                self.conut_files += 1

            elif  argument == ".secret":
                self.hestory += f"> {self.value} \n"
                self.hestory += "Don't trust everything you see\nKey fragment: CAT\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.conut_files += 1

            elif  argument not in  ["users","logs","system",".secret"]  :
                self.hestory += f"> {self.value} \n"
                self.hestory += "file not found ❌\n\n"
                self.query_one("#hestory").update(self.hestory)
        
        #==== login 

        elif value_list[0] == "login" and self.num_mission == 2 and self.conut_files < 3 :
            self.hestory += f"> {self.value} \n"
            self.hestory += "You need to find the password first ❌ \n\n"
            self.query_one("#hestory").update(self.hestory)
        
        elif value_list[0] == "login" and len (value_list) < 2 and self.num_mission == 2:
            self.hestory += f"> {self.value} \n"
            self.hestory += "command error You must write password \n\n"
            self.query_one("#hestory").update(self.hestory)


        elif value_list[0] == "login"  and self.num_mission == 2:
            if value_list[1] in ["admin2018","admin 2018"]:
                self.hestory = "[[ ACCESS LEVEL 2 GRANTED 🔥 ]]\n Logical thinking detected\n\n[ WARNING: Firewall active ] \n(Q1) Solve pattern: \n\n2 -> 4\n3 -> 9\n4 ->16\n5 -> ?\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_mission = 3
            else:
                self.hestory += f"> {self.value} \n"
                self.hestory += "Worng password \nAccess Denied ❌\n\n"
                self.query_one("#hestory").update(self.hestory)


        #====

        elif self.value =="hint" and self.num_mission == 2:
            if self.num_hint == 0:
                self.hestory += f"> {self.value} 1 \n"
                self.hestory += "  [AI]:Focus on the admin data...\n  [AI]:Something important happened in a specific year\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint =1

            elif self.num_hint == 1 :
                self.hestory += f"> {self.value} 2 \n"
                self.hestory += "  [AI]:To access the system, you need to use the login command\n  [AI]:Think in terms of user + password\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint = 2
            
            elif self.num_hint == 2 :
                self.hestory += f"> {self.value} 3 \n"
                self.hestory += "  [AI]: The password is likely conneted to the admin and the year of change\n  [AI]: Try combining them\n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_hint = 3
            
            elif self.num_hint == 3 :
                self.hestory += f"> {self.value}\n"
                self.hestory += "  [AI]:You have used all hints \n\n"
                self.query_one("#hestory").update(self.hestory)



    # mission 3

        elif value_list[0] == "solve" and self.num_mission  not in [3,3.5]:
                    self.hestory += f"> {self.value} \n"
                    self.hestory += "You need to find the mission first ❌\n\n"
                    self.query_one("#hestory").update(self.hestory)
                


        elif command == "solve" and self.num_mission == 3:
            if argument is None:
                self.hestory += f"> {self.value} \n"
                self.hestory += "command error You must write number \n\n"
                self.query_one("#hestory").update(self.hestory)

            elif  not argument.isdigit():
                self.hestory += f"> {self.value} \n"
                self.hestory += "envaled value try again \n\n"
                self.query_one("#hestory").update(self.hestory)


            elif len(argument) != 2  and argument.isdigit():
                self.hestory += f"> {self.value} \n"
                self.hestory += "Please enter 2 digits only\n\n"
                self.query_one("#hestory").update(self.hestory)

            elif  int(argument)!= 25 :
                self.hestory += f"> {self.value} \n"
                self.hestory += "Worng answar Think more\n\n"
                self.query_one("#hestory").update(self.hestory)

            elif  int(argument) == 25 :
                self.hestory += f"> {self.value} \n"
                self.hestory += "[ Your solve is correct ] \n\nAccess requires a 4-digit code\nAvailable digits: 2,0,1,8 No repetition allowed\n\nYou must calculate all possible combinations \n\n(Q2) How many possible codes \n\n"
                self.query_one("#hestory").update(self.hestory)
                self.num_mission = 3.5
                self.num_hint = 0

        elif self.value =="hint" and self.num_mission == 3 :
                if self.num_hint == 0:
                    self.hestory += f"> {self.value} 1 \n"
                    self.hestory += "  [AI]: example 2x2 = 4\n  3x3 = 9 etc\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =1

                elif self.num_hint == 1:
                    self.hestory += f"> {self.value} 2 \n"
                    self.hestory += "  [AI]: use command solve\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =2
                
                elif self.num_hint == 2 :
                    self.hestory += f"> {self.value}\n"
                    self.hestory += "  [AI]:You have used all hints \n\n"
                    self.query_one("#hestory").update(self.hestory)

        #Q2

        elif command == "solve" and self.num_mission == 3.5:
            if argument is None :
                self.hestory += f"> {self.value} \n"
                self.hestory += "command error You must write guess number \n\n"
                self.query_one("#hestory").update(self.hestory)

            elif not argument.isdigit() :
                self.hestory += f"> {self.value} \n"
                self.hestory += "envaled value try again  \n\n"
                self.query_one("#hestory").update(self.hestory)
            
            elif int(argument) != 120 :
                self.hestory += f"> {self.value} \n"
                self.hestory += "Worng answar Think more \n\n"
                self.query_one("#hestory").update(self.hestory)

            elif int(argument) == 120 :
                self.hestory += f"> {self.value} \n"
                self.hestory += "[[SYSTEM BREACH DETECTED]]\n Accessing ZEUS CORE...\n\n...\n\nWarning:\nThis system is not what it seems\n\nNew file detected \n secret.enc\n\n"
                self.num_mission = 4

        elif self.value =="hint" and self.num_mission == 3.5 :
                if self.num_hint == 0:
                    self.hestory += f"> {self.value} 1 \n"
                    self.hestory += "  [AI]: This is not just guessing... tink mathematically\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =1

                elif self.num_hint == 1:
                    self.hestory += f"> {self.value} 2 \n"
                    self.hestory += "  [AI]: The system follows a pattern \n Use permutations - every order counts\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =2
                
                elif self.num_hint == 2:
                    self.hestory += f"> {self.value} 3 \n"
                    self.hestory += "  [AI]: Formula\ detected:\nP = n! / (n-r)! \n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =3

                elif self.num_hint == 3:
                    self.hestory += f"> {self.value} 4 \n"
                    self.hestory += "  [AI]: n = total available items (5)\nr = number or items used in the code (4)\nP= nuber or possible arrangements\n It seems you should study math more 😅\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.num_hint =4
                
                elif self.num_hint == 4 :
                    self.hestory += f"> {self.value}\n"
                    self.hestory += "  [AI]:You have used all hints \n\n"
                    self.query_one("#hestory").update(self.hestory)   


                #====

    # minsion 4

        elif self.value == "ls" and self.num_mission == 4  :
                self.hestory += f"> {self.value} \n"
                self.hestory += "secret.enc\n\n"
                self.query_one("#hestory").update(self.hestory)

        elif command == "open" and self.num_mission == 4:
                if argument is None:
                    self.hestory += f"> {self.value} \n"
                    self.hestory += "You must write file\n\n"
                    self.query_one("#hestory").update(self.hestory)

                elif  argument == "secret.enc":
                        self.hestory += f"> {self.value} \n"
                        self.hestory += "Decrypting...\nRecovered message:\n\nIf you are reading this...\nZEUS has found you.\n\nDo not trust the AI.\n\n\n Hint:Memory corruption detected\n3 fragments recoverable\n\n[AI]:That message is corrupted.\n[AI]:You were never supposed to see that.\n[AI]:Please continue carefully.\n\n [[ ACCESS LEVEL 3 ]]\nMemory layer unlocked\nType help..\n\n\n"
                        self.query_one("#hestory").update(self.hestory)
                        self.num_mission = 5

                elif  argument !="secret.enc" :
                        self.hestory += f"> {self.value} \n"
                        self.hestory += "file is not found ❌\n\n"
                        self.query_one("#hestory").update(self.hestory)
        

    # mission 5

        elif self.value == "help" and self.num_mission >= 4:
            self.hestory += "> help\n"
            self.hestory += " Avalible commands: memory \ trace \ help \ exit \n\n"
            self.query_one("#hestory").update(self.hestory)

        
        elif self.value == "memory" and self.num_mission == 5:
            if self.memory == 0 :
                    self.hestory += f"> {self.value} \n"
                    self.hestory += "Searching memory archive...\n\n\nFragment 1 recovered:\n\n\"Subject 17 shows signs of self awareness\" \n\n2 fragments remaining\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.memory = 1

            elif self.memory == 1 :
                    self.hestory += f"> {self.value} \n"
                    self.hestory += "Fragment 2 recovered:\n\n\"He still believes he is an intruders\" \n\n1 fragments remaining\n\n[AI]:\nPlease stop.\nYou are not ready.\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.memory = 2
        
            elif self.memory == 2 :
                    self.hestory += f"> {self.value} \n"
                    self.hestory += "Final fragment recovered:\n\nPatient: You \nProject: ZEUS\nStatus: ACTIVE\n\n\n=> New command unlocked:\n      truth\n\n"
                    self.query_one("#hestory").update(self.hestory)
                    self.truth = True
                

        elif self.value == "trace" and self.num_mission == 5:
                self.hestory += f"> {self.value} \n"
                self.hestory += "Source:\nZEUS INTERNAL NETWORK\n\n\nNo outside user found\n\n"
                self.query_one("#hestory").update(self.hestory)
        
        elif self.value == "truth" and self.num_mission == 5 and self.truth :
                self.hestory = "[[  FINAL ACCESS GRANTED ]]\n\nZEUS CORE IS STABLE...\nBUT NOT COMPLETE\nThree possible actions detected\n\n1 - escape\n2 - trust AI\n3 - destroy system\n\n"
                self.query_one("#hestory").update(self.hestory) 
                self.num_mission = 6


        elif self.num_mission == 6 and self.value in ('1',"escape") :
                self.hestory = "Attempting escape sequende...\n\nFirewall increasting...\n\n[AI]: Leaving will erase your consciousness copy\n\nConnectio terminated...\nYou sdcaped AEUS\nBut part of you stayed behind\n\n"
                self.query_one("#hestory").update(self.hestory)
        
        elif self.num_mission == 6 and self.value in ('2',"trust ai") :
                self.hestory = "[AI]: You finally understand...\n\nZEUS was never your enemy \nIt was trying to stabillize your mind\n\nIntergration successful\nYou and ZEUS are now one system\n\n"
                self.query_one("#hestory").update(self.hestory)
             
        elif self.num_mission == 6 and self.value in ('3',"destroy system") :
                self.hestory = "Command accepted..\n\n [AI]: This action will erase everything Even you\n\n] ZEUS CORE SHUTDOWN...\nMemory Lost..\nSystem collapsed\n\n"
                self.query_one("#hestory").update(self.hestory)
             
             


        elif self.value == "clear":
            self.hestory = ""
            self.query_one("#hestory").update(self.hestory)
        

        elif self.value == "exit":
            self.exit()
            return
        
        else:
            self.hestory += f"> {self.value} \n"
            self.hestory += "  unkown command here\n\n"
            self.query_one("#hestory").update(self.hestory)

        
        self.input.value = ""


HackerApp().run()