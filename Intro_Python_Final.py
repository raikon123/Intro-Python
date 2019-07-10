# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Dataset day.xlsx description
# instant: record index
# dteday : date
# season : season (1:springer, 2:summer, 3:fall, 4:winter)
# yr : year (0: 2011, 1:2012)
# mnth : month ( 1 to 12)
# hr : hour (0 to 23)
# holiday : weather day is holiday or not (extracted from [Web Link])
# weekday : day of the week
# workingday : if day is neither weekend nor holiday is 1, otherwise is 0.
# weathersit : 
#  1: Clear, Few clouds, Partly cloudy, Partly cloudy
#  2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist
#  3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds
#  4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog
# temp : Normalized temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-8, t_max=+39 (only in hourly scale)
# atemp: Normalized feeling temperature in Celsius. The values are derived via (t-t_min)/(t_max-t_min), t_min=-16, t_max=+50 (only in hourly scale)
# hum: Normalized humidity. The values are divided to 100 (max)
# windspeed: Normalized wind speed. The values are divided to 67 (max)
# casual: count of casual users
# registered: count of registered users
# cnt: count of total rental bikes including both casual and registered

#Our goal is build a model to forecast cnt
#the TARGET is cnt
#the poential predictors/features are: season, mnth, holiday, weathersit, atemp, hum, windspeed, casual,registered
#where the categorical predictors/feaures are: season, mnth, holiday, weathersit
#wher the continous predictors are: atemp, hum, windspeed, casual,registered

#step1: load the packages needed for modeling 
#hint: you need to load RandomForestRegressor instead of RandomForestClassifier since we are modeling continous target cnt

#from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestRegressor




#step 2 load the dataset 


#2.1. load day.xlsx file into memory using pandas
import os
os.getcwd()
os.chdir("Users\\apple\\Downloads")
import pandas as pd
import numpy as np
day= pd.read_excel(open('day-1.xlsx', 'rb'), sheetname='mydata')


#2.2 printout the variable names/column names
day.columns


#2.3 print out the size of the data
day.shape

#2.4 summarize the data set using info and describle functions
day.info()

#2.5 check missing values
import missingno as msno
msno.matrix(day)


#3 Seperate the predictors/featues by using categorical variables groups and continous variables groups.
#note that 
#the categorical predictors/feaures are: season, mnth, holiday, weathersit
#the continous predictors are: atemp, hum, windspeed, casual,registered

categ =  [ 'season','yr', 'mnth','holiday','weathersit']
conti = ['atemp','hum','windspeed','casual', 'registered']

# 4 using the loops graph the categorical and continous variables 
import matplotlib.pyplot as plt
import seaborn as sns
fig= plt.figure(figsize=(30,10))
for i in range (0,len(categ)):
    fig.add_subplot(4,4,i+1)
    sns.countplot(x=categ[i],data=day)
    
for y in conti:
    fig.add_subplot(4,4,i+2)
    sns.distplot(day[y].dropna())
    i+= 1

plt.show()
fig.clear()

#5: using loops countplot all the categrical variables except holiday and set hue= 'holiday'
fig1=plt.figure(figsize=(30,10))
i=1
for col in categ:
    if col != 'holiday':
        fig1.add_subplot(4,4,i)
        sns.countplot(x=col, data=day, hue='holiday');
        i +=1
    


#6: swarmplot x = atemp, y = cnt, hue = season
sns.swarmplot(x='atemp', y='cnt', data=day, hue='season')



#7: boxplot x = season, y = cnt
sns.boxplot(x='season', y='cnt', data=day)




# 8: correlations with the new features
# you need to drop instant,	dteday
#plot the heatmap of the correlation
corr = day.drop(['instant','dteday'], axis=1).corr()
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(corr, mask=mask, cmap=cmap, cbar_kws={"shrink": .5})







#9: set the Target to be cnt
#   set the features/predictors to be  'season', 'mnth', 'holiday', 'weathersit',
#           'atemp', 'hum', 'windspeed', 'casual','registered']
Target =  day.cnt
Features =day.drop(['instant', 'dteday', 'yr', 'weekday', 'workingday', 'temp','cnt'],axis=1)

#10  Create training and test sets by seting test_size to be 20% and random_state =100
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(Features, Target, test_size = 0.2, random_state=100)

MlRes= {}
def MlResult(model,score):
    MlRes[model] = score
    print(MlRes)
    


#11  Create a random Forest regressor model instance  and set n_estimators = 1000
rfr = RandomForestRegressor(n_estimators = 100)



#11.1  Fit to the training data
rfr.fit(X_train, y_train)



#11.2  Predict on the test data: y_pred
y_pred = rfr.predict(X_test)

    
#11.3 print out  Score / Metrics
accuracy = rfr.score(X_test, y_test)
MlResult('Random Forest',accuracy)


#12 Rank the importance of the Features by using the follwing given function
from collections import OrderedDict
def FeaturesImportance(data,model):
    features = data.columns.tolist()
    fi = model.feature_importances_
    sorted_features = {}
    for feature, imp in zip(features, fi):
        sorted_features[feature] = round(imp,3)

    # sort the dictionnary by value
    sorted_features = OrderedDict(sorted(sorted_features.items(),reverse=True, key=lambda t: t[1]))

    #for feature, imp in sorted_features.items():
        #print(feature+" : ",imp)

    dfvi = pd.DataFrame(list(sorted_features.items()), columns=['Features', 'Importance'])
    #dfvi.head()
    plt.figure(figsize=(15, 5))
    sns.barplot(x='Features', y='Importance', data=dfvi);
    plt.xticks(rotation=90) 
    plt.show()
    return sorted_features
#12.1 Features importance
FeaturesImportance(day,rfr)


