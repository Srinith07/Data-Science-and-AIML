total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share_per_person = total_bill / people
print(f"total bill:{total_bill},each person should pay:{share_per_person:.2f}")
