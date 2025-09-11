import locale
locale.setlocale(locale.LC_ALL, "English_United States.1252")

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses
annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

print("Your monthly savings are ", locale.currency(monthly_savings, grouping=True))
print("Projected savings after one year, with interest, is:", locale.currency(annual_savings, grouping=True))