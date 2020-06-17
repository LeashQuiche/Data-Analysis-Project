# =================================================================================================
# KNearestNeighborClassifier.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin 
# levels, glucose levels, and chronic kidney disease (CKD). Create n number of random test cases
# and determine whether the case is likely to have CKD depending on the mode of the classifications
# of the k number of nearest points.
# =================================================================================================

# =================================================================================================
# Import statements
# =================================================================================================
import matplotlib.pyplot as plt
import numpy as np
import NearestNeighborClassifier_AnswerKey as NNC
from scipy import stats
from scipy.spatial import KDTree

# =================================================================================================
# Functions
# =================================================================================================
# Method 1: 
# kNearestNeighbor takes in a DataArr class, a cartesian points, and an int.
# Creates an array of distances of cartesian point to data.
# Returns the k number of indices of the shortest distances.
def kNearestNeighbor(normArr, testCase, k):
    distArr = np.zeros(normArr.len)
    for i in range(normArr.len):
        distArr[i] = NNC.findDistance(normArr.h[i], normArr.g[i],
                                  testCase[1], testCase[0])
    return np.argsort(distArr)[:k]

# Method 2:
# treeNearestNeighbor takes in a DataArr class, a cartesian points, and an int.
# Creates a KDTree class of the data in the DataArr class.
# Returns the indices of the k number of nearest neighbors.
def treeNearestNeighbor(normArr, testCase, k):
    dataTree = KDTree(normArr.points)
    return dataTree.query(testCase, k)[1]

# kNNClass inputs a DataArr classof data and indices of the points closest to the test case.
# Returns the most common class of the data closest to the point
def kNNClass(normArr, distArr):
    return stats.mode(normArr.c[distArr])[0]

# graphKNearestNeighbor void function takes in a cartesian point, array of k number of indices, and
# a DataArr class.
# Graphs the data, the test case (cartesian point), and the k number of data points closest to the
# test case.
def graphKNearestNeighbor(testCase, distArr, normArr):
    testCaseClass = kNNClass(normArr, distArr)
    color = ['b', 'r']
    NNC.graphCSVFile(normArr)
    plt.plot(testCase[1], testCase[0], color[int(testCaseClass)]
             + 'x', label = "Test case", markersize = 15)
    plt.plot(normArr.h[distArr], normArr.g[distArr], 'yo', 
             label = "k Nearest", markersize = 5)
    plt.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    plt.show()
    plt.close()
    return

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file, the k number of 
# nearest neighbors, and the test case. 
# This function returns 0.
def mainDriver():
    #Ask for integer k input.
    k = int(input("What value of k do you want? \n"))
    
    # Open the CSV file, normalizes data from file, and creates a random point using the functions
    # from NearestNeighborClassifier.
    dataArr = NNC.openCSVFile("CKD")
    normArr = NNC.normalizeData(dataArr)
    testCase = NNC.createTestCase()
    # testCase = np.array([0.1, 0.8])
    
    # Finds and graphs k number of nearest neighbors.
    # distArr = kNearestNeighbor(normArr, testCase, k)
    distArr = treeNearestNeighbor(normArr, testCase, k)
    graphKNearestNeighbor(testCase, distArr, normArr)
    return 0

mainDriver()