# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Movies
# ## What are the movies with the greatest rating difference that women prefer? Men prefer?

# <codecell>

#!head movie_data/users.dat 

# <codecell>

#!head movie_data/ratings.dat

# <codecell>

#!head movie_data/movies.dat

# <codecell>

import pandas as pd
import os

unames = ['user_id','gender','age','occupation','zip']
users = pd.read_table(os.path.join('movie_data','users.dat'), sep='::', header=None, names=unames)
print users.head()

# <codecell>

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(os.path.join('movie_data','ratings.dat'), sep='::', header=None, names=rnames)
print ratings.head()

# <codecell>

mnames = ['movie_id', 'title','genres']
movies = pd.read_table(os.path.join('movie_data','movies.dat'), sep='::', header=None, names=mnames)
print movies.head()

# <markdowncell>

# ##Merge
# Pandas has several ways to combine and merge data:
# 
# * merge: connect rows on one or more keys.  Think SQL.
# * concat: stacks objects along an axis
# * combine_first: overlapping data

# <codecell>

data = pd.merge(pd.merge(ratings, users), movies)
print data

# <markdowncell>

# ##Aggregation
# 
# * split objects
# * group by
# * pivot tables
# 
# ###Group by

# <codecell>

from IPython.core.display import Image
# From Python for Data Analysis, Wes McKinney
Image(filename='slides/groupby.png')

# <markdowncell>

# What is the highest rated movie?

# <codecell>

movies_by_rating = data.groupby(data['title']).mean()
movies_by_rating.head()

# <codecell>

movies_by_rating.sort_index(by='rating', ascending=False).head()

# <markdowncell>

# What's wrong with this?

# <codecell>

number_of_ratings = data.groupby('title').size()
number_of_ratings.head()

# <codecell>

high_ratings = movies_by_rating.ix[number_of_ratings > 1000]
high_ratings.head()

# <codecell>

high_ratings.sort_index(by='rating', ascending=False).head()

# <codecell>

ratings = data[['title','rating']]
ratings.head()



#grouped_size = data['rating'].groupby('title').size()
#grouped_rating = data['rating'].groupby('title').mean()

# <codecell>

group = ratings.groupby('title')
group.size().head()

# <codecell>

group.mean().head()

# <markdowncell>

# ##Pivot Tables
# 
# We would like to creat another data frame of our data that contains mean ratings with movie totals as row lables and gender as colunm lables.

# <codecell>

mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')
mean_ratings.head()

# <codecell>

mean_ratings

# <markdowncell>

# ##Group By
# Our table has 3706 rows.  Let's reduce that by only evaluating movies that have a certain number of ratings.
# 
# * size() is the number of observations
# * mean(), sum(), etc.

# <codecell>

ratings_by_title = data.groupby('title').size()
ratings_by_title.head()

# <codecell>

obj = ratings_by_title > 250
obj.index

# <codecell>

ratings_by_title[0:5]

# <codecell>

ratings_by_title.index[0:5]

# <codecell>

active_titles = ratings_by_title.index[ratings_by_title > 250]
active_titles[:10]

# <codecell>

mean_ratings = mean_ratings.ix[active_titles]
mean_ratings[:10]

# <codecell>

mean_ratings

# <markdowncell>

# We are now down to 1214 entries.

# <markdowncell>

# What are the top rated movies by women?

# <codecell>

top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]

# <codecell>

mean_ratings['diff'] = mean_ratings['F'] - mean_ratings['M']
mean_ratings[:10]

# <codecell>

sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[:10]

# <codecell>

sorted_by_diff = mean_ratings.sort_index(by='diff', ascending=False)
sorted_by_diff[:10]

# <codecell>


