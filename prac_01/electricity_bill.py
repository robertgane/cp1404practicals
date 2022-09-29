print("Electricity bill estimator")
price_per_kwh = float(input("Enter cents per kWh: "))
daily_use_kwh = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
estimated_bill = daily_use_kwh * (price_per_kwh / 100) * number_of_days
print(f"Estimated bill: ${estimated_bill:.2f}")
