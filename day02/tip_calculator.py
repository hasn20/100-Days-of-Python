# Welcome message
print("Welcome to the tip calculator.")

# Input for the total bill
total_bill = input("What was the total bill? $ ")

# Input for the tip percentage
per_tip = input("What percentage tip would you like to give? ")

# Input for the number of people
people = input("How many people to split the bill? ")

# Convert input values to float
f_total_bill = float(total_bill)
f_per_tip = float(per_tip) / 100.0 + 1.0  # Convert percentage to a multiplier
f_people = float(people)

# Calculate the amount each person should pay
each_p_bill = f_total_bill / f_people * f_per_tip

# Format the result to 2 decimal places
each_p_bill_f = ("{:.2f}".format(each_p_bill))

# Print the result
print(f"Each person should pay: ${each_p_bill_f}")
