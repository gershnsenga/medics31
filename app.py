from src.search_disease import *
from src.search_gender import *
from scripts.welcome import *
from scripts.app_menu import appMenu
from scripts.talk_to_doc import talkToDoc

def main():
    welcome()
    
    while True:
        appMenu()

        choice = int(input("\t\t\t --- Your Choice :: "))

        if choice == 1:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 2:
            disease = input("\n\t\t\t\t\t Type a disease : ")
            search_by_disease(disease)
        elif choice == 3:
            print("\n\n\t\t\t--- For search by gender\n\n")
            search_by_gender_menu()
        elif choice == 4:
            print("\n\n\t\t\t--- For disease and prevention\n\n")
        elif choice == 5:
            print("\n\n\t\t\t--- For disease and treatment\n\n")
        elif choice == 6:
            print("\n\n\t\t\t--- For talking to a doctor\n\n")
            talkToDoc()
        elif choice == 7:
            print("\n\n\t\t\t--- Exiting...\n\n")
            break
        else:
            print("\n\n\t\t\t--- No such choice\n\n")

if __name__ == "__main__":
    main()
