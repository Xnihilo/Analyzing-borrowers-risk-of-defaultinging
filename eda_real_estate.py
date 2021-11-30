#!/usr/bin/env python
# coding: utf-8

# ## Review
# 
# Hi Raymond. My name is Soslan. I'm reviewing your project. I've added all my comments to new cells with different coloring.
# 
# <div class="alert alert-success" role="alert">
#   If you did something great I'm using green color for my comment
# </div>
# 
# <div class="alert alert-warning" role="alert">
# If I want to give you advice or think that something can be improved, then I'll use yellow. This is an optional recommendation.
# </div>
# 
# <div class="alert alert-danger" role="alert">
#   If the topic requires some extra work so I can accept it then the color will be red
# </div>
# 
# You did correctly almost all the checkpoints in the project. Can you just spend extra time filling missed values? Because you just filled them without an explanation of your decision. Also as an advice, you can add some plots to make your project visually better and easier to read.
# 
# ---

# ## Review (2)
# 
# Thank you for update. I'm accepting your project. Goood luck with future learning.
# 
# ---

# # Research on apartment sales ads
# 
# You will have the data from a real estate agency. It is an archive of sales ads for realty in St. Petersburg, Russia, and the surrounding areas collected over the past few years. You’ll need to learn how to determine the market value of real estate properties. Your task is to define the parameters. This will make it possible to build an automated system that is capable of detecting anomalies and fraudulent activity.
# 
# There are two different types of data available for every apartment for sale. The first type is a user’s input. The second type is received automatically based upon the map data. For example, the distance from the downtown area, airport, the nearest park or body of water. 

# ### Step 1. Open the data file and study the general information. 

# In[18]:


import pandas as pd
import numpy as np

apt_sales = pd.read_csv('/datasets/real_estate_data_eng.csv', sep='\t')
apt_sales.info()
apt_sales.head(5)


# In[19]:


display(apt_sales.tail(10))
"This is a last line"


# ### Conclusion

# The data has values that are missing that need to be dealt with before analysis can be done.

# <div class="alert alert-success" role="alert">
# Agree :)
# </div>

# ### Step 2. Data preprocessing

# In[20]:


#Fill the NaN values of these columns with 0
apt_sales['balcony'] = apt_sales['balcony'].fillna(0)
apt_sales['living_area'] = apt_sales['living_area'].fillna(0)
apt_sales['kitchen_area'] = apt_sales['kitchen_area'].fillna(0)
apt_sales['parks_around3000'] = apt_sales['parks_around3000'].fillna(0)
apt_sales['ponds_around3000'] = apt_sales['ponds_around3000'].fillna(0)
apt_sales['cityCenters_nearest'] = apt_sales['cityCenters_nearest'].fillna(0)


#Check if the missing data has been changed successfully
apt_sales.info()


# In[21]:


#Fill the NaN values of these columns with the avg amount of their respective columns
avg_ceil_height = apt_sales['ceiling_height'].mean()
apt_sales['ceiling_height'] = apt_sales['ceiling_height'].fillna(avg_ceil_height)

avg_airports_nearest = apt_sales['airports_nearest'].mean()
apt_sales['airports_nearest'] = apt_sales['airports_nearest'].fillna(avg_airports_nearest)

avg_parks_nearest = apt_sales['parks_nearest'].mean()
apt_sales['parks_nearest'] = apt_sales['parks_nearest'].fillna(avg_parks_nearest)

avg_ponds_nearest = apt_sales['ponds_nearest'].mean()
apt_sales['ponds_nearest'] = apt_sales['ponds_nearest'].fillna(avg_ponds_nearest)

avg_floors = apt_sales['floors_total'].mean()
apt_sales['floors_total'] = apt_sales['floors_total'].fillna(avg_floors)

#Check if the missing data has been changed successfully
apt_sales.info()


# Data might have been missing from the columns due to human error as it was input or maybe could've been due to different 
# formatting thus resulting in NaN values

# In[22]:


#Change data types of certain columns into int 
apt_sales['floors_total'] = apt_sales['floors_total'].astype('int')
apt_sales['balcony'] = apt_sales['balcony'].astype('int')


#Check if the changes went through
apt_sales.info()


#Data types were changed into int because the column data makes more sense as a whole number


# <div class="alert alert-danger" role="alert">
# You changed part of the missed data with 0s and part with means but you have to write a short explanation of why you decide to do so. 
# </div>

# I decided to change the missing values in balcony, living area, kitchen area, parks around 3000, ponds around 3000, and city centers nearest to 0 because I believe that these were due to human error as the data was entered into the spreadsheet.
# 
# I decided to change the missing values in ceiling height, airports nearest, parks nearest, ponds nearest, floors total to the average in their respective columns because there should be a value in those columns, but since they weren't in there initially, I chose to use the mean to best estimate the number that could be there.

# ### Step 3. Make calculations and add them to the table

# In[23]:


#The price per square meter
apt_sales['price_sq_meter'] = apt_sales['last_price'] / apt_sales['total_area']

#Check the new columns
apt_sales.head(5)


# In[24]:


#The day of the week, month, and year that the ad was published
apt_sales['first_day_exposition'] = pd.to_datetime(apt_sales['first_day_exposition'], format='%Y-%m-%dT%H:%M:%S')
apt_sales['day_of_week'] = apt_sales['first_day_exposition'].dt.day_name()
apt_sales['day'] = apt_sales['first_day_exposition'].dt.day
apt_sales['month_name'] = apt_sales['first_day_exposition'].dt.month_name()
apt_sales['month'] = apt_sales['first_day_exposition'].dt.month
apt_sales['year'] = apt_sales['first_day_exposition'].dt.year


#Check the new columns
apt_sales.head(5)


# In[25]:


#Location of floor in apartment
def floor_location(current, total):
    '''
    Checks the current floor of apartment room.
    '''
    if current == total:
        return 'last'
    elif current == 1:
        return 'first'
    else:
        return 'other'

apt_sales['current_floor'] = apt_sales.apply(lambda x: floor_location(x['floor'], x['floors_total']), axis=1)  

#Check the new columns
apt_sales.head(5)


# In[26]:


#Ratio between the living space and the total area
apt_sales['ratio_living_vs_total'] = apt_sales['living_area'] / apt_sales['total_area']

#Check the new columns
apt_sales.head(5)


# In[27]:


#Ratio between the kitchen space and the total area
apt_sales['ratio_kitchen_vs_total'] = apt_sales['kitchen_area'] / apt_sales['total_area']

#Check the new columns
apt_sales.head(5)


# <div class="alert alert-success" role="alert">
# All the calculations were done correctly
# </div>

# ### Step 4. Conduct exploratory data analysis and follow the instructions below:

# In[28]:


#Histogram of square area, price, number of rooms, and ceiling height
apt_sales.hist('total_area', bins=200, range=(0,500))
apt_sales.hist('rooms', bins=25, range=(0,15))
apt_sales.hist('last_price', bins=200, range=(0,30000000))
apt_sales.hist('ceiling_height', bins=30, range=(0,10))


# In[29]:


#Examine the time it's taken to sell the apartment and plot a histogram. 
apt_sales['days_exposition'].hist(bins=100, range=(0,1500))

#Calculate the mean and median and explain the average time it usually takes to complete a sale. 
avg_exp = apt_sales['days_exposition'].mean()
print('Average days to complete a sale:', avg_exp)

med_exp = apt_sales['days_exposition'].median()
print('Median days to complete a sale:', med_exp)

#When can a sale be considered to have happened rather quickly or taken an extra long time?
print(apt_sales['days_exposition'].describe())


# <div class="alert alert-success" role="alert">
# Good
# </div>

# After analyzing the data, I would consider any time that's shorter than 10 days to be too quick and 
# time longer than 800 days to be too long
# 

# In[30]:


#Remove rare and outlying values and describe the patterns you've discovered.
no_outliers = apt_sales.query('days_exposition < 800 & days_exposition > 10')
no_outliers['days_exposition'].hist(bins=100, range=(0,900))


# After removing the outliers, examining the histogram seems to reveal that most of the sales occur before 200 days

# In[31]:


#Which factors have had the biggest influence on an apartment’s price? 
#Examine whether the value depends on the total square area, number of rooms, floor (top or bottom), 
#or the proximity to the downtown area. 
print('Correlation btwn value and sq area:', apt_sales['last_price'].corr(apt_sales['total_area']))

print('Correlation btwn value and rooms:', apt_sales['last_price'].corr(apt_sales['rooms']))

print('Correlation btwn value and first floor:', apt_sales['last_price'].corr(apt_sales['current_floor']=='first'))

print('Correlation btwn value and last floor:', apt_sales['last_price'].corr(apt_sales['current_floor']=='last'))

print('Correlation btwn value and downtown:', apt_sales['last_price'].corr(apt_sales['cityCenters_nearest']))


# <div class="alert alert-warning" role="alert">
# Correct but some plot visualizing correlation would be nice here
# </div>

# Analyzing the correlations between the different variables show that the biggest influence on the apartment's price
# is the total sq area.

# In[32]:


#Also study the correlation to the publication date: day of the week, month, and year.
print('Correlation btwn value and day of week:', apt_sales['last_price'].corr(apt_sales['day']))

print('Correlation btwn value and month:', apt_sales['last_price'].corr(apt_sales['month']))

print('Correlation btwn value and year:', apt_sales['last_price'].corr(apt_sales['year']))

#Analyzing the correlation for the publication date shows that it doesn't affect the value of the apartment's price.


# In[33]:


#Select the 10 localities with the largest number of ads then calculate the average price per square meter in these localities. 
#Determine which ones have the highest and lowest housing prices. 
#You can find this data by name in the ’locality_name’ column.

top_10_names = apt_sales['locality_name'].value_counts().head(10).index
top_10 = apt_sales.query('locality_name in @top_10_names')
print(top_10.pivot_table(index='locality_name', values='price_sq_meter', aggfunc='mean'))


# After grouping the data into the top 10 localities and calculating the average price per sq meter, Saint Peterburg has 
# the highest housing prices while Vyborg has the lowest housing prices.

# In[34]:


#Thoroughly look at apartment offers: Each apartment has information about the distance to the city center. 
#Select apartments in Saint Petersburg (‘locality_name’). 
apt_in_petersburg = apt_sales.query('locality_name == "Saint Peterburg"')

#Your task is to pinpoint which area is considered to be downtown. 
#In order to do that, create a column with the distance to the city center in km and round to the nearest whole number. 
apt_in_petersburg['dist_in_km'] = (apt_in_petersburg['cityCenters_nearest'] / 1000).round()

#Next, calculate the average price for each kilometer and 
#plot a graph to display how prices are affected by the distance to the city center. 
#Find a place on the graph where it shifts significantly. That's the downtown border.
price_per_km = apt_in_petersburg.pivot_table(index='dist_in_km', values='price_sq_meter', aggfunc='mean')
price_per_km.plot(style='o-', grid=True, figsize=(15,6), xticks=np.arange(0,35,1))

#After analyzing the bar graph of the avg price for each km, the price shifts the most when it changes from 7km to 8km. 
#That is where the downtown border is located.


# <div class="alert alert-success" role="alert">
# Agree with you
# </div>

# In[25]:


#Select all the apartments in the downtown and examine correlations between the following parameters: 
#total area, price, number of rooms, ceiling height. 
downtown_apt = apt_in_petersburg.query('dist_in_km < 7')

print('Correlation btwn downtown and total area:', downtown_apt['dist_in_km'].corr(downtown_apt['total_area']))
print('Correlation btwn downtown and price:', downtown_apt['dist_in_km'].corr(downtown_apt['last_price']))
print('Correlation btwn downtown and number of rooms:', downtown_apt['dist_in_km'].corr(downtown_apt['rooms']))
print('Correlation btwn downtown and ceiling height:', downtown_apt['dist_in_km'].corr(downtown_apt['ceiling_height']))


#Also identify the factors that affect an apartment’s price: 
#number of rooms, floor, distance to the downtown area, and ad publication date. 
'''
factor_apt_price = downtown_apt.pivot_table(index=['rooms', 'floor', 'dist_in_km', 'first_day_exposition'],
                                            values='last_price',
                                           aggfunc = 'mean')
print(factor_apt_price)
'''
print('')
print('Correlation btwn price and rooms:', apt_in_petersburg['last_price'].corr(apt_in_petersburg['rooms']))
print('Correlation btwn price and floor:', apt_in_petersburg['last_price'].corr(apt_in_petersburg['floor']))
print('Correlation btwn price and distance:', apt_in_petersburg['last_price'].corr(apt_in_petersburg['dist_in_km']))
print('Correlation btwn price and ad publication date:', apt_in_petersburg['last_price'].corr(apt_in_petersburg['month']))

#Draw your conclusions. Are they different from the overall deductions about the entire city?


# After analyzing the data, it would seem that the number of rooms plays the largest part in the price of the apartment.
# The price doesn't seem to be too different from the entire city.

# <div class="alert alert-warning" role="alert">
# Correct but again some plot visualizing correlation would be nice here
# </div>

# ### Step 5. Overall conclusion

# After categorizing the data further and creating various graphs, most apartments are sold around 200 days abd the largest influence on the price of an apartment is the total sq area. A closer examination on the city of Saint Petersburg shows that 

# ### Project completion checklist
# 
# Mark the completed tasks with 'x'. Then press Shift+Enter.

# - [x]  file opened
# - [ ]  files explored (first rows printed, info() method)
# - [ ]  missing values determined
# - [ ]  missing values filled in
# - [ ]  clarification of the discovered missing values provided
# - [ ]  data types converted
# - [ ]  explanation of which columns had the data types changed and why
# - [ ]  calculated and added to the table: the price per square meter
# - [ ]  calculated and added to the table: the day of the week, month, and year that the ad was published
# - [ ]  calculated and added to the table: which floor the apartment is on (first, last, or other)
# - [ ]  calculated and added to the table: the ratio between the living space and the total area, as well as between the kitchen space and the total area
# - [ ]  the following parameters investigated: square area, price, number of rooms, and ceiling height
# - [ ]  histograms for each parameter created
# - [ ]  task completed: "Examine the time it's taken to sell the apartment and create a histogram. Calculate the mean and median and explain the average time it usually takes to complete a sale. When can a sale be considered extra quick or taken an extra slow?"
# - [ ]  task completed: "Remove rare and outlying values and describe the specific details you've discovered."
# - [ ]  task completed: "Which factors have had the biggest influence on an apartment’s value? Examine whether the value depends on price per meter, number of rooms, floor (top or bottom), or the proximity to the downtown area. Also study the correlation to the ad posting date: day of the week, month, and year. "Select the 10 places with the largest number of ads and then calculate the average price per square meter in these localities. Select the locations with the highest and lowest housing prices. You can find this data by name in the ’*locality_name’* column. "
# - [ ]  task completed: "Thoroughly look at apartment offers: each apartment has information about the distance to the downtown area. Select apartments in Saint Petersburg (*‘locality_name’*). Your task is to pinpoint which area is considered to be downtown. Create a column with the distance to the downtown area in km and round to the nearest whole number. Next, calculate the average price for each kilometer. Build a graph to display how prices are affected by the distance to the downtown area. Define the turning point where the graph significantly changes. This will indicate downtown. "
# - [ ]  task completed: "Select a segment of apartments in the downtown. Analyze this area and examine the following parameters: square area, price, number of rooms, ceiling height. Also identify the factors that affect an apartment’s price (number of rooms, floor, distance to the downtown area, and ad publication date). Draw your conclusions. Are they different from the overall conclusions about the entire city?"
# - [ ]  each stage has a conclusion
# - [ ]  overall conclusion drawn
