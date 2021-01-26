#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 12:19:30 2019

@author: johnguttag
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#change defaults for plotting
#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 20
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 20
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
#set numpoints for legend
plt.rcParams['legend.numpoints'] = 1
#set parameters for saving figures
plt.rcParams['savefig.dpi'] = 1000
# plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0

# # Code on page 512
# wwc = pd.read_csv('wwc2019_q-f.csv')
# print(wwc.to_string())

# # Code on page 513
# for i in wwc.index:
#     print(i)

# # Code on page 514   
# for c in wwc.columns:
#     print(c)
    
# print(wwc.values)

# # Code on page 515
# print(pd.DataFrame())

# rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
# print(pd.DataFrame(rounds))

# print(pd.DataFrame({'Round': rounds}))

# rounds = ['Semis', 'Semis', '3rd Place', 'Championship']
# teams = ['USA', 'Netherlands', 'Sweden', 'USA']
# df = pd.DataFrame({'Round': rounds, 'Winner': teams})
# print(df)
# 
# Code on page 516
# df['W Goals'] = [2, 1, 0, 0]
# print(df)

# df['W Goals'] = [2, 1, 2, 2]
# print(df)

# print(df.drop('Winner', axis = 'columns'))

# # Code on page 517
# quarters_dict = {'Round': ['Quarters']*4,
#                   'Winner': ['England', 'USA', 'Netherlands', 'Sweden'],
#                   'W Goals': [3, 2, 2, 2]}
# df = pd.concat([pd.DataFrame(quarters_dict), df], sort = False)
# print(df.to_string())

# print(pd.concat([pd.DataFrame(quarters_dict), df], sort = True).to_string())

# # Code on page 518
# print(df.reset_index(drop = True).to_string())

# print(df.set_index('Round').to_string())

# print(wwc['Winner'].to_string())

# # Code on page 519
# print(wwc['Winner'][3])

# winners = ''
# for w in wwc['Winner']:
#     winners += w + ','
# print(winners[:-1])

# print(wwc[['Winner', 'Loser']].to_string())

# # Code on page 520
# print(wwc[['Round','Winner','Loser','W Goals','L Goals']].to_string())

# print(wwc[1:2])

# print(wwc.loc[3])

# # Code on page 521
# print(wwc.loc[[1,3,5]])

# print(wwc.loc[3:7:2])

# print(wwc.loc[6:])

# # Code on page 522
# print(wwc.loc[:2])

# print(wwc.loc[0:2, 'Round':'L Goals':2])

# wwc_by_round = wwc.set_index('Round')
# print(wwc_by_round.to_string())

# # Code on page 523
# print(wwc_by_round.loc['Semis'])

# print(wwc_by_round.loc[['Semis', 'Championship']])

# print(wwc_by_round.loc['Quarters':'Semis':2])

# print(wwc_by_round.iloc[[1,2]])

# # Code on page 524
# grouped_by_round = wwc.groupby('Round')
# print(grouped_by_round.sum())

# print(wwc.groupby('Winner').mean())

# # Code on page 525
# print(wwc.groupby(['Loser', 'Round']).mean())

# print(wwc.loc[wwc['Winner'] == 'Sweden'])

# print(wwc.loc[(wwc['Winner'] == 'Sweden') | (wwc['Loser'] == 'Sweden')])

# # Code on page 526
def get_country(df, country):
    """df a DataFrame with series labeled Winner and Loser
        country a str
        returns a DataFrame with all rows in which country appears
        in either the Winner or Loser column"""
    return df.loc[(df['Winner'] == country) | (df['Loser'] == country)]

# print(get_country(get_country(wwc, 'Sweden'),'Germany'))

def get_games(df, countries):
    return df[(df['Winner'].isin(countries) |
                df['Loser'].isin(countries))]


# # Code on page 527
# print(wwc['W Goals'].sum())

# print((wwc[wwc['Winner'] == 'Sweden']['W Goals'].sum() +
#         wwc[wwc['Winner'] == 'Sweden']['L Goals'].sum()))

# print((wwc['W Goals'].sum() - wwc['L Goals'].sum())/len(wwc['W Goals']))


# # Code on page 528
# wwc['G Diff'] = wwc['W Goals'] - wwc['L Goals']
# print(wwc)

# # Add new column to wwc
# wwc['G Diff'] = wwc['W Goals'] - wwc['L Goals']
# # create a dict with values for new row
# new_row_dict = {'Round': ['Total'],
#                 'W Goals': [wwc['W Goals'].sum()],
#                 'L Goals': [wwc['L Goals'].sum()],
#                 'G Diff': [wwc['G Diff'].sum()]}
# # Create DataFrame from dict, then pass it to concat
# new_row = pd.DataFrame(new_row_dict)
# wwc = pd.concat([wwc, new_row], sort = False).reset_index(drop = True)
# print(wwc.to_string())

# # Code on page 529
# print(wwc.loc[wwc['Round'] != 'Total'].corr(method = 'pearson'))

# # Code on page 530
# pd.set_option('display.max_rows', 6)
# pd.set_option('display.max_columns', 5)
# temperatures = pd.read_csv('US_temperatures.csv')
# print(temperatures)

# # Code on page 531
# print(temperatures.loc[temperatures['Date']==19790812][['New York','Tampa']])

# temperatures['Max T'] = temperatures.max(axis = 'columns')
# temperatures['Min T'] = temperatures.min(axis = 'columns')
# temperatures['Mean T'] = round(temperatures.mean(axis = 'columns'), 2)
# print(temperatures.loc[temperatures['Date']==20000704])

# # code from page 532
# # Read in file again, because above code modified temperatures
# temperatures = pd.read_csv('US_temperatures.csv')

# temperatures.set_index('Date', drop = True, inplace = True)
# temperatures['Max T'] = temperatures.max(axis = 'columns')
# temperatures['Min T'] = temperatures.min(axis = 'columns')
# temperatures['Mean T'] = round(temperatures.mean(axis = 'columns'), 2)
# print(temperatures.loc[20000704:20000704])

# plt.figure(figsize = (14, 3)) #set aspect ratio for figure
# plt.plot(list(temperatures['Mean T']))
# plt.title('Mean Temp Across 21 US Cities')
# plt.xlabel('Days Since 1/1/1961')
# plt.ylabel('Degrees C')

# plt.figure(figsize = (14, 3)) #set aspect ratio for figure
# plt.plot(list(temperatures['Mean T'])[0:3*365])
# plt.title('Mean Temp Across 21 US Cities')
# plt.xlabel('Days Since 1/1/1961')
# plt.ylabel('Degrees C')

# # Figure 23-3 from page 534
def get_dict(temperatures, labels):
    """temperatures a DataFrame. Its indices are ints
    representing dates of the form yyyymmdd
    labels a list of column labels
    returns a dict with strs representing years as keys,
    the values dicts with the columns as keys, and
    a list of the daily temperatures in that column for
    that year as values
    """
    year_dict = {}
    for index, row in temperatures.iterrows():
        year = str(index)[0:4]
        try:
            for col in labels:
                year_dict[year][col].append(row[col])
        except:
            year_dict[year] = {col:[] for col in labels}
            for col in labels:
                year_dict[year][col].append(row[col])
    return year_dict

# # Code from page 535
temperatures = pd.read_csv('US_temperatures.csv')
temperatures.set_index('Date', drop = True, inplace = True)
temperatures['Mean T'] = round(temperatures.mean(axis = 'columns'), 2)
temperatures['Max T'] = temperatures.max(axis = 'columns')
temperatures['Min T'] = temperatures.min(axis = 'columns')
yearly_dict = get_dict(temperatures, ['Max T', 'Min T', 'Mean T'])
years, mins, maxes, means = [], [], [], []
for y in yearly_dict:
    years.append(y)
    mins.append(min(yearly_dict[y]['Min T']))
    maxes.append(max(yearly_dict[y]['Max T']))
    means.append(round(np.mean(yearly_dict[y]['Mean T']), 2))
yearly_temps = pd.DataFrame({'Year': years, 'Min T': mins,
                              'Max T': maxes, 'Mean T': means})
print(yearly_temps)

# Figure 23-5 from page 536
# plt.figure(0)
# plt.plot(yearly_temps['Year'], yearly_temps['Mean T'])
# plt.title('Mean Annual Temp in 21 U.S. Cities')
# plt.figure(1)
# plt.plot(yearly_temps['Year'], yearly_temps['Min T'])
# plt.title('Min Annual Temp in 21 U.S. Cities')
# for i in range(2):
#     plt.figure(i)
#     plt.xticks(range(0, len(yearly_temps), 4),
#                 rotation = 'vertical', size = 'large')
#     plt.ylabel('Degrees C')
 
# # Figure 23-5 modified as shown on page 537
# plt.figure(0)
# plt.plot(yearly_temps['Year'], yearly_temps['Mean T'])
# plt.title('Mean Annual Temp in 21 U.S. Cities')
# plt.figure(1)
# plt.plot(yearly_temps['Min T'].rolling(7).mean())
# plt.title('Min Annual Temp in 21 U.S. Cities')
# for i in range(2):
#     plt.figure(i)
#     plt.xticks(range(0, len(yearly_temps), 4),
#                 rotation = 'vertical', size = 'large')
#     plt.ylabel('Degrees C')

# # Code from page 537
# num_years = 7
# for label in ['Min T', 'Max T', 'Mean T']:
#     yearly_temps[label] = yearly_temps[label].rolling(num_years).mean()
# yearly_temps['Year'] = yearly_temps['Year'].apply(int)
# print(yearly_temps.corr())

# # Implementation fo r_squared from Section 20.2.1 
def r_squared(measured, predicted):
    """Assumes measured a one-dimensional array of measured values
                predicted a one-dimensional array of predicted values
        Returns coefficient of determination"""
    estimated_error = ((predicted - measured)**2).sum()
    mean_of_measured = measured.sum()/len(measured)
    variability = ((measured - mean_of_measured)**2).sum()
    return 1 - estimated_error/variability

# # Code from page 538
# indices = np.isfinite(yearly_temps['Mean T'])
# model = np.polyfit(list(yearly_temps['Year'][indices]),
#                    list(yearly_temps['Mean T'][indices]), 1)
# print(r_squared(yearly_temps['Mean T'][indices],
#                 np.polyval(model, yearly_temps['Year'][indices])))

# # Code from page 539
# temperatures = pd.read_csv('US_temperatures.csv')
# temperatures.drop('Date', axis = 'columns', inplace = True)
# means = round(temperatures.mean(), 2)
# maxes = temperatures.max()
# mins = temperatures.min()
# city_temps = pd.DataFrame({'Min T':mins, 'Max T':maxes,
# 'Mean T':means})
# city_temps = city_temps.apply(lambda x: 1.8*x + 32)
# city_temps['Max-Min'] = city_temps['Max T'] - city_temps['Min T']
# print(city_temps.sort_values('Mean T', ascending = False).to_string())

# # Code from page 540
# plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Min T'],
#           'b^', label = 'Min T')
# plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Max T'],
#           'kx', label = 'Max T')
# plt.plot(city_temps.sort_values('Max-Min', ascending=False)['Mean T'],
#           'ro', label = 'Mean T')
# plt.xticks(rotation = 'vertical')
# plt.legend()
# plt.title('Variation in Extremal Daily\nTemperature 1961-2015')
# plt.ylabel('Degrees F')

# # Code from page 541
# emissions = pd.read_csv('global-fossil-fuel-consumption.csv')
# print(emissions)

# # Code from page 542
# emissions['Fuels'] = emissions.sum(axis = 'columns')
# emissions.drop(['Coal', 'Crude Oil', 'Natural Gas'], axis = 'columns',
# inplace = True)
# num_years = 5
# emissions['Roll F'] =\
# emissions['Fuels'].rolling(num_years).mean()
# emissions = emissions.round()

# plt.plot(emissions['Year'], emissions['Fuels'],
#           label = 'Consumption')
# plt.plot(emissions['Year'], emissions['Roll F'],
# label = str(num_years) + ' Year Rolling Ave.')
# plt.legend()
# plt.title('Consumption of Fossil Fuels')
# plt.xlabel('Year')
# plt.ylabel('Consumption')

# # # Code from page 543
# yearly_temps['Year'] = yearly_temps['Year'].astype(int)
# merged_df = pd.merge(yearly_temps, emissions,
#                       left_on = 'Year', right_on = 'Year')
# print(merged_df)

print(merged_df.corr().round(2).to_string())