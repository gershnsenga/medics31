from .db_connection import *

class DiseaseGenderSearch:
    def __init__(self):
        pass

    def search_by_gender_menu(self):
        while True:
            print("\n\n\t\t\t\t\tSearch by gender most affected:\n")
            print("\t\t\t\t\t\tOption 1: Male")
            print("\t\t\t\t\t\tOption 2: Female")
            print("\t\t\t\t\t\tOption 3: Back to main menu")

            choice = input("\n\t\t\t\t\t\t---Select an option: ")

            if choice == "1":
                self.search_by_gender("Male") 
            elif choice == "2":
                self.search_by_gender("Female")
            elif choice == "3":
                break
            else:
                print("\nInvalid choice. Please try again.")

    def search_by_gender(self, gender):
        connection = connect_to_database()
        cursor = connection.cursor()

        sql = "SELECT d.disease_name, di.preventions, di.treatment FROM disease d INNER JOIN disease_info di ON d.id = di.disease_id INNER JOIN disease_gender dg ON d.id = dg.disease_id INNER JOIN gender g ON dg.gender_id = g.id WHERE g.gender_name = %s"
        cursor.execute(sql, (gender,))
        diseases = cursor.fetchall()

        if diseases:
            print(f"\n\t\t\t\t\t\t\t LIST OF DISEASES MOSTLY AFFECTED BY THIS GENDER")
            for index, disease in enumerate(diseases, start=1):
                print(f"\n\t\t\t\t\t\t\tDisease {index}: {disease[0]}")
                print(f"\t\t\t\t\t\t\t\tPreventive measures: {disease[1]}")
        else:
            print(f"\n\t\t\t\t\t\tNo diseases found for {gender}.")

        cursor.close()
