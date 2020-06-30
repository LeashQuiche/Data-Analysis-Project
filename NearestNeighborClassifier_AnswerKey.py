# =================================================================================================
# NearestNeighborClassifier.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin 
# levels, glucose levels, and chronic kidney disease (CKD). Create n number of random test cases 
# and determine whether the case is likely to have CKD depending on the classification of the
# nearest point.
# =================================================================================================

# =================================================================================================
# Import statements
# =================================================================================================
import matplotlib.pyplot as plt
import numpy as np
from scipy.spatial import KDTree
import csv

# =================================================================================================
# Functions
# =================================================================================================
# DataArr class makes a class of an # x 3 Numpy array and breaks it down into components for ease
# of use wihout excessive indexing.
class DataArr:
    def __init__(self, dataArr):
        self.h = dataArr[:, 0]
        self.g = dataArr[:, 1]
        self.c = dataArr[:, 2]
        self.points = dataArr[:, :2]
        self.len = len(dataArr[:, 0])
        self.size = len(dataArr[0])

# openCSVFile function takes in no arguments.
# Parses/organizes data from a CSV file.
# Return data as a 2-D numpy array with the columns being: 
def openCSVFile(fileName):
    headers = next(csv.reader(open(fileName + '.csv', newline='')))
    dataArr = np.genfromtxt((fileName + '.csv'),delimiter=',', skip_header = 1)
    return dataArr, headers

# normalizeData function takes in a DataArr class.
# Scales down the data to range from 0-1.
# Returns a DataArr class with the normalized data.
def normalizeData(dataArr):
    for i in range(len(dataArr[0])):
        maxVals = np.amax(dataArr[:, i], axis = 0)
        minVals = np.amin(dataArr[:, i], axis = 0)
        dataArr[:, i]= (dataArr[:, i]-minVals)/(maxVals-minVals)
    return DataArr(dataArr)

# graphCSVFile void function takes in a DataArr class.
# Graphs array: 1st column = y axis, 2nd = x axis, 3rd = color.
def graphCSVFile(normArr, headers):
    fig, ax = plt.subplots(figsize = (20, 10))
    ax.plot(normArr.h[normArr.c == 0], normArr.g[normArr.c == 0], 'b.', label = "No CKD", 
             markersize = 15)
    ax.plot(normArr.h[normArr.c == 1], normArr.g[normArr.c == 1], 'r.', label = "CKD", 
             markersize = 15)
    fig.suptitle(headers[0] + " vs. " + headers[1], fontsize = 30)
    ax.set_xlabel(headers[0],  fontsize = 24)
    ax.set_ylabel(headers[1], fontsize = 24)
    ax.grid()
    return fig, ax

# findDistance function takes in two cartesian points.
# Returns the distance between points.
def findDistance(x1, y1, x2, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)

# createTestCase function takes in no parameters.
# Returns a 1D numpy array of two random points.
def createTestCase():
    return np.random.rand(2)

# Method 1:
# nearestNeighbor function takes in a DataArr class and 1D numpy array.
# Finds the index of the point in the DataArr class closest to the 1D array.
# Returns the index of that point.
def nearestNeighborIndex(normArr, testCase):
    distArr = np.zeros(normArr.len)
    for i in range(normArr.len):
        distArr[i] = findDistance(normArr.h[i], normArr.g[i], testCase[0], testCase[1])
    return np.argmin(distArr)

# Method 2: 
# treeNNIndex function takes in a DataArr class and 1D numpy array.
# Returns the index of the closest point of data to the test case.
def treeNNIndex(normArr, testCase):
    return KDTree(normArr.points).query(testCase)[1]

# graphNearestNeighbor void function takes in a DataArr class, 
# a cartesian point, and the classification of the point.
# Graphs the 2D numpy array and the point
def graphNearestNeighbor(normArr, testCase, testCaseIndex, headers):
    color = ['bx', 'rx']
    fig, ax = graphCSVFile(normArr, headers)
    ax.plot(testCase[0], testCase[1], color[int(normArr.c[testCaseIndex])], label = "Test case", 
             markersize = 20)
    ax.plot(np.array([testCase[0], normArr.h[testCaseIndex]]), 
             np.array([testCase[1], normArr.g[testCaseIndex]]), 'k-')
    ax.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    plt.show()
    return

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in no inputs and graphs both the orginial CSV file and the test case. 
# This function returns 0.
def mainDriver():
    # Parse and normalize data from csv file.
    filename = input("Name of file? ")
    dataArr, headers = openCSVFile(filename)
    normArr = normalizeData(dataArr)
    # graphCSVFile(normArr)
    
    # Generate random testcase.
    testCase = createTestCase()
    # testCase = np.array([0.2, 0.7])
    
    # Determine index of point closes to the test case.
    # testCaseIndex = nearestNeighborIndex(normArr, testCase)
    testCaseIndex = treeNNIndex(normArr, testCase)
    
    # Graph data and test case.
    graphNearestNeighbor(normArr, testCase, testCaseIndex, headers)
    return 0

# mainDriver()