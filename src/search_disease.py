from .db_connection import *

def search_by_disease(disease):    
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "SELECT * FROM disease WHERE disease_name = %s"
    cursor.execute(sql, (disease,))

    if(len(cursor.fetchall()) > 0): 
        print("\n\t\t\t\t\t\t|     1. Preventive measures")
        print("\t\t\t\t\t\t|     2. Treatment           ")
        print("\t\t\t\t\t\t|     3. Back to main menu   ")

        while True:
            whatNow = int(input("\n\t\t\t\t\t\t\t --- Which service now :: "))
            if whatNow == 1:

                results = "SELECT d.disease_name, i.preventions FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
                cursor.execute(results, (disease,))

                rows = cursor.fetchall()
                print("\n\n\t\t\t\t\t\t\t\t {} Preventions\n\t\t\t\t\t\t\t\t -----------".format(disease))
                for row in rows:
                    disease_name, prevention = row
                    print(f"\n\t\t\t\t\t\t\t\t | - {prevention}")
                
                print("\n")
                
            elif whatNow == 2:
                results = "SELECT d.disease_name, i.preventions FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
                cursor.execute(results, (disease,))

                rows = cursor.fetchall()
                print("\n\n\t\t\t\t\t\t\t\t {} Treatment \n\t\t\t\t\t\t\t\t -----------".format(disease))
                for row in rows:
                    disease_name, treatment = row
                    print(f"\n\t\t\t\t\t\t\t\t | - {treatment}")
                
                print("\n")
            elif whatNow == 3:
                break
            else:
                print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Your choice is not valid.  | \n\t\t\t\t\t\t\t------------------------------\n")


    else:
        print("\n\t No Such disease\n\t ------------\n")

    cursor.close()