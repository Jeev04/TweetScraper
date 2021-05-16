#!/usr/bin/env python
# coding: utf-8

# In[1]:


import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data to
tweets_list1 = []
tweets_list2 = []
tweets_list3 = []
tweets_list4 = []
tweets_list5 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('need oxygen near: Jaipur within_time:3d').get_items()):
    if i>100:
        break
    tweets_list1.append([tweet.date, tweet.id, tweet.content, tweet.username])
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('need oxygen near: Delhi within_time:3d').get_items()):
    if i>100:
        break
    tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.username])
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('need oxygen near: Mumbai within_time:3d').get_items()):
    if i>100:
        break
    tweets_list3.append([tweet.date, tweet.id, tweet.content, tweet.username])
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('need oxygen near:  within_time:3d').get_items()):
    if i>100:
        break
    tweets_list4.append([tweet.date, tweet.id, tweet.content, tweet.username])
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('oxygen cylinder geocode:26.9048,75.7489,100km').get_items()):
    if i>50:
        break
    tweets_list5.append([tweet.date,tweet.id,tweet.content,tweet.username])
# Creating a dataframe from the tweets list above 
tweets_df1 = pd.DataFrame(tweets_list1, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])
from sqlalchemy import create_engine

# create sqlalchemy engine
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost/{db}"
                       .format(user="root",
                               pw="root",
                               db="ipproject"))
tweets_df1.to_sql('tweets', con = engine, if_exists = 'append', chunksize = 1000)
print(tweets_df1)


# In[62]:


w=len(tweets_list1)
x=len(tweets_list2)
y=len(tweets_list3)
z=len(tweets_list4)
total=x+y+z+w
perw=(w/total)*100
perx=(x/total)*100
pery=(y/total)*100
perz=(z/total)*100


# In[67]:


import matplotlib.pyplot as plt
#making a pie chart
labels = ['Jaipur','Delhi','Mumbai','Ahmedabad']
sizes=[w,x,y,z]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.06, 0.04, 0.04, 0.05)
plt.pie(sizes, explode=explode, labels=labels, colors=colors,autopct='%1.1f%%')
plt.axis('equal')
plt.show()
#making a graph
xpoints=['Jaipur','Delhi','Mumbai','Ahmedabad']
ypoints=[perw,perx,pery,perz]
plt.xlabel("Cities")
plt.ylabel("Percentage of Tweets")
plt.bar(xpoints, ypoints)
plt.title('Major Cities and Percentage of Tweets per Hour', fontsize=15)
plt.show()


# In[ ]:




