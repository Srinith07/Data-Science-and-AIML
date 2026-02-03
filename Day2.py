name = input("Enter your name: ")
age = int(input("Enter your age: "))
age += 4
print(f"Hello, {name}, You are {age} years old in 2030.")


total_bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
share_per_person = total_bill / people
print(f"total bill:{total_bill},each person should pay:{share_per_person:.2f}")

item_name = "Laptop"
quantity = 2
price = 499.99
in_stock = True
print("Item:", item_name, ", Qty:", quantity,
      ", Price:", price, ", Available:", in_stock)
total_cost = quantity * price
print("Total Cost:", total_cost)
