import pickle
import numpy as np
import pandas as pd

uniqueTo = 0
uniqueFrom = 0
uniqueOrigin = 0
uniqueName = 0

emails_df = pd.read_pickle('filtered.pkl')
print(emails_df.shape)

print('Columns: ', emails_df.columns)

print('#########################')
print('Describe Dataframe: ')
print(emails_df.describe())
print('#########################')
print('Transpose Dataframe: ')
print(emails_df.T)
print('#########################')

#unique to addresses
for i in emails_df['To'].unique():
    #    print(emails_df['X-To'].unique())
    uniqueTo += 1

print('unique to: ' + str(uniqueTo))

#unique from addresses
for i in emails_df['From'].unique():
    #    print(emails_df['X-To'].unique())
    # print(i)
    uniqueFrom += 1

print('unique From: ' + str(uniqueFrom))

#unique origins
for i in emails_df['X-Origin'].unique():
    #    print(emails_df['X-To'].unique())
    uniqueOrigin += 1

print('unique origin: ' + str(uniqueOrigin))

#unique from addresses
# print('Columns: ', emails_df.columns)

# for col in emails_df:
#    print(col, emails_df)

# print(emails_df[345677])