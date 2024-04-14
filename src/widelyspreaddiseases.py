from .db_connection import *

class WidelySpreadDiseases:
    def __init__(self) -> None:
        pass

    def getDiseases(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        sql = "SELECT disease_name FROM disease WHERE is_widely=TRUE"
        cursor.execute(sql)

        print("\n\t\t\t\t\t\t Widely Spread diseases ::")
        for row in cursor.fetchall():
            print("\n\t\t\t\t\t\t\t|- {}".format(row[0]))

        print("\n\n\t\t\t\t\t\t--------------------------------------------------- \n\t\t\t\t\t\t| Need to do more? Main menu has a lot for you.    |\n\t\t\t\t\t\t---------------------------------------------------\n\n")
        cursor.close()