import pandas as pd

marks = pd.Series([85, 90, 78], index=['A', 'B', 'C'])
print(marks)

mark = marks >= 80
print(mark)

filtered_marks = marks[mark]
print(filtered_marks)

marks[marks >= 90] = 70
print(marks)

data = pd.Series([10, None, 30, None])

print(data.isnull())
print(data.fillna(0))

data = pd.Series([10, None, 30, None])
print(data.dropna())

print(data.notnull())
