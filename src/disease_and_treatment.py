from .db_connection import *

class DiseaseTreatment:
    def __init__(self):
        pass

    def get_treatment(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        while True:
            disease_name = input("\n\t\t\t\t\t\t Type a disease : ")

            sql = "SELECT d.disease_name, i.treatment FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name LIKE %s"
            cursor.execute(sql, ('%' + disease_name + '%',))

            res = cursor.fetchall()
            if len(res) <= 0:
                print("\n\t\t\t\t\t No treatment measures found.\n")
            else:
                print(f"\n\n\t\t\t\t\t {res[0][0]} Treatment Measures\n\t\t\t\t\t------------------------------")
                for row in res:
                    print(f"\n\t\t\t\t\t | - {row[1]}")

                print("\n")
                back_to_menu = input("\n\t\t\t\t Do you want to continue(y/n): ")
                if back_to_menu.lower() == 'y':
                    continue
                else:
                    cursor.close()
                    break
