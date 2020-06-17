# =================================================================================================
# KMeansClustering.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin
# levels, glucose levels, and chronic kidney disease (CKD). Randomly generate up to 10 centroids
# without issue. Each centroid will have a classification. The nearest centroid to a point will
#  determine the point's classicfication (decide what to do if the distances are equal yourself).
# Create random test cases until centroids stop mocing and determine whether each case is likely to
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
# assignCentroids takes in a DataArr class and a 2D array of cartesian points
# Returns the index of the centroid closes to each point of the dataArr
def assignToCentroids(normArr, centArr):
    return KDTree(centArr,leafsize = len(centArr)).query(normArr.points)[1]

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
    centArr, upCentArr = updateCentroids(normArr, centArr, classArr)
    if (centArr != upCentArr).any():
        upCentArr = iterate(normArr, upCentArr)
        return upCentArr
    return upCentArr

# graphClusters void function takes a DataArr class, a 1D and 2D array
# Graphs centroids of 1D array and corresponding points of the same color from DataArr class.
def graphClusters(normArr, centArr, classArr):
    # Think of a way to animate the iteration process 
    colors = cm.rainbow(np.linspace(0, 1, len(centArr)))
    plt.figure(figsize = (20, 10))
    for i in range(len(centArr)):
        plt.scatter(normArr.h[classArr == i], normArr.g[classArr == i], 
                    s = 200, color = colors[i], marker = '.', 
                    label = "Class " + str(i))
        plt.scatter(centArr[i, 1], centArr[i, 0], s = 500, color = colors[i],
                    marker = '*', label = "Centroid" + str(i))
    plt.title("Glucose vs. Hemoglobin", fontsize = 30)
    plt.xlabel("Hemoglobin",  fontsize = 24)
    plt.ylabel("Glucose", fontsize = 24)
    plt.grid()
    plt.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    plt.show()
    plt.close()
    return

# dataAnalysis void function takes a DataArr class and a 1D array.
# Prints the true/false positive and negative percentages.
def dataAnalysis(normArr, classArr):
    # Is there a way to match classes?
    signPos, signNeg = (0, )*2 
    pos = np.count_nonzero(normArr.c == 1, axis = 0)
    neg = np.count_nonzero(normArr.c == 0, axis = 0)
    for i in range(len(classArr)):
        if normArr.c[i] == classArr[i] and normArr.c[i] == 1:
            signPos += 1
        elif normArr.c[i] == classArr[i] and normArr.c[i] == 0:
            signNeg += 1
    truPos = 100*signPos/pos
    truNeg = 100*signNeg/neg
    if signPos/pos < .3:
        truPos = 100*(1-signPos/pos)
        truNeg = 100*(1-signNeg/neg)
    print("True Positive: ", round(truPos, 2), '%')
    print("False Positive: ", round(100-truPos, 2), '%')
    print("True Negative: ", round(truNeg, 2), '%')
    print("False Negative: ", round(100-truNeg, 2), '%')
    return

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file, the k number of 
# nearest neighbors, and the test case. 
# This function returns 0.
def mainDriver():
    # Open the CSV file and normalize data using method from NearestNeighborClassifier.
    dataArr = NNC.openCSVFile("CKD")
    normArr = NNC.normalizeData(dataArr)
    
    # Take in an integer number of centroids (i.e.: k value) and create k number of random 
    # centroids.
    k = int(input("How many centroids? \n"))
    centArr = randomCentroids(k)
    
    # Iterate updating and assigning centroids until centroids do not move.
    # Determine location of centroids and class of each point.
    finalCentArr = iterate(normArr, centArr)
    finalClassArr = assignToCentroids(normArr, finalCentArr)
    
    # Analyze data
    graphClusters(normArr, finalCentArr, finalClassArr)
    if k == 2:
        dataAnalysis(normArr, finalClassArr)
    return 0

mainDriver()