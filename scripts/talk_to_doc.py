from src.db_connection import *
from .app_menu import *

class Doctor:
    def __init__(self, name, phone, email, hospital, specialization, bio):
        self.name = name
        self.specialization = specialization
        self.bio = bio
        self.phone = phone
        self.email = email
        self.hospital = hospital

class DoctorMenu:
    def __init__(self):
        pass

    def display_doctors(self):
        print("\n\n\t\t List of Doctors\n")
        print("\t\t|         * Dr. John Smith                 |")
        print("\t\t|         * Dr. Emily Brown                |")
        print("\t\t|         * Dr. Michael Johnson            |")
        print("\t\t|         * Dr. David Williams             |")
        print("\t\t|         * Dr. Sarah Lee                  |")

    def talk_to_doctor(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        while True:
            self.display_doctors()

            doctor_name = input("\n\t\t\t\t\t Type a doctor :: ")

            sql = 'SELECT * FROM doctor WHERE name LIKE %s'
            cursor.execute(sql, ('%' + doctor_name + '%',))

            result = cursor.fetchone()
            if result is None:
                print("\n\n\t\t\t\t\t\t------------------------ \n\t\t\t\t\t\t| Doctor is not found    |\n\t\t\t\t\t\t------------------------\n\n")
            else:
                print(f"\n\n\t\t\t\t  -- Desc : {result[1]}\n")
                print(f"\n\t\t\t\t\t  -- Tel : {result[4]} ")
                print(f"\n\t\t\t\t\t  -- Email : {result[5]} ")
                print(f"\n\t\t\t\t\t  -- Hospital :  {result[6]} \n")

                back_to_menu = input("\n\t\t\t\t Do you want to continue(y/n): ")
                if back_to_menu.lower() == 'y':
                    continue
                else:
                    cursor.close()
                    break