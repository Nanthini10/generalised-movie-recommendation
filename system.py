'''A generalized recommendation model
based on the ratings and number of people
who saw the movie.
We only load up the dataset and sort them out
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date',
             'video release date','IMDb URL','unknown','Action',
             'Adventure','Animation','Childrens','Comedy','Crime',
             'Documentary','Drama','Fantasy','Film-Noir','Horror',
             'Musical','Mystery','Romance ','Sci-Fi','Thriller',
             'War' ,'Western']
user_cols = ['user id','age','gender','occupation','zip code']

#importing the data files onto dataframes
users = pd.read_csv('ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
item = pd.read_csv('ml-100k/u.item', sep='|',names=item_cols, encoding='latin-1')
data = pd.read_csv('ml-100k/u.data', sep='\t',names=data_cols, encoding='latin-1')

#Create one data frame from the three
dataset = pd.merge(pd.merge(item, data),users)
ratings_total = dataset.groupby('movie title').size()
ratings_mean = (dataset.groupby('movie title'))['movie title','rating'].mean()

#modify the dataframes so that we can merge the two
ratings_total = pd.DataFrame({'movie title':ratings_total.index, 'total ratings': ratings_total.values})
ratings_mean['movie title'] = ratings_mean.index

final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings',ascending= False)
final = final[:300].sort_values(by = 'rating',ascending = False)
print(final.head())
