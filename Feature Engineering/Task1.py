import pandas as pd


data = {
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual', 'Automatic'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Red']
}

df = pd.DataFrame(data)
df['Transmission'] = df['Transmission'].map({'Manual': 0, 'Automatic': 1})
# One-Hot Encoding
df = pd.get_dummies(df, columns=['Color'], drop_first=True)
print(df)
