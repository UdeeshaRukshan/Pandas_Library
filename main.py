import pandas as pd

# Creating a list of dictionaries
data = [
    {'Name': 'John', 'Age': 25, 'Gender': 'M', 'Country': 'USA'},
    {'Name': 'Alice', 'Age': 30, 'Gender': 'F', 'Country': 'Canada'},
    {'Name': 'Bob', 'Age': 35, 'Gender': 'M', 'Country': 'UK'},
    {'Name': 'Emily', 'Age': 27, 'Gender': 'F', 'Country': 'Australia'}
]

# Creating a DataFrame from the list of dictionaries
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)
print("----------")

print(df.head(1))
print("----------")

print(df.tail(1))
print("----------")

print(df.sample(3))
print("----------")

print(df.info())
print("----------")

print(df.describe())
print("----------")

print(df.columns)
print("----------")

print(df.shape)
print("----------")

print(df.dtypes)
print("----------")

df.insert(4,'Degree',['Computer science','Business studies','Art','Cyber security'])
print(df)

df.drop('Degree', axis=1, inplace=True)
print(df)


