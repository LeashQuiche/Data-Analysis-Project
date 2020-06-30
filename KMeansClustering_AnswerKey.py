# =================================================================================================
# KMeansClustering.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin
# levels, glucose levels, and chronic kidney disease (CKD). Randomly generate up to 10 centroids
# without issue. Each centroid will have a classification. The nearest centroid to a point will
#  determine the point's classicfication (decide what to do if the distances are equal yourself).
# Create random test cases until centroids stop moving and determine whether each case is likely to
# have CKD depending on the classification of the nearest centroid.
# =================================================================================================

# =================================================================================================
# Import statements
# =================================================================================================
import matplotlib.pyplot as plt
import numpy as np
import NearestNeighborClassifier_AnswerKey as NNC
from scipy.spatial import KDTree
import matplotlib.cm as cm

# =================================================================================================
# Functions
# =================================================================================================
# randomCentroids function takes in an integer number of clusters to be generated. 
# Outputs a 2D array filled with random values between 0-1.
def randomCentroids(k):
    return np.random.rand(k, 2)

# Method 1:
# assignCentroids function takes in a DataArr class and a 2D array of cartesian points
# Returns the index of the centroid closes to each point of the dataArr
def assignToCentroids(normArr, centArr):
    return KDTree(centArr, leafsize = len(centArr)).query(normArr.points)[1]

# Method 2: Much slower!
# Create distance arrays for every point vs every centroid.
# Find which centroid each point is closest to and return the indices.

# updateCentroids function takes in a DataArr class, a 2D array of points, and an array of indices.
# Returns a 2D array of points in the center of their repsective indexed class.
def updateCentroids(normArr, centArr, classArr):
    upCentArr = np.zeros((len(centArr), len(centArr[0])))
    # You can do a longer boolean statement to ge rid of warning
    for i in range(len(centArr)):
        upCentArr[i] = np.mean(normArr.points[classArr == i], axis = 0)
    return centArr[~np.isnan(upCentArr).any(axis=1)], upCentArr[~np.isnan(upCentArr).any(axis=1)]

# iterate function has an input of a DataArr class and a 2D array of cartesian points.
# Centroid uses recursian to reassign points and update the centroid location until the centroids
# do not move.
# Returns the a 2D array of the final position of the centroids.
def iterate(normArr, centArr):
    classArr = assignToCentroids(normArr, centArr)
    # graphClusters(normArr, centArr, classArr) # If you want to see all the update graphs
    centArr, upCentArr = updateCentroids(normArr, centArr, classArr)
    if (centArr != upCentArr).any():
        return iterate(normArr, upCentArr)
    return upCentArr

# graphClusters void function takes a DataArr class, a 1D and 2D array
# Graphs centroids of 1D array and corresponding points of the same color from DataArr class.
def graphClusters(normArr, centArr, classArr, headers):
    # Add lines separating the different centroids -- may get messy for >3 centroids
    colors = cm.rainbow(np.linspace(0, 1, len(centArr)))
    fig, ax = plt.subplots(figsize = (20, 10))
    for i in range(len(centArr)):
        ax.plot(normArr.h[classArr == i], normArr.g[classArr == i], ls = 'None', c = colors[i],
                    marker = '.', markersize = 15, label = "Class " + str(i))
        ax.plot(centArr[i, 0], centArr[i, 1], ls = 'None', c = colors[i], marker = '*', 
                    markersize = 20, label = "Centroid" + str(i))
    fig.suptitle(headers[0] + " vs. " + headers[1], fontsize = 30)
    ax.set_xlabel(headers[0],  fontsize = 24)
    ax.set_ylabel(headers[1], fontsize = 24)
    ax.grid()
    ax.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    plt.show()
    plt.close()
    return

# dataAnalysis void function takes a DataArr class and a 1D array.
# Prints the true/false positive and negative percentages.
def dataAnalysis(normArr, classArr):
    signPos, signNeg = (0, )*2 
    pos = np.count_nonzero(normArr.c == 1, axis = 0)
    neg = np.count_nonzero(normArr.c == 0, axis = 0)
    for i in range(len(classArr)):
        if normArr.c[i] == classArr[i] and normArr.c[i] == 1:
            signPos += 1
        elif normArr.c[i] == classArr[i] and normArr.c[i] == 0:
            signNeg += 1
    truPos = 100 * signPos/pos
    truNeg = 100 * signNeg/neg
    if signPos/pos < .3:    
    # Find a way to match classes
        truPos = round(100 * (1 - signPos/pos), 2)
        truNeg = round(100 * (1 - signNeg/neg), 2)
    return truPos, round(100 - truPos, 2), truNeg, round(100 - truNeg, 2)

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file, the centroids, and 
# the points with the same classification as the centroids
# This function returns 0.
def mainDriver():
    # Take in an integer number of centroids (i.e.: k value) and create k number of random 
    # centroids.
    k = int(input("How many centroids? "))
    centArr = randomCentroids(k)
    
    # Open the CSV file and normalize data using method from NearestNeighborClassifier.
    fileName = input("Name of file? ")
    dataArr, headers = NNC.openCSVFile(fileName)
    normArr = NNC.normalizeData(dataArr)
    
    # Iterate updating and assigning centroids until centroids do not move.
    # Determine location of centroids and class of each point.
    finalCentArr = iterate(normArr, centArr)
    finalClassArr = assignToCentroids(normArr, finalCentArr)
    
    # Analyze data
    graphClusters(normArr, finalCentArr, finalClassArr, headers)
    if k == 2:
        print(dataAnalysis(normArr, finalClassArr))
    return 0

# mainDriver()