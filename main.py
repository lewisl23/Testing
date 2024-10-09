

import pandas as pd

#load data from pokemon_data.csv
df = pd.read_csv('pokemon_data.csv')

#print(df.head(5))
#rint(df.tail(5))


#print the headers (columns)
print(df.columns)
print(df['Name'])
print(df[['Name','HP']])

#print the rows
print(df.head(4))
print(df.iloc[2,1])

#find data with Type equals to fire
print(df.loc[df['Type 1'] == 'Fire'])

#Sort the values using Type 1 and HP
print(df.sort_values(['Type 1', 'HP'], ascending = [1, 0]))


print(df.head(10))

#sum up the values using iloc and axis = 1 means add horizontally
# and axis = 0 means add verticaly
df['Total'] = df.iloc[:, 4:10].sum(axis = 1)

#edit the columns to move total to the front
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.iloc[5])

#save the file as a csv and removing the index
#df.to_csv('modified.csv', index=False)