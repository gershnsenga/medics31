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
        # self.doctors = [
        #     Doctor("Dr. Nmesoma", "General medicine", "BIO1"),
        #     Doctor("Dr. Gershom", "Internal medicine", "BIO2"),
        #     Doctor("Dr. L.J", "General medicine", "BIO3"),
        #     Doctor("Dr. Tracy", "Internal medicine", "BIO4"),
        #     Doctor("Dr. David Peter", "General medicine", "BIO5"),
        #     Doctor("Dr. Jade", "Internal medicine", "BIO6")
        # ]

    def display_doctors(self):
        print("\n\n\t\t List of Doctors\n")
        print("\t\t|         * Dr. Nmesoma: General medicine                  |")
        print("\t\t|         * Dr. Gershom : Internal medicine                |")
        print("\t\t|         * Dr. L.J: General medicine                      |")
        print("\t\t|         * Dr. Tracy: Internal medicine                   |")

    def talk_to_doctor(self):
        connection = connect_to_database()
        cursor = connection.cursor()

        while True:
            self.display_doctors()

            doctor_name = input("\n\t\t\t\t\t Type a doctor :: ")
            sql = 'SELECT * FROM doctor WHERE name LIKE %s'
            cursor.execute(sql, ('%' + doctor_name + '%',))

            result = cursor.fetchone()
            print(f"\n\n\t\t\t\t  -- Desc : {result[1]}\n")
            print(f"\n\t\t\t\t\t  -- Tel : {result[4]} ")
            print(f"\n\t\t\t\t\t  -- Email : {result[5]} ")
            print(f"\n\t\t\t\t\t  -- Hospital :  {result[6]} \n")

            back_to_menu = input("\n\t\t\t\t Press 'b' to go back to the main menu: ")
            if back_to_menu.lower() == 'b':
                break
