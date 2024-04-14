from src.search_disease import *
from src.search_gender import *
from src.disease_and_prevention import *
from src.widelyspreaddiseases import *
from scripts.welcome import *
from scripts.app_menu import *
from scripts.talk_to_doc import talkToDoc

def main():
    welcome()
    
    while True:
        appMenu()

        choice = int(input("\t\t\t --- Your Choice :: "))

        match choice:
            case 1:
                getDisease()
            case 2:
                disease = input("\n\t\t\t\t\t Type a disease : ")
                search_by_disease(disease)
            case 3:
                print("\n\n\t\t\t--- For search by gender\n\n")
                search_by_gender_menu()
            case 4:
                print("\n\n\t\t\t--- For disease and prevention\n\n")
                disease = input("\n\t\t\t\t\t Type a disease : ")
                disease_and_prevention(disease)
            case 5:
                print("\n\n\t\t\t--- For disease and treatment\n\n")
            case 6:
                print("\n\n\t\t\t--- For talking to a doctor\n\n")
                talkToDoc()
            case 7:
                print("\n\n\t\t\t--- Exiting...\n\n")
                break
            case _:
                print("\n\n\t\t\t--- No such choice\n\n")

if __name__ == "__main__":
    main()
