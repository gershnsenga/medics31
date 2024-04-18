from .db_connection import *

class SearchByType:

    def __init__(self):
        pass

    # methods
    def getTypes(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        sql = 'SELECT * FROM type'
        cursor.execute(sql)
        
        print("\n\n\t\t\t\t\t All Types \n\t\t\t\t\t -----------")
        rows = cursor.fetchall()
        for row in rows:
            print(f"\n\t\t\t\t\t | - {row[1]}")
            cursor.close()

    # get diseases from any type
    def getTypeDiseases(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        typeInput = str(input("\n\t\t\t\tWhat type : "))

        sql = "SELECT * FROM type WHERE type_name LIKE %s"
        cursor.execute(sql, ('%' + typeInput + '%',))

        result = cursor.fetchone()

        if result is None:
            print("\n\n\t\t\t\t\t\t------------------------ \n\t\t\t\t\t\t| No such type found    |\n\t\t\t\t\t\t------------------------\n\n")
        else:
            main_sql = "SELECT disease.disease_name FROM disease JOIN disease_type ON disease.id = disease_type.disease_id WHERE disease_type.type_id=%s"
            cursor.execute(main_sql, (result[0],))

            print(f"\n\n\t\t\t\t\t {result[1]} diseases \n\t\t\t\t\t -----------")
            for row in cursor.fetchall():
                print("\n\t\t\t\t\t\t|- {}".format(row[0]))
            cursor.close()