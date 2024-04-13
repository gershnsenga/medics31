from .app_menu import *

def talkToDoc():

    print("\t|                      1) Dr. Nmesoma: General medicine                                |")
    print("\t|                      2) Dr. Gershom : Internal medicine                                  |")
    print("\t|                      3) Dr. L.J: General medicine                                  |")
    print("\t|                      4) Dr. Tracy: Internal medicine                                  |")
    print("\t|                      5) Dr. David Peter: General medicine                                  |")
    print("\t|                      6) Dr. Jade: Internal medicine                                  |")
    print("\t|                      7) back to main menu                                  |")

    option = int(input("Select the doctor you want to speak with"))

    while True:
        if option == 1:
            print("\n\n\t\t\t--- DR.1 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 2:
            print("\n\n\t\t\t--- DR.2 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 3:
            print("\n\n\t\t\t--- DR.3 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 4:
            print("\n\n\t\t\t--- DR.4 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 5:
            print("\n\n\t\t\t--- DR.5 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 6:
            print("\n\n\t\t\t--- DR.6 BIO\n\n")
            print("press 1 to go back to previous menu?")
            print("press 2 to go back to main menu?")
            choice = int(input(" "))
            if choice == 1:
                talkToDoc()
            elif choice == 2:
                appMenu()
        elif option == 7:
            # print("\n\n\t\t\t--- Exiting...\n\n")
            # exit()
            appMenu()
        else:
                # print("\n\n\t\t\t--- For widely spread diseases\n\n")
            talkToDoc()


