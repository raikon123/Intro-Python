# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd #handle data frame (tabluar data)
import numpy as np#handle matrix

#load Excel workbook into memery
#first step, we need to specify the directory
# Import `os` operating system
import os

# Retrieve Current Working Directory (`cwd`)
cwd = os.getcwd()
cwd

# Change directory to the file directory
os.chdir("C:\\Users\\saints.MARYVILLE\\Downloads")
cwd = os.getcwd()
cwd
#Load data into memory
#this is the recommended method
#open the file for reading only
#r means read; b means binary
#good practice to specify the worksheet by name
df = pd.read_excel(open('day.xlsx','rb'), 
    sheetname='mydata')
#determien the number rows or columns in the data
df.shape
# or using sheet index starting 0
#it is a bad practice
df = pd.read_excel(open('day.xlsx','rb'), 
     sheetname=0)
df.head()
#subset
#select all rows such that cnt>1000
df[df.cnt>1000]
#we select all rows and columns cnt, temp
df.loc[:, ['cnt', 'temp']]
#select rows such that temp> 70, and 
#columns  from atemp	to	cnt
df.loc[df.temp<70, 'atemp':'cnt']

#add new column
df['ratio'] = df['registered']/df['cnt']
df.head()

#save Data frame to Excel file
# DF TO EXCEL
#pd.ExcelWriter(filetosave)
writer = pd.ExcelWriter('daynew.xlsx')
#specify worksheetname;in most cases set 
#set row index to False
df.to_excel(writer,'mydaysheet', index=False)
#save the data to disk file
writer.save()
#load the Excel work book House.Data.xlsx into memory
#step 1: set the directory to the file to read
os.chdir("C:\\Users\\saints.MARYVILLE\\Downloads")
#step 2: read the file
df = pd.read_excel(open('House.Data.xlsx','rb'), 
    sheetname='kc_house_data')
#select a subset such that all rows
#with bedrooms == 3  and 
#columns  from yr_renovated	 to sqft_lot15
df.loc[df.bedrooms == 3, 'yr_renovated':'sqft_lot15']

#grade		yr_built	zipcode
df.loc[df.bedrooms == 3, ['grade',		'yr_built',	'zipcode' ]]

#create a new column 
#ratio = sqft_living15	/sqft_lot15
df['ratio'] = df['sqft_living15']/df['sqft_lot15']
#Finally save the data frame to 
#Excel workbook houseratio.xlsx
writer = pd.ExcelWriter('houseratio.xlsx')
#specify worksheetname;in most cases set 
#set row index to False
df.to_excel(writer,'newdata', index=False)
#save the data to disk file
writer.save()
#optional topics: Python and SQL
#Goal: count the number of email you received 
#from different users
import sqlite3
#connect to the database
conn = sqlite3.connect('emaildb.sqlite')
#use cursor to access database
#similar concept room key:
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (email TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
#when we read a file, it read line by line
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count FROM Counts WHERE email = ? ', (email,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (email, count)
                VALUES (?, 1)''', (email,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE email = ?',
                    (email,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
