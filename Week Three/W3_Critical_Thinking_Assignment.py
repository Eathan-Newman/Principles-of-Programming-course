sales_tax_ratio = 0.07
tip_18_ratio = 0.18

print("What is the cost of the food?", end=" ")
meal_cost = float(input())

tax_cost = sales_tax_ratio * meal_cost
tip_cost = tip_18_ratio * meal_cost
total_meal_cost = meal_cost + tax_cost + tip_cost

print("--- Meal Cost Breakdown ---")
print(f"Tax Total: ${tax_cost:.2f}")
print(f"18% Tip Total: ${tip_cost:.2f}")
print(f"Total Cost of Meal: ${total_meal_cost:.2f}")