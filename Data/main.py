import seaborn as sns; sns.set_style('whitegrid')

import os, sys, email
import numpy as np
import pandas as pd

import json
import csv
from pymongo import MongoClient
import wordcloud
import re

filename = 'fradulent_emails.txt'
file = open(filename, 'rt')
text = file.read()
file.close()
temp = ""
# split into words by white space
words = re.split(r'\n+', text)
for i in range(0, len(words)) :
	if("From r" in words[i] or "Return-Path:" in words[i] or "From:" in words[i] or "Reply-To" in words[i] or "To:" in words[i] or "Date:" in words[i] 
		or "Subject:" in words[i] or "X-Mailer:" in words[i]):
		temp += words[i] + '\n';

with open('phishingEmails.txt', 'a') as the_file:
	words = re.split(r'\WFrom r+', temp)
	for i in range(0, len(words)) :
		if(i == 0):
			the_file.write("phishingEmail: true" + '\n')
			the_file.write(words[i] + "\n\n")
		else :
			the_file.write("phishingEmail: true" + '\n')
			the_file.write("From r" + words[i] + "\n\n")