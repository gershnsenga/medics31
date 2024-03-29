import welcome
import app_menu
import talk_to_doc 

def main():
    welcome.welcome()
    
    while True:
        app_menu.appMenu()

        choice = int(input("\t\t Your Choice :: "))

        if choice == 1:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 2:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 3:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 4:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 5:
            print("\n\n\t\t\t--- For widely spread diseases\n\n")
        elif choice == 6:
            print("\n\n\t\t\t--- Talk to a doctor.\n\n")
            talk_to_doc.talkToDoc()
        elif choice == 7:
            print("\n\n\t\t\t--- Exiting...\n\n")
            exit()
            break
        else:
            # print("\n\n\t\t\t--- For widely spread diseases\n\n")
            main()

        
            # case _:
            #     raise ValueError("No such choice")

        # match choice:
        #     case 1:
        #         print("--- For widely spread diseases\n")
        #         break
        #     case 2:
        #         print("--- For searching by diseases\n")
        #     case 3:
        #         print("--- For searching by gender\n")
        #     case 4:
        #         print("--- For widely spread diseases\n")
        #     case 5:
        #         print("--- For widely spread diseases\n")
        #     case 6:
        #         print("--- For widely spread diseases\n")
        #     case 7:
        #         print("--- Exit\n")
        #         break
        #     case _:
        #         raise ValueError("No such choice")
        

if __name__ == "__main__":
    main()