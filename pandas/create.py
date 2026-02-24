import pandas as pd


s = pd.Series([10, 20, 30, 40])
print(s)

marks = pd.Series([85, 90, 78], index=['Maths', 'Science', 'English'])
print(marks)

print(marks[0])

print(marks['Science'])

print(marks[['Maths', 'English']])

print(marks[0:2])
