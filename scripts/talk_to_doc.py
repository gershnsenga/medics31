# from .app_menu import *

# def talkToDoc():

#     print("\t|                      1) Dr. Nmesoma: General medicine                                |")
#     print("\t|                      2) Dr. Gershom : Internal medicine                                  |")
#     print("\t|                      3) Dr. L.J: General medicine                                  |")
#     print("\t|                      4) Dr. Tracy: Internal medicine                                  |")
#     print("\t|                      5) Dr. David Peter: General medicine                                  |")
#     print("\t|                      6) Dr. Jade: Internal medicine                                  |")
#     print("\t|                      7) back to main menu                                  |")

#     option = int(input("Select the doctor you want to speak with"))

#     while True:
#         if option == 1:
#             print("\n\n\t\t\t--- DR.1 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 2:
#             print("\n\n\t\t\t--- DR.2 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 3:
#             print("\n\n\t\t\t--- DR.3 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 4:
#             print("\n\n\t\t\t--- DR.4 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 5:
#             print("\n\n\t\t\t--- DR.5 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 6:
#             print("\n\n\t\t\t--- DR.6 BIO\n\n")
#             print("press 1 to go back to previous menu?")
#             print("press 2 to go back to main menu?")
#             choice = int(input(" "))
#             if choice == 1:
#                 talkToDoc()
#             elif choice == 2:
#                 appMenu()
#         elif option == 7:
#             # print("\n\n\t\t\t--- Exiting...\n\n")
#             # exit()
#             appMenu()
#         else:
#                 # print("\n\n\t\t\t--- For widely spread diseases\n\n")
#             talkToDoc()


from .app_menu import *

class Doctor:
    def __init__(self, name, specialization, bio):
        self.name = name
        self.specialization = specialization
        self.bio = bio

class DoctorMenu:
    def __init__(self):
        self.doctors = [
            Doctor("Dr. Nmesoma", "General medicine", "BIO1"),
            Doctor("Dr. Gershom", "Internal medicine", "BIO2"),
            Doctor("Dr. L.J", "General medicine", "BIO3"),
            Doctor("Dr. Tracy", "Internal medicine", "BIO4"),
            Doctor("Dr. David Peter", "General medicine", "BIO5"),
            Doctor("Dr. Jade", "Internal medicine", "BIO6")
        ]

    def display_menu(self):
        print("\t|                      1) Dr. Nmesoma: General medicine                                      |")
        print("\t|                      2) Dr. Gershom : Internal medicine                                    |")
        print("\t|                      3) Dr. L.J: General medicine                                          |")
        print("\t|                      4) Dr. Tracy: Internal medicine                                       |")
        print("\t|                      5) Dr. David Peter: General medicine                                  |")
        print("\t|                      6) Dr. Jade: Internal medicine                                        |")
        print("\t|                      7) back to main menu                                                  |")

    def talk_to_doctor(self):
        self.display_menu()
        option = int(input("\n\t\t\t\t\t\tSelect the doctor you want to speak with: "))
        if 1 <= option <= len(self.doctors):
            doctor = self.doctors[option - 1]
            print(f"\n\n\t\t\t--- {doctor.name} \n\n")
            print("\n\n\t\t\t\t  -- Desc : Meet Doctor Gershom, a specialist in Dental therapy. For more information, use the contacts \n\t\t\t\t\tbelow to get in touch with him.\n")
            print("\n\t\t\t\t\t  -- Tel : +250 783 563 849 ")
            print("\n\t\t\t\t\t  -- Hospital :  King Faisal \ns")
            choice = int(input("press 1 to go back to previous menu or 2 to go back to main menu: "))
            if choice == 1:
                self.talk_to_doctor()
            elif choice == 2:
                AppMenu().display_menu()
        elif option == 7:
            AppMenu().display_menu()
        else:
            self.talk_to_doctor()

# Assuming appMenu() is a function in app_menu module
# You might need to adjust this depending on the actual structure
# If appMenu is a method in the same class, you can simply call it.