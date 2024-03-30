def disease_and_prevention(disease_name):
    disease_prevention = {
        "Malaria": "Prevention: Use mosquito nets while sleeping, apply insect repellent, wear long-sleeved clothing, eliminate standing water around your home.",
        "Typhoid": "Prevention: Drink only bottled or boiled water, avoid raw fruits and vegetables, wash hands frequently.",
        "Influenza": "Prevention: Get vaccinated annually, practice good hand hygiene, cover your mouth when coughing or sneezing, avoid close contact with sick individuals.",
        "COVID-19": "Prevention: Get vaccinated when available, wear masks in public spaces, practice physical distancing, wash hands frequently, avoid large gatherings.",
        "Cholera": "Prevention: Drink only safe water, eat properly cooked food, avoid raw or undercooked seafood, wash hands frequently, use latrines or toilets properly.",
        "Diabetes": "Prevention: Maintain a healthy diet, engage in regular physical activity, avoid tobacco use, limit alcohol consumption, manage stress, get regular check-ups."
    }

    return disease_prevention.get(disease_name, "Prevention details not available for this disease.")

def main():
    print("Welcome to Disease and Prevention Menu:")
    print("Option 1: Malaria")
    print("Option 2: Typhoid")
    print("Option 3: Influenza")
    print("Option 4: COVID-19")
    print("Option 5: Cholera")
    print("Option 6: Diabetes")
    
    choice = input("Enter your choice (1-6): ")

    if choice in ["1", "2", "3", "4", "5", "6"]:
        disease_names = ["Malaria", "Typhoid", "Influenza", "COVID-19", "Cholera", "Diabetes"]
        chosen_disease = disease_names[int(choice) - 1]
        print("You chose {}.".format(chosen_disease))
        print("Prevention details:")
        print(disease_and_prevention(chosen_disease))
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()

