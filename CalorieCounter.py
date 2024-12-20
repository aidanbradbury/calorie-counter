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
                        calorie_goal=int(input("Enter Your daily calorie goal: ").strip())
                        f.write(f"{calorie_goal}\n")
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

def find_total_calories():
    #Reads calories entered by the user from a file, adds them up, and returns the total calories.
    try:
        total_calories = 0
        with open("CalorieCounter.csv", "r") as file:
            next(file)
                    
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 2: 
                    continue
                _, calories = parts
                try:
                    total_calories += int(calories) 
                except ValueError:
                    print(f"Invalid calorie value in line: {line.strip()}")
                    continue
        
        print(f"Total Calories Consumed: {total_calories}")
        return total_calories
    except FileNotFoundError:
        print(f"File '{"CalorieCounter.csv"}' not found. Make sure it exists and try again.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

def compare_calories(total_calories,calorie_goal):
    total_calories==find_total_calories
    calorie_goal==set_Goal
    #Compares calories entered to goal if one was set, and tells user if they met, missed, or exceeded their goal and by how much      
    try:
        with open("Goal.csv", "r") as f:
            next(f)
            goal_line = f.readline().strip()
            print(f"Goal File Contents:{goal_line}")
            if goal_line:
                calorie_goal = int(goal_line)
                print(f"Your calorie goal is: {calorie_goal}")
                difference=total_calories-calorie_goal
                if difference >0:
                    print(f"You exceeded your goal by {difference} calories.")
                if difference <0:
                    print(f"You did not meet your goal by {difference} calories.")
                if difference==0:
                    print("You met your goal exactly!")     
            else:
                print("No calorie goal set.")
    except FileNotFoundError:
        print("No goal file found. You can set a goal later.")
    
    



