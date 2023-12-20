print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n$"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
people = int(input("How many people to split the bill?\n"))

total_bill = bill + bill*tip/100
bill_per_person = total_bill/people
final_bill = round(bill_per_person, 2)
final_bill = "{:.2f}".format(bill_per_person)

print(f"Each person should pay: ${final_bill}")