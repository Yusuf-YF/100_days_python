# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

# print welcome message
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

# calculating the tip percent.
tip_percent = tip / 100

# multiply the bill to the tip percent to get total bill.
total_tip = bill * tip_percent

# adding bill to the total tip to get total bill.
total_bill = bill + total_tip

# divide total bill to people.
bill_per_person = total_bill / people

# format the result to 2 decimal places.
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
