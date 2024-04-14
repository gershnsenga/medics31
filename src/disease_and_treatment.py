from .db_connection import *

def disease_and_treatment(disease):
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "SELECT * FROM disease WHERE disease_name = %s"
    cursor.execute(sql, (disease,))

    disease_found = cursor.fetchall()
    if disease_found:
        while True:
            try:
                results_sql = "SELECT d.disease_name, i.treatment FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
                cursor.execute(results_sql, (disease,))
                rows = cursor.fetchall()

                if rows:
                    print(f"\n\n\t\t\t\t {disease.capitalize()} Disease Treatment \n\t\t\t\t\t-------------")
                    for row in rows:
                        print(f"\n\t | - {row[1]}")
                    print("\n")
                else:
                    print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| No treatment information available.  | \n\t\t\t\t\t\t\t------------------------------\n")

                choice = input("\n\t\t\t --- Press 'm' to return to the main menu: ")
                if choice.lower() == 'm':
                    break
                else:
                    print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Invalid input.  | \n\t\t\t\t\t\t\t------------------------------\n")

            except Exception as e:
                print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| An error occurred: ", e, " | \n\t\t\t\t\t\t\t------------------------------\n")
                
    else:
        print("\n\t No such disease found.\n\t ------------\n")

    cursor.close()