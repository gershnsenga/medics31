n():
    
disease_prevention = {
     "Malaria": "Prevention: Use mosquito nets while sleeping, apply insect repellent, wear long-sleeved clothing, eliminate standing water around your home.",
     "Typhoid": "Prevention: Drink only bottled or boiled water, avoid raw fruits and vegetables, wash hands frequently.",
     "Influenza": "Prevention: Get vaccinated annually, practice good hand hygiene, cover your mouth when coughing or sneezing, avoid close contact with sick individuals.",
     "COVID-19": "Prevention: Get vaccinated when available, wear masks in public spaces, practice physical distancing, wash hands frequently, avoid large gatherings."
  
    
    
}

def main():
    print("Welcome to Disease and Prevention Menu:")
    print("Option 1: Malaria")
    print("Option 2: Typhoid")
    
    choice = input("Enter your choice (1-2): ")

    if choice == "1":
        print("You chose Malaria.")
        print("Prevention details:")
        print(disease_prevention["Malaria"])
    elif choice == "2":
        print("You chose Typhoid.")
        print("Prevention details:")
        print(disease_prevention["Typhoid"])
    elif choice == "3":
        print("You chose Influenza.")
        print("Prevention details:")
        print(disease_prevention["Influenza"])
    elif choice == "4":
        print("You chose COVID-19.")
        print("Prevention details:")
        print(disease_prevention["COVID-19"])
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
