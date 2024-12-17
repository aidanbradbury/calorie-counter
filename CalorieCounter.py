def get_Info():
    # Allows the user to input the name of the food they ate and the calorie count,
    # then writes it to a CSV file.
    try:
        with open("CalorieCounter.csv", "a") as f:
            while True:
                user_input = input("Would you like to enter a food? (yes/no): ").lower().strip()
                if user_input == "yes":
                    food_name = input("Enter the name of the food: ").strip()
                    try:
                        cal_count = int(input("Enter the calorie count of the food: ").strip())
                        f.write(f"{food_name},{cal_count}\n")
                    except ValueError:
                        print("Invalid input. Please enter a numerical value for calories.")
                elif user_input == "no":
                    print("Exiting entry mode.")
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def set_Goal():
#Gives the user the option to set a daily calorie goal
    try:
        with open("Goal.csv","a") as f:
            while True:
                user_input = input("Would you like to set a calorie goal? (yes/no): ").lower().strip()
                if user_input=="yes":
                    try:
                        goal=int(input("Enter your daily calorie goal: ").strip())
                        f.write(f"{goal}\n")
                        print("Calorie Goal saved.")
                        break
                    except ValueError:
                        print("Invalid Input. Please enter a numerical value.") 
                elif user_input=="no":
                    print("Okay,let's just total your calories for the day then.")
                    break
                else:
                    print("Invalid input. Please type 'yes' or 'no'.")
    except Exception as e:
        print(f"An error occured: {e}")


if __name__=="__main__":
    get_Info()
    set_Goal()