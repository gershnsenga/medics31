import welcome
import app_menu

def main():
    welcome.welcome()
    
    while True:
        app_menu.appMenu()

        choice = int(input("\t\t Your Choice :: "))

        if choice == 1:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 2:
            print("\n\n\t\t\t--- for search by disease\n\n")
        elif choice == 3:
            print("\n\n\t\t\t--- For search by gender\n\n")
        elif choice == 4:
            print("\n\n\t\t\t--- For disease and prevention\n\n")
        elif choice == 5:
            print("\n\n\t\t\t--- For disease and treatment\n\n")
        elif choice == 6:
            print("\n\n\t\t\t--- For talking to a doctor\n\n")
        elif choice == 7:
            print("\n\n\t\t\t--- Exiting...\n\n")
            break
        else:
            print("\n\n\t\t\t--- No such choice\n\n")

if __name__ == "__main__":
    main()