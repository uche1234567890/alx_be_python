# Prompt the user for financial details
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% interest
annual_savings = monthly_savings * 12
projected_annual_savings = annual_savings + (annual_savings * 0.05)

# Output results
print(f"Your monthly savings are: ${monthly_savings}")
print(f"Your projected annual savings after interest are: ${projected_annual_savings}")
