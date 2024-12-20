if __name__=="__main__":
    from CalorieCounter import get_Info
    from CalorieCounter import set_Goal
    from CalorieCounter import find_total_calories
    from CalorieCounter import compare_calories
    get_Info()
    calorie_goal=set_Goal()
    total_calories=find_total_calories()
    compare_calories(total_calories,calorie_goal)