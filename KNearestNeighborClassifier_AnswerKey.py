# =============================================================================
# KNearestNeighborClassifier.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# Create n number of random test cases and determine whether the case is
# likely to have CKD depending on the mode of the classifications of the
# k number of nearest points.
# =============================================================================

# =============================================================================
# Import statements
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import NearestNeighborClassifier_AnswerKey as NNC
from scipy import stats

# =============================================================================
# Functions
# =============================================================================
# kNearestNeighbor takes in a 2D array of data, a cartesian points, and an int.
# Creates an array of distances of cartesian point to data.
# Returns the k number of indices of the shortest distances.
def kNearestNeighbor(dataArr, testCase, k):
    distArr = np.zeros(len(dataArr))
    for i in range(len(dataArr)):
        distArr[i] = NNC.findDistance(dataArr[i, 1], dataArr[i, 0],
                                  testCase[1], testCase[0])
    return np.argsort(distArr)[:k]

# kNNClass inputs a 2D array of data and indices of the points closest to the 
# test case.
# Returns the most common class of the data closest to the point
def kNNClass(dataArr, distArr):
    return stats.mode(dataArr[distArr, 2])[0]

# graphKNearestNeighbor void function takes in a cartesian point, array of k 
# number of indices, and a 2D data array.
# Graphs the data, the test case (cartesian point), and the k number of data
# points closest to the tes case.
def graphKNearestNeighbor(testCase, distArr, dataArr):
    testCaseClass = kNNClass(dataArr, distArr)
    color = ['b', 'r']
    NNC.graphCSVFile(dataArr)
    plt.plot(testCase[1], testCase[0], color[int(testCaseClass)]
             + 'x', label = "Test case", markersize = 15)
    plt.plot(dataArr[distArr, 1], dataArr[distArr, 0], 'yo', 
             label = "k Nearest", markersize = 5)
    plt.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file,
# the k number of nearest neighbors, and the test case. This function returns 
# 0.
def mainDriver():
    #Ask for integer k input
    k = int(input("What value of k do you want? \n"))
    
    # Open the CSV file using the parsing method from 
    # NearestNeighborClassifier. No input, outputs 2D numpy array.
    dataArr = NNC.openCSVFile("CKD")
    
    # Normalize data using method from NearestNeighborClassifier. Input and
    # outputs a 2D numpy array
    normArr = NNC.normalizeData(dataArr)
    
    # Create a random test case using the method from 
    # NearestNeighborClassifier. No input, outputs 1D numpy array.
    testCase = NNC.createTestCase()
    # testCase = np.array([0.1, 0.8])
    
    distArr = kNearestNeighbor(normArr, testCase, k)
    graphKNearestNeighbor(testCase, distArr, normArr)
    return 0

# mainDriver()