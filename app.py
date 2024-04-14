from src.search_disease import *
from src.search_type import *
from src.search_gender import *
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
                print("\n\n\t\t\t--- For widely spread diseases\n\n")
            case 2:
                print("\n\t\t\t\t\t\t|     1. Get All types of diseases")
                print("\t\t\t\t\t\t|     2. Get diseases in a type           ")
                print("\t\t\t\t\t\t|     3. Back to main menu   ")

                typeObj = SearchByType()

                while True:
                    typeChoice = int(input("\n\n\t\t\t\t\t-- What you want : "))
                    match typeChoice:
                        case 1:
                            typeObj.getTypes()
                        case 2: 
                            typeObj.getTypeDiseases()
                        case 3:
                            break
                        case _:
                            print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Your choice is not valid.  | \n\t\t\t\t\t\t\t------------------------------\n")
                        
            case 3:
                print("\n\n\t\t\t--- For search by gender\n\n")
                search_by_gender_menu()
            case 4:
                print("\n\n\t\t\t--- For disease and prevention\n\n")
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
