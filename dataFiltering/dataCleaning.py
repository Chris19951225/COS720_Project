import matplotlib.pyplot as plt



import seaborn as sns; sns.set_style('whitegrid')

import os, sys, email
import numpy as np
import pandas as pd

import json
import csv
from pymongo import MongoClient
import wordcloud

# Network analysis
import networkx as nx
#NLP
from nltk.tokenize.regexp import RegexpTokenizer

from subprocess import check_output


######################################################################### Helper methods
def get_text_from_email(msg):
    parts = []
    for part in msg.walk():
        if part.get_content_type() == 'text/plain':
            parts.append( part.get_payload())
    return ''.join(parts)


def split_email_addresses(line):
    if line:
        addrs = line.split(',')
        addrs = frozenset(map(lambda x: x.strip(), addrs))
    else:
        addrs = None
    return addrs


######################################################################### Read in csv. Will also be used later for reading in the filtered csv
emails_df = pd.read_csv('/home/hristian/Documents/enron/CSV/emails.csv')
print(emails_df.shape)
emails_df.head()

######################################################################### Set up the pandas dataframe object
messages = list(map(email.message_from_string, emails_df['message']))
emails_df.drop('message', axis=1, inplace=True)
# Get fields from parsed email objects
keys = messages[0].keys()
for key in keys:
    emails_df[key] = [doc[key] for doc in messages]
# Parse content from emails
emails_df['content'] = list(map(get_text_from_email, messages))
# Split multiple email addresses
emails_df['From'] = emails_df['From'].map(split_email_addresses)
emails_df['To'] = emails_df['To'].map(split_email_addresses)

# Extract the root of 'file' as 'user'
emails_df['user'] = emails_df['file'].map(lambda x:x.split('/')[0])
del messages

emails_df.head()

######################################################################### Show unfiltered data
print("########################################")
print('shape of the dataframe:', emails_df.shape)
# Find number of unique values in each columns
for col in emails_df.columns:
    print(col, emails_df[col].nunique())


######################################################################### This code is suppose to filter the sent folder (takes ages)

for i in range(250000):
    if "sent" in str(emails_df['file'][i]).lower():
        emails_df.drop(emails_df.index[i])
        print(i)

emails_df = emails_df.set_index('Message-ID')\
    .drop(['file', 'X-Folder', 'Mime-Version', 'Content-Type', 'Content-Transfer-Encoding', 'X-cc', 'X-bcc', 'content',
           'user', 'Date', 'X-FileName'], axis=1)

######################################################################### Show filtered data
print("########################################")
print('shape of the dataframe:', emails_df.shape)
# Find number of unique values in each columns
for col in emails_df.columns:
    print(col, emails_df[col].nunique())

######################################################################### Example on how you would access data
print("########################################")
print(emails_df['X-From'][0])

######################################################################### Write to a csv file
print("########################################")
emails_df.to_pickle('/home/hristian/Documents/enron/CSV/filtered.pkl')
