import os, sys, email
import numpy as np 
import pandas as pd

import json
import csv
from pymongo import MongoClient
# Plotting
#import plotly
#plotly.offline.init_notebook_mode()
#import plotly.graph_objs as go
import wordcloud

# Network analysis
import networkx as nx
# NLP
from nltk.tokenize.regexp import RegexpTokenizer

from subprocess import check_output

def dataAcquisition(filepath):
	#KAGGLE EMAIL ACQUISITION VERSION
	# emails_df = pd.read_csv('Enron/emails.csv') 
	# print(emails_df.shape)
	# emails_df.head()

	#This code takes the data from the csv file and puts it in the mongoDB database you make
	#Next : The following to do will be to put clean the data and this can be done by using the csv package from python and then basically only taking certain info we want.
	#download the csv file from : https://www.kaggle.com/roberttrankle/explore-enron/edit?unified=1
	print("hello")
	mongoclient = MongoClient('mongodb://localhost:27017/')
	mongoDB = mongoclient['Enron']
	collection_name = 'emails'
	db_cm = mongoDB[collection_name]
	cdir = os.path.dirname(__file__)
	file_res = os.path.join(cdir, filepath)

	data = pd.read_csv(file_res)
	data_json = json.loads(data.to_json(orient='records'))
	db_cm.remove()
	db_cm.insert(data_json)

if __name__ == '__main__':
    filepath = 'Enron/emails.csv'
    dataAcquisition(filepath)