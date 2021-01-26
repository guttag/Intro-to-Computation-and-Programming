# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate
import scipy.stats

#set line width
plt.rcParams['lines.linewidth'] = 4
#set font size for titles 
plt.rcParams['axes.titlesize'] = 16
#set font size for labels on axes
plt.rcParams['axes.labelsize'] = 16
#set size of numbers on x-axis
plt.rcParams['xtick.labelsize'] = 16
#set size of numbers on y-axis
plt.rcParams['ytick.labelsize'] = 16
#set size of ticks on x-axis
plt.rcParams['xtick.major.size'] = 7
#set size of ticks on y-axis
plt.rcParams['ytick.major.size'] = 7
#set size of markers, e.g., circles representing points
plt.rcParams['lines.markersize'] = 10
#set number of times marker is shown when displaying legend
plt.rcParams['legend.numpoints'] = 1
#Set size of type in legend
plt.rcParams['legend.fontsize'] = 14

# # Figure 22-2 on page 492
def plot_housing(impression):
    """Assumes impression a str. Must be one of 'flat',
         'volatile,' and 'fair'
       Produce bar chart of housing prices over time"""
    labels, prices = ([], [])
    with open('midWestHousingPrices.csv', 'r') as f:
        #Each line of file contains year quarter price
        #for Midwest region of U.S.
        for line in f:
            year, quarter, price = line.split(',')
            label = year[2:4] + '\n Q' + quarter[1]
            labels.append(label)
            prices.append(int(price)/1000)
    quarters = np.arange(len(labels)) #x coords of bars
    width = 0.8 #Width of bars
    plt.bar(quarters, prices, width)
    plt.xticks(quarters+width/2, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError
# plot_housing('flat')
# plt.figure()
# plot_housing('volatile')
# plt.figure()
# plot_housing('fair')

# Solution to finger exercise on page 493      
def plot_housing(impression):
    """Assumes impression a str. Must be one of 'flat',
          'volatile,' and 'fair'
        Produce bar chart of housing prices over time"""
    labels, prices = ([], [])
    with open('midWestHousingPrices.csv', 'r') as f:
        #Each line of file contains year quarter price
        #for Midwest region of U.S.
        for line in f:
            year, quarter, price = line.split(',')
            label = year[2:4] + '\n Q' + quarter[1]
            labels.append(label)
            prices.append(int(price)/1000)
    quarters = np.arange(len(labels)) #x coords of bars
    width = 0.8 #Width of bars
    baseline = 200
    bars = plt.bar(quarters, np.array(prices) - baseline, width,
                    bottom = baseline)
    for b in bars:
        if b.get_height() < 0:
            b.set_color('r')
    plt.axhline(200)
    plt.xticks(quarters+width/2, labels)
    plt.title('Housing Prices in U.S. Midwest')
    plt.xlabel('Quarter')
    plt.ylabel('Average Price ($1,000\'s)')
    if impression == 'flat':
        plt.ylim(1, 500)
    elif impression == 'volatile':
        plt.ylim(180, 220)
    elif impression == 'fair':
        plt.ylim(150, 250)
    else:
        raise ValueError

# plot_housing('fair')

# # Code to produce plots in Figure 22-5 on page 494
def plot_followers(with_jguttag):
    if with_jguttag:
        plt.bar('jguttag', 6, color = 'g')
    plt.bar('khemric', 130000, color = 'c')
    plt.bar('katyperry', 95000000, color = 'y')
    plt.title('Number of Followers on Instagram')
    plt.semilogy()
    
# plot_followers(False)
# plt.figure()
# plot_followers(True)

# # Figure 22-13 on page 505
def june_prob(num_trials):
    june_48 = 0
    for trial in range(num_trials):
      june = 0
      for i in range(446):
          if random.randint(1,12) == 6:
              june += 1
      if june >= 48:
          june_48 += 1
    print('Probability of at least 48 births in June =',
          round(june_48/num_trials, 4))

# random.seed(0)
# june_prob(10000)

# # Figure 22-14 on page 506
def any_prob(num_trials):
    any_month_48 = 0
    for trial in range(num_trials):
      months = [0]*12
      for i in range(446):
          months[random.randint(0,11)] += 1
      if max(months) >= 48:
          any_month_48 += 1
    print('Probability of at least 48 births in some month =',
          round(any_month_48/num_trials, 4))

# random.seed(0)
# any_prob(10000)

# # Code from page 510
# print(scipy.stats.ttest_1samp([1, 1], 0.5)[1])