print("How many years of rainfall would you like to submit?", end=" ")
num_years = int(input())
total_rainfall = 0.0 
total_months = 0

for year in range(1, num_years + 1):
    for month in range(1, 13):  
        print(f"Enter rainfall for Year {year}, Month {month}:", end=" ")
        monthly_rainfall = float(input())
        total_rainfall = total_rainfall + monthly_rainfall
        total_months = total_months + 1

average_rainfall = total_rainfall / total_months

print("--Rainfall Calculations--")
print(f"Total Months: {total_months}")
print(f"Total Rainfall: {total_rainfall:.2f} inches")
print(f"Average Monthly Rainfall: {average_rainfall:.2f} inches")
