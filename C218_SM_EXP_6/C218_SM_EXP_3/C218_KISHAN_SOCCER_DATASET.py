# -*- coding: utf-8 -*-
"""KISHAN_SINGH_SOCCER_DATASET.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8_QM_dI0YmbNeXIsqAX8tJ3cIQqplA0

*   KISHAN SINGH
*   C218 70532100045
"""

#C218 KISHAN SINGH
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression as slr

#C218 KISHAN SINGH
da=pd.read_csv('/content/WorldCups_C218.csv')
da

#C218 KISHAN SINGH
da.shape

da.head()  #C218 KISHAN SINGH

#C218 KISHAN SINGH
data = da.loc[:,('Year','Country', 'Winner', 'Runners-Up','GoalsScored','QualifiedTeams','MatchesPlayed','Attendance')]
data.head()

#C218 KISHAN SINGH
data.info()

#C218 KISHAN SINGH
duplicateRowsDF = data[data.duplicated()]
duplicateRowsDF

# Check for missing data
data.isnull().sum()  #C218 KISHAN SINGH

# Drop the missing values
data.dropna(inplace = True)  #C218 KISHAN SINGH

#Dataset after missing values are dropped
data.shape  #C218 KISHAN SINGH

data.columns = ['Year','Country','Winner','Runners-Up', 'GoalsScored','QualifiedTeams','MatchesPlayed','Attendance']

data.head()

data.drop('Attendance',axis=1)

numerical = ['GoalsScored','QualifiedTeams','MatchesPlayed','Attendance']
data[numerical].describe()

fig, axs = plt.subplots(2,2, figsize=(15, 10))  #C218 KISHAN SINGH
sns.histplot(data= data, x="GoalsScored", kde=True, color="red", ax=axs[0,0])
sns.histplot(data= data, x="QualifiedTeams", kde=True, color="skyblue", ax=axs[0,1])
sns.histplot(data= data, x="MatchesPlayed", kde=True, color="olive", ax=axs[1,0])
sns.histplot(data= data, x="Attendance", kde=True, color="gold", ax=axs[1,1])
plt.show()

fig, axs = plt.subplots(2,2, figsize=(15,8))  #C218 KISHAN SINGH
sns.boxplot(data['GoalsScored'], ax = axs[0,0])
sns.boxplot(data['QualifiedTeams'], ax = axs[0,1])
sns.boxplot(data['MatchesPlayed'], ax = axs[1,0])

qh25, qh50, qh75 = np.percentile(data['MatchesPlayed'], [25,50,75])  #C218 KISHAN SINGH
iqrh = qh75-qh25
minh = qh25 - 1.5*iqrh
maxh = qh75 + 1.5*iqrh
data = data[(data['MatchesPlayed'] > minh) & (data['MatchesPlayed'] < maxh)]
maxh

qw25, qw50, qw75 = np.percentile(data['QualifiedTeams'], [25,50,75])  #C218 KISHAN SINGH
iqrw = qw75-qw25
maxw = qh75 + 1.5*iqrw
data = data[data['QualifiedTeams'] < maxw]
maxw

qb25, qb50, qb75 = np.percentile(data['GoalsScored'], [25,50,75])  #C218 KISHAN SINGH
iqrb = qb75-qb25
maxb = qb75 + 1.5*iqrb
data = data[data['GoalsScored'] < maxb]
maxb

data.shape  #C218 KISHAN SINGH

fig, axs = plt.subplots(1,3, figsize=(15, 5))  #C218 KISHAN SINGH
sns.histplot(data= data, x="GoalsScored", kde=True, color="skyblue", ax=axs[0])
sns.histplot(data= data, x="MatchesPlayed", kde=True, color="olive", ax=axs[1])
sns.histplot(data= data, x="QualifiedTeams", kde=True, color="gold", ax=axs[2])
plt.show()

fig, axs = plt.subplots(1,3, figsize=(17, 4))  #C218 KISHAN SINGH
sns.boxplot(data['GoalsScored'], ax = axs[0])
sns.boxplot(data['MatchesPlayed'], ax = axs[1])
sns.boxplot(data['QualifiedTeams'], ax = axs[2])
plt.show()

"""Feature Engineering

One Hot Encoding
"""

data['Winner'] = data.Winner.replace({1 : 'Uruguay', 2 : 'Italy'})
data['Winner']

categorical = data[['GoalsScored','MatchesPlayed','QualifiedTeams']]  #C218 KISHAN SINGH
categorical.head()

dummy = pd.get_dummies(categorical,drop_first=True)  #C218 KISHAN SINGH
dummy

"""Log transform of skewed variables"""

numerical = data[['GoalsScored','MatchesPlayed','QualifiedTeams']] #C218 KISHAN SINGH
skew_limit = 0.75 
skew_vals = numerical.skew()
skew_vals

"""Pairplot Feature"""

sns.pairplot(data, plot_kws=dict(alpha=.1, edgecolor='none'))  #C218 KISHAN SINGH

sns.pairplot(data, hue = 'MatchesPlayed', palette = 'husl')  #C218 KISHAN SINGH

sns.pairplot(data, hue = 'QualifiedTeams', palette = 'Set2')  #C218 KISHAN SINGH

