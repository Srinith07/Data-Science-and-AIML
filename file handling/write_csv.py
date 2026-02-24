import csv


data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, "New York"],
    ['Bob', 25, "Los Angeles"],
    ['Charlie', 35, 'Chicago']
]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
