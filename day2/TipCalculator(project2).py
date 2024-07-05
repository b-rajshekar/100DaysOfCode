# This line will print welcome message!

print("*********************************")
print("* Welcome to the Tip Calculator! *")
print("*********************************")


# This line stores the bill amount typed by the user
bill = float(input("What was the total bill? ₹"))

# This line stores the tip amount typed by the user
tip = int(input("How much tip would you like to give? 10, 12, 15 or nothing? "))

# This line stores the number of people typed by the user
people = int(input("How many people to split the bill? "))

tip_as_percent = tip / 100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ₹{final_amount}" )