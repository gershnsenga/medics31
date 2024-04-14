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

