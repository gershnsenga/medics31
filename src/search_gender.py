from .db_connection import *

def search_by_gender_menu():
    while True:
        print("\nSearch by gender most affected:")
        print("Option 1: Male")
        print("Option 2: Female")
        print("Option 3: Back to main menu")

        choice = input("\nSelect an option: ")

        if choice == "1":
            search_by_gender("Male") 
        elif choice == "2":
            search_by_gender("Female")
        elif choice == "3":
            break
        else:
            print("\nInvalid choice. Please try again.")

def search_by_gender(gender):
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "SELECT d.disease_name, di.preventions, di.treatment FROM disease d INNER JOIN disease_info di ON d.id = di.disease_id INNER JOIN disease_gender dg ON d.id = dg.disease_id INNER JOIN gender g ON dg.gender_id = g.id WHERE g.gender_name = %s"
    cursor.execute(sql, (gender,))
    diseases = cursor.fetchall()

    if diseases:
        for index, disease in enumerate(diseases, start=1):
            print(f"\nOption {index}: {disease[0]}")
            print(f"\tDescription: {disease[1]}")
            print("\tOption 1: Preventive measures")
            print("\tOption 2: Treatment")
            print("\tOption 3: Back to the previous menu")
            print("\tOption 4: Back to main menu")
    else:
        print(f"\nNo diseases found for {gender}.")

    cursor.close()
