from src.search_type import *
from src.search_gender import *
from src.disease_and_prevention import *
from src.disease_and_treatment import *
from scripts.welcome import *
from scripts.app_menu import *
from scripts.talk_to_doc import DoctorMenu
from src.disease_and_treatment import *
from src.widelyspreaddiseases import *


def main():
    welcome()
    
    while True:
        appMenu()

        choice = int(input("\t\t\t --- Your Choice :: "))

        match choice:
            case 1:
                # getDisease()
                WidelySpreadDiseases().getDiseases()
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
                gender_search = DiseaseGenderSearch()
                gender_search.search_by_gender_menu()
            case 4:
                disease_name = input("\n\t\t\t\t\t Type a disease : ")
                disease_prevention = DiseasePrevention(disease_name)
                disease_prevention.get_preventions()
            case 5:
                disease_name = input("\n\t\t\t\t\t Type a disease : ")
                disease_treatment = DiseaseTreatment(disease_name)
                disease_treatment.get_treatment()
            case 6:
                print("\n\n\t\t\t--- For talking to a doctor\n\n")
                DoctorMenu().talk_to_doctor()  # Call the talk_to_doctor method of DoctorMenu
            case 7:
                print("\n\n\t\t\t--- Exiting...\n\n")
                break
            case _:
                print("\n\n\t\t\t--- No such choice\n\n")

if __name__ == "__main__":
    main()

