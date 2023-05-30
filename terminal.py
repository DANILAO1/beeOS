#this program is copyrighted by Danila(DANILAO)
#os isn't finished


def main():
    username = ""
    choice = ""
    settingchoice = ""
    folderschoice = ""
    run = True
    settings = True
    folder = True
    version = "v1.1a"

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    #user log
    print("copyrighted by Danila 2023©")
    print("welcome to beeOS ", version)
    username = input("\n\n\n\n\nwrite your username:>")

    #'user' home
    while run:
        choice = input(username + ":>")

        #home functions
        if choice == "exit":
            run = False

        elif choice == "BOS $version":
            print("BeeOS version ", version)

        #folders
        elif choice == "!folders":
            while folder:
                folderschoice = input("folders/" + username + ":>")

                if folderschoice == "exit":
                    folder = False
                
        
        #settings 
        elif choice == "!settings":
            while settings:
                settingchoice = input("settings/" + username + ":>")
                
                if settingchoice == "exit":
                    settings = False

                elif settingchoice == "sys updates":
                    print("there's no System updates yet")

                elif settingchoice == "os updates":
                    print("there's no OS updates yet")


    
main()