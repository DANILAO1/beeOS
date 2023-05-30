#this program is copyrighted by Danila(DANILAO)
#os isn't finished

version = "v0.11a"

def main():
    username = ""
    choice = ""
    run = True
    version = "v0.11a"

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("copyrighted by Danila 2023©")
    print("welcome to beeOS ", version)
    username = input("\n\n\n\n\nwrite your username:>")

    while run:
        choice = input(username + ":>")

        if choice == "exit":
            run = False

        elif choice == "BOS $version":
            print("BeeOS version ", version)

    
main()