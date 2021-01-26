# -*- coding: utf-8 -*-

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
plt.rcParams['savefig.bbox'] = 'tight'
plt.rcParams['savefig.pad_inches'] = 0

# # Figure 24-6 on page 554
def minkowski_dist(v1, v2, p):
    """Assumes v1 and v2 are equal-length arrays of numbers
       Returns Minkowski distance of order p between v1 and v2"""
    dist = 0.0
    for i in range(len(v1)):
        dist += abs(v1[i] - v2[i])**p
    return dist**(1/p)

# # Figure 24-7 on page 555
class Animal(object):
    def __init__(self, name, features):
        """Assumes name a string; features a list of numbers"""
        self.name = name
        self.features = np.array(features)
        
    def get_name(self):
        return self.name
    
    def get_features(self):
        return self.features
    
    def distance(self, other):
        """Assumes other is an Animal
           Returns the Euclidean distance between feature vectors
              of self and other"""
        return minkowski_dist(self.get_features(),
                             other.get_features(), 2)

# # Figure 24-8 on page 556
def compare_animals(animals, precision):
    """Assumes animals is a list of animals, precision an int >= 0
       Builds a table of distances between each animal"""
    # Get labels for columns and rows
    column_labels = [a.get_name() for a in animals]
    row_labels = column_labels[:]
    table_vals = []
    # Get distances between pairs of animals
    # For each row
    for a1 in animals:
        row = []
        #For each column
        for a2 in animals:
            distance = a1.distance(a2)
            row.append(str(round(distance, precision)))
        table_vals.append(row)
    # Produce table
    table = plt.table(rowLabels=row_labels,
                        colLabels=column_labels,
                        cellText=table_vals,
                        cellLoc='center',
                        loc='center',
                        colWidths=[0.2]*len(animals))
    plt.axis('off')
    table.scale(1, 2.5)

# # Code from page 556
# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa', [0,1,0,1,0])
# dart_frog = Animal('dart frog', [1,0,1,0,4])
# animals = [rattlesnake, boa, dart_frog]
# compare_animals(animals, 3)

# # Previous code with addition described on page 557
# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa', [0,1,0,1,0])
# dart_frog = Animal('dart frog', [1,0,1,0,4])
# animals = [rattlesnake, boa, dart_frog]
# alligator = Animal('alligator', [1,1,0,1,4])
# animals.append(alligator)
# compare_animals(animals, 3)

# # Binary version described on page 558
# rattlesnake = Animal('rattlesnake', [1,1,1,1,0])
# boa = Animal('boa', [0,1,0,1,0])
# dart_frog = Animal('dart frog', [1,0,1,0,1])
# animals = [rattlesnake, boa, dart_frog]
# alligator = Animal('alligator', [1,1,0,1,1])
# animals.append(alligator)
# compare_animals(animals, 3)

