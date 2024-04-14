from .db_connection import *

def search_by_disease(disease):    
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "SELECT * FROM disease WHERE disease_name = %s"
    cursor.execute(sql, (disease,))

    disease_found = cursor.fetchall()
    if disease_found:
        while True:
            print("\n\t\t\t\t\t\t|     1. Treatment")
            print("\t\t\t\t\t\t|     2. Back to main menu")

            try:
                choice = int(input("\n\t\t\t\t\t\t\t --- Which service now :: "))
                if choice == 1:
                    treatment_sql = "SELECT i.treatment FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
                    cursor.execute(treatment_sql, (disease,))
                    treatments = cursor.fetchall()

                    if treatments:
                        print(f"\n\n\t\t\t\t\t\t\t\t {disease.capitalize()} Treatment \n\t\t\t\t\t\t\t\t -----------")
                        for treatment in treatments:
                            print(f"\n\t\t\t\t\t\t\t\t | - {treatment[0]}")
                        print("\n")
                    else:
                        print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| No treatment information available.  | \n\t\t\t\t\t\t\t------------------------------\n")
                
                elif choice == 2:
                    break
                
                else:
                    print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Your choice is not valid.  | \n\t\t\t\t\t\t\t------------------------------\n")
            
            except ValueError:
                print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Please enter a valid number.  | \n\t\t\t\t\t\t\t------------------------------\n")
            
    else:
        print("\n\t No Such disease\n\t ------------\n")

    cursor.close()