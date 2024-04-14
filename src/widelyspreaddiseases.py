def getDisease():
    print("Most widely spread diseases")
    print("1: COVID")
    print("2: Malaria")
    print("3: Diabetes")
    print("4: Influenza")
    print("5: Common Cold")
    print("6: Exit")

     choice = input("Enter your choice: ")
    if choice == '1':
        disease_menu("COVID")
    elif choice == '2':
        disease_menu("Malaria")
    elif choice == '3':
        disease_menu("Diabetes")
    elif choice == '4':
        disease_menu("Influenza")
    elif choice == '5':
        disease_menu("Common Cold")
    elif choice == '6':
        exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()


def disease_menu(disease_name):
    print(f"\n{disease_name}")
    print("1: Description of the disease")
    print("2: Back to previous menu")
    print("3: Back to main menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        print("Descriptoion of the disease", disease_name)
    elif choice == '2':
        main_menu()
    elif choice == '3':
        exit()
    else:
        print("Invalid choice. Please try again.")
        disease_menu(disease_name)

if __name__ == "__main__":
    main_menu()