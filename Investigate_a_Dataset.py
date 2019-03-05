#!/usr/bin/env python
# coding: utf-8

# # TMDb Movie Data - What contributes to making a genre popular?
# 
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# 

# <a id='intro'></a>
# ## Introduction
# 
# > **What contributes to making a genre popular?** 
# This study uses the data set containing information from about 10,000 movies collected from The Movie Database (TMDb). This data set contains information on a list of movies including its popularity, adjusted budget, adjusted revenue, run time, release year, vote average and so on. This study evaluates how each of the factors listed in the previous sentence impacts
# the popularity of a movie's genre. Is there a correlation between each of these factors and the genre of the movie?

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# ### General Properties

# In[3]:


# Load data
df = pd.read_csv('tmdb-movies.csv')
pd.options.display.max_columns = None
display(df)


# In[4]:


# What is the shape of this data frame?
df.shape


# In[5]:


# Summary Statistics
df.info()


# 
# ### Data Cleaning

# In[6]:


# Only grab the columns that we want to analyze
df = df[["genres", "popularity", "vote_average", "runtime", "budget_adj", "revenue_adj", "release_year"]]
df


# In[7]:


# View missing value count for each feature.
df.isnull().sum()
# There is no missing data, so we don't need to drop any rows.


# In[8]:


# Show how many duplicate entries are in the dataset.
sum(df.duplicated())
# There aren't any duplicates, so we don't need to drop any.


# In[9]:


# Remove duplicates.
df.drop_duplicates()
sum(df.duplicated())


# In[10]:


# Remove rows with zero values.
df = df[(df != 0).all(1)]
df


# In[11]:


# There are multiple genre entries for each movie. Split these genre entries.
all_genres = df.join(df.genres
               .str.strip('|')
               .str.split('|',expand=True)
               .stack()
               .reset_index(level=1,drop=True)
               .rename('genre')).reset_index(drop=True)
all_genres


# In[12]:


# Group the mean adjusted budget by genre
genre_budget = all_genres.groupby('genre').budget_adj.mean()

# Group the mean popularity by genre
genre_popularity = all_genres.groupby('genre').popularity.mean()

# Group the mean runtime by genre
genre_runtime = all_genres.groupby('genre').runtime.mean()

# Group the mean release year by genre
genre_release_year = all_genres.groupby('genre').release_year.mean()

# Group the mean vote average by genre
genre_vote = all_genres.groupby('genre').vote_average.mean()

# Group the mean adjusted revenue by genre
genre_revenue = all_genres.groupby('genre').revenue_adj.mean()

# Combine all of the new data into one dataframe
genre_data = pd.concat([genre_budget, genre_popularity, genre_revenue, genre_runtime, genre_release_year, genre_vote], axis=1)  # Combine data frame based on indexes (genre)
genre_data


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# 
# 
# ### What contributes to making a movie genre popular?
# 
# 

# In[13]:


d = genre_data.reset_index()


# ### **Part 1**: Average Popularity of Genres

# In[14]:


# Average popularity of genres
g = sns.barplot(data=d, x="genre", y="popularity")
g.set_xticklabels(g.get_xticklabels(), rotation=90)
ax = plt.gca()
ax.set_title("Average Popularity of Genres")
plt.xlabel("Genre")
plt.ylabel("Popularity")


# Science fiction was the most popular genre and foreign was the least popular genre.

# In[15]:


# List of data to show genre popularity ranking
genre_data.sort_values('popularity', ascending=False).popularity


# In[16]:


d.popularity.hist(figsize=[8, 5], bins=8)
plt.title('Distribution of Popularity')
plt.xlabel('Popularity')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring popularity score for movie genres is approximately between 0.8 and 1.25.

# ### Part 2: Average Adjusted Budget of Genres vs Average Popularity of Genres

# In[17]:


# Average adjusted budget of genres vs average popularity of genres
g = sns.lmplot(data=d, x="budget_adj", y="popularity", hue="genre", fit_reg=False)  # Draw points as separate data without line of fit
sns.regplot(data=d, x="budget_adj", y="popularity", scatter=False, ax=g.axes[0, 0], ci=None)  # Draw line of fit to all points
ax = plt.gca()
ax.set_title("Average Adjusted Budget of Genres vs Average Popularity of Genres")
plt.xlabel("Adjusted Budget")
plt.ylabel("Popularity")


# There seems to be a positive correlation between the average budget of a genre and the popularity of that genre. In general, the higher the budget, the more popular the genre. On average, animation movies have the highest budget. The most popular genre was science fiction. 

# In[18]:


d.budget_adj.hist(figsize=[8,5], bins=6)
plt.title('Distribution of Adjusted Budget')
plt.xlabel('Adjusted Budget')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring adjusted budget for movie genres is approximately between 3.1e^7 and 4.4e^7.

# ### Part 3: Average Adjusted Revenue of Genres vs Average Popularity of Genres

# In[19]:


# Average adjusted revenue of genres vs average popularity of genres
g = sns.lmplot(data=d, x="revenue_adj", y="popularity", hue="genre", fit_reg=False)  # Draw points as separate data without line of fit
sns.regplot(data=d, x="revenue_adj", y="popularity", scatter=False, ax=g.axes[0, 0], ci=None)  # Draw line of fit to all points
ax = plt.gca()
ax.set_title("Average Adjusted Revenue of Genres vs Average Popularity of Genres")
plt.xlabel("Adjusted Revenue")
plt.ylabel("Popularity")


# There was also a positive correlation between the average adjusted revenue of a genre and the popularity of that genre. That is to say, the more revenue a genre generates, the more popular the genre is. Animation movies had the highest revenue on average.

# In[20]:


d.revenue_adj.hist(figsize=[8, 5], bins=6)
plt.title('Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring revenue for movie genres is approximately between 1.1e^8 and 1.5e^7.

# ### Part 4: Average Release Year of Genres vs Average Popularity of Genres

# In[21]:


# Average release year of genres vs average popularity of genres
g = sns.lmplot(data=d, x="release_year", y="popularity", hue="genre", fit_reg=False)  # Draw points as separate data without line of fit
ax = plt.gca()
ax.set_title("Average Release Year of Genres vs Average Popularity of Genres")
plt.xlabel("Release Year")
plt.ylabel("Popularity")


# Overall, there appears to be no correlation between the average release year of a genre and the popularity of the genre. Documentaries were released more recently on average than other movie genres, however they are the third least popular.

# In[22]:


d.release_year.hist(figsize=[8, 5], bins=6)
plt.title('Distribution of Release Year')
plt.xlabel('Release Year')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring release year for movie genres is approximately between 2001 and 2003.

# ### Part 5: Average Runtime of Genres vs Average Popularity of Genres

# In[23]:


# Average runtime of genres vs average popularity of genres
g = sns.lmplot(data=d, x="runtime", y="popularity", hue="genre", fit_reg=False)  # Draw points as separate data without line of fit
ax = plt.gca()
ax.set_title("Average Runtime of Genres vs Average Popularity of Genres")
plt.xlabel("Runtime")
plt.ylabel("Popularity")


# There seems to be no correlation between the average runtime and the average popularity of a genre of movie. History movies have the longest runtimes on average.

# In[24]:


d.runtime.hist(figsize=[8, 5], bins=6)
plt.title('Distribution of Runtime')
plt.xlabel('Runtime')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring runtime for movie genres is approximately between 107 and 116.

# ### Part 6: Vote Average of Genres vs Average Popularity of Genres

# In[25]:


# Vote Average vs Average Popularity of Genres
g = sns.lmplot(data=d, x="vote_average", y="popularity", hue="genre", fit_reg=False)  # Draw points as separate data without line of fit  # Draw line of fit to all points
ax = plt.gca()
ax.set_title("Vote Average of Genres vs Average Popularity of Genres")
plt.xlabel("Vote Average")
plt.ylabel("Popularity")


# The highest voted movie genres don't seem to be the most popular genres. Documentaries were the third least popular movies, but had the highest average vote (6.7).

# In[26]:


d.vote_average.hist(figsize=[8, 5], bins=6)
plt.title('Distribution of Vote Average')
plt.xlabel('Vote Average')
plt.ylabel('Frequency of Occurence')


# The most frequently occuring vote budget for movie genres is approximately between 5.95 and 6.15.

# <a id='conclusions'></a>
# ## Conclusions
# There are many different factors that seem to correlate with the popularity of a genre, but from the limited data we have here, we cannot conclude what exactly causes a genre to be popular.
# 
# #### Factors that seem to contribute to making a genre popular:
# - Budget (positive correlation)
# - Revenue (positive correlation)
# 
# #### Factors that don't seem to contribute to making a genre popular:
# - Runtime (no correlation)
# - Vote average (no correlation)
# - Release year (no correlation)
# 
# #### The most popular genres ranked from most popular to least popular:
# 1. Science Fiction
# 2. Adventure
# 3. Fantasy
# 4. Animation
# 5. Action
# 6. Family
# 7. Thriller
# 8. War
# 9. Mystery
# 10. Western
# 11. Crime
# 12. Comedy
# 13. Drama
# 14. History
# 15. Romance
# 16. Music
# 17. Horror
# 18. Documentary
# 19. TV Movie
# 20. Foreign
# 
# #### Limitations:
# - We don't have data for every movie ever made.
# - Genre of movies may not be accurate.
# - Movies can have multiple genres, so each movie may not be a pure representation of those genres.
