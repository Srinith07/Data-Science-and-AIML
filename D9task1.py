import pandas as pd
products = pd.Series(
    data=[700, 150, 300],
    index=['Laptop', 'Mouse', 'Keyboard']
)
print("Full Product Price List:")
print(products)
laptop_price = products.loc['Laptop']
print("\nPrice of Laptop (Label-based indexing):")
print(laptop_price)
first_two = products.iloc[0:2]
print("\nFirst Two Products (Positional indexing):")
print(first_two)
