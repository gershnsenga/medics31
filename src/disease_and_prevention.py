from .db_connection import *

def disease_and_prevention(disease):
    connection = connect_to_database()
    cursor = connection.cursor()

    sql = "SELECT d.disease_name, i.preventions FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
    cursor.execute(sql, (disease,))

    rows = cursor.fetchall()

    if len(rows) > 0:
        print("\n\n\t\t\t\t {} Preventive Measures\n\t\t\t\t\t-------------".format(disease))
        for row in rows:
            disease_name, prevention = row
            print(f"\n\t\t | - {prevention}")
        
        print("\n")
        back_to_menu = input("\n\t\t\t Press 'b' to go back to the main menu: ")
        if back_to_menu.lower() == 'b':
            return
    else:
        print("\n\t No such disease found.\n")

    cursor.close()

