# =============================================================================
# NearestNeighborClassifier.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# Create n number of random test cases and determine whether the case is
# likely to have CKD depending on the classification of the nearest point.
# =============================================================================

# =============================================================================
# Import statements
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# Functions
# =============================================================================
# openCSVFile function takes in no arguments.
# Parses/organizes data from a CSV file.
# Return data as a 2-D numpy array with the columns being: 
# glucose, hemoglobin, classification and each row being a case.
def openCSVFile(fileName):
    return np.genfromtxt((fileName + '.csv'),delimiter=',', skip_header = 1)

# normalizeData function takes in a 2D numpy array,
# Scales down the data to range from 0-1.
# Returns a 2D array with the normalized data.
def normalizeData(dataArr):
    maxVals = np.amax(dataArr, axis = 0)
    minVals = np.amin(dataArr, axis = 0)
    for i in range(len(dataArr)):
        dataArr[i]= (dataArr[i]-minVals)/(maxVals-minVals)
    return dataArr

# graphCSVFile void function takes in a 2D numpy array.
# Graphs array: 1st column = y axis, 2nd = x axis, 3rd = color.
def graphCSVFile(dataArr):
    plt.plot(dataArr[dataArr[:, 2] == 0, 1], dataArr[dataArr[:, 2] == 0, 0], 
             'b.', label = "No CKD")
    plt.plot(dataArr[dataArr[:, 2] == 1, 1], dataArr[dataArr[:, 2] == 1, 0], 
             'r.', label = "CKD")
    plt.title("Hemoglobin vs. Glucose vs CKD")
    plt.xlabel("Hemoglobin")
    plt.ylabel("Glucose")
    plt.legend()
    plt.show()
    return

# findDistance function takes in two cartesian points.
# Returns the distance between points.
def findDistance(x1, y1, x2, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)

# createTestCase function takes in no parameters.
# Returns a 1D numpy array of two random points.
def createTestCase():
    return np.random.rand(2)

# nearestNeighbor takes in a 2D numpy array and 1D numpy array.
# Finds the index of the point in the 2D array closest to the 1D array.
# Returns the index of that point.
def nearestNeighborIndex(dataArr, testCase):
    distArr = np.zeros(len(dataArr))
    for i in range(len(dataArr)):
        distArr[i] = findDistance(dataArr[i, 1], dataArr[i, 0],
                                  testCase[1], testCase[0])
    return np.argmin(distArr)

# graphNearestNeighbor void function takes in a 2D numpy array, 
# a cartesian point, and the classification of the point.
# Graphs the 2D numpy array and the point
def graphNearestNeighbor(dataArr, testCase, testCaseIndex):
    color = ['b', 'r']
    plt.figure(figsize = (20, 10))
    plt.plot(dataArr[dataArr[:, 2] == 0, 1], dataArr[dataArr[:, 2] == 0, 0], 
             color[0] + '.', label = "No CKD", markersize = 10)
    plt.plot(dataArr[dataArr[:, 2] == 1, 1], dataArr[dataArr[:, 2] == 1, 0], 
             color[1] + '.', label = "CKD", markersize = 10)
    plt.plot(testCase[1], testCase[0], color[int(dataArr[testCaseIndex, 2])]
             + 'x', label = "Test case", markersize = 15)
    plt.plot(np.array([testCase[1], dataArr[testCaseIndex, 1]]),
             np.array([testCase[0], dataArr[testCaseIndex, 0]]), 'k-')
    plt.title("Glucose vs. Hemoglobin", fontsize = 30)
    plt.xlabel("Hemoglobin",  fontsize = 24)
    plt.ylabel("Glucose", fontsize = 24)
    plt.grid()
    plt.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    # plt.show()
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in no inputs and graphs both the orginial CSV
# file and the test case. This function returns 0.
def mainDriver():
    dataArr = openCSVFile('CKD')
    normArr = normalizeData(dataArr)
    # graphCSVFile(normArr)
    testCase = createTestCase()
    # testCase = np.array([0.2, 0.7])
    testCaseIndex = nearestNeighborIndex(normArr, testCase)
    graphNearestNeighbor(normArr, testCase, testCaseIndex)
    return 0

mainDriver()