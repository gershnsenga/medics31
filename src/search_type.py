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
            # id, type_name = row
            print(f"\n\t\t\t\t\t | - {row[1]}")
            cursor.close()

    # get diseases from any type
    def getTypeDiseases(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        typeInput = str(input("\n\t\t\t\tWhat type : "))

        sql = "SELECT * FROM type WHERE type_name= %s"
        cursor.execute(sql, (typeInput,))

        id, type_name = cursor.fetchone()

        main_sql = "SELECT disease.disease_name FROM disease JOIN disease_type ON disease.id = disease_type.disease_id where disease_type.type_id=%s"
        cursor.execute(main_sql, (id,))

        print("\n\n\t\t\t\t\t {} diseases \n\t\t\t\t\t -----------".format(type_name))
        for row in cursor.fetchall():
            print("\n\t\t\t\t\t\t|- {}".format(row[0]))
        cursor.close()