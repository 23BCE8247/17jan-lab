def calculate_money_needed(cost_of_trip, proportions, total_students):
    year_prices = [12, 10, 7, 5]  # Prices for each year
    total_money_raised = 0

    for i, proportion in enumerate(proportions):
        year_share = int(proportion) * total_students
        total_money_raised += year_share * year_prices[i]

    money_for_trip = total_money_raised * 0.5

    if money_for_trip >= cost_of_trip:
        return "The students have enough money for the school trip."
    else:
        needed_money = cost_of_trip - money_for_trip
        return f"The students need to raise ${needed_money:.2f} more for the school trip."


# Example usage:
cost_of_school_trip = float(input("Enter the cost of the school trip: $"))
proportions_input = input("Enter the proportion of students in each year (comma-separated): ")
proportions_list = [int(x) for x in proportions_input.split(',')]
total_students = int(input("Enter the total number of students: "))

result = calculate_money_needed(cost_of_school_trip, proportions_list, total_students)
print(result)