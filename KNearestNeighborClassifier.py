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

# =================================================================================================
# Functions
# =================================================================================================
# kNearestNeighbor function inputs a numpy array, a random point, and an integer k and returns an
# array of length k which holds the indices of the k number of nearest points to the test case.
# Method 1: Use the findDistance function from NearestNeighborClassifier. 
# Method 2: Use a KD Tree
def kNearestNeighbor(dataArr, testCase, k):
    distArr = np.array([])
    return distArr

# kNNClass function takes in an 2 arrays. One of the data and the other is a list of indices.
# Can use various statistical calculations to find the value of the most common class and return
# that class.
def kNNClass(dataArr, distArr):
    return


# graphKNearestNeighbor void function takes in two 1D and one 2D numpy arrays
# to graph. One of the 1D arrays is a random testCase with its own distinct
# points. The other 1D array is used to circle the k number of points closest 
# to the test case. The 2D array contains information parsed from the CSV 
# column. The first column (hemoglobin) is graphed as the x-axis and the second
# column (glucose) as the y-axis. The third column  (classification) determines
# the color of the points. A legend is generated in a reasonable position.
def graphKNearestNeighbor(testCase, distArr, dataArr):
    return

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file, the k number of 
# nearest neighbors, and the test case. This function returns 0.
def mainDriver():
    # Open the CSV file, normalizes data from file, and creates a random point using the functions
    # from NearestNeighborClassifier.
    dataArr = NNC.openCSVFile("CKD")
    normArr = NNC.normalizeData(dataArr)
    testCase = NNC.createTestCase()
    return 0