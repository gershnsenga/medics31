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

        sql = 'SELECT * FROM type WHERE type_name= %s'
        cursor.execute(sql, (typeInput,))

        id, type_name = cursor.fetchone()

        main_sql = "SELECT disease.disease_name FROM disease JOIN disease_type ON disease.id = disease_type.disease_id where disease_type.type_id=%s"
        cursor.execute(main_sql, (id,))

        print("\n\n\t\t\t\t\t {} diseases \n\t\t\t\t\t -----------".format(type_name))
        for row in cursor.fetchall():
            print("\n\t\t\t\t\t\t|- {}".format(row[0]))
        cursor.close()


















# def search_by_type(disease):    
#     connection = connect_to_database()
#     cursor = connection.cursor()

#     sql = "SELECT * FROM disease WHERE disease_name = %s"
#     cursor.execute(sql, (disease,))

#     if(len(cursor.fetchall()) > 0): 
#         print("\n\t\t\t\t\t\t|     1. Preventive measures")
#         print("\t\t\t\t\t\t|     2. Treatment           ")
#         print("\t\t\t\t\t\t|     3. Back to main menu   ")

#         while True:
#             whatNow = int(input("\n\t\t\t\t\t\t\t --- Which service now :: "))

#             match whatNow:
#                 case 1:
#                     results = "SELECT d.disease_name, i.preventions FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
#                     cursor.execute(results, (disease,))

#                     rows = cursor.fetchall()
#                     print("\n\n\t\t\t\t\t\t\t\t {} Preventions\n\t\t\t\t\t\t\t\t -----------".format(disease))
#                     for row in rows:
#                         disease_name, prevention = row
#                         print(f"\n\t\t\t\t\t\t\t\t | - {prevention}")
                    
#                     print("\n")
                    
#                 case 2:
#                     results = "SELECT d.disease_name, i.preventions FROM disease d INNER JOIN disease_info i on d.id=i.disease_id WHERE d.disease_name = %s"
#                     cursor.execute(results, (disease,))

#                     rows = cursor.fetchall()
#                     print("\n\n\t\t\t\t\t\t\t\t {} Treatment \n\t\t\t\t\t\t\t\t -----------".format(disease))
#                     for row in rows:
#                         disease_name, treatment = row
#                         print(f"\n\t\t\t\t\t\t\t\t | - {treatment}")
                    
#                     print("\n")
#                 case 3:
#                     break
#                 case _:
#                     print("\n\t\t\t\t\t\t\t------------------------------\n\t\t\t\t\t\t\t| Your choice is not valid.  | \n\t\t\t\t\t\t\t------------------------------\n")
#     else:
#         print("\n\t No Such disease\n\t ------------\n")

#     cursor.close()