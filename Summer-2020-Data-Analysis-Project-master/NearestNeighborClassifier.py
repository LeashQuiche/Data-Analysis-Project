# =============================================================================
# NearestNeighborClassifier.py
# Name: Alycia Wong and Brandon Wong
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
# Classes
# =============================================================================
class Butts:
    def __init__(self, data):
        self.gluc = data[:,0]
        self.hemo = data[:,1]
        self.disease = data[:,2]
        self.len = len(data)
        self.all = data[:,:3]
        self.paras = data[:,:2]
        self.shape = np.shape(data)
        self.colmax = np.amax(data, axis = 0)
        self.colmin = np.amin(data, axis = 0)

# =============================================================================
# Functions
# =============================================================================
# Parses in file and turns it into Butts class of data
def openCSVFile(fileName):
    return Butts(np.genfromtxt(fileName, delimiter=',',skip_header=1))

# Takes in butts class
# Loops over data normalizing it for every row
# returns normalized butts class data
def normalizeData(dataArr):
    normArr = np.zeros(dataArr.shape)
    for i in range(len(normArr)):
        normArr[i] = (dataArr.all[i] - dataArr.colmin) / (dataArr.colmax - dataArr.colmin)
    return Butts(normArr)

# graphCSVFile void function takes in a 2D numpy array and graphs with the
# first column (hemoglobin) as the x-axis and second column (glucose) as the 
# y-axis. The third column (classification) is used to determine the color of
# the points on the graph.
def graphCSVFile(normArr):
    plt.scatter(normArr.hemo[normArr.disease==0], normArr.gluc[normArr.disease==0],
                c='b', label='No CKD' )
    plt.scatter(normArr.hemo[normArr.disease==1], normArr.gluc[normArr.disease==1],
                c='r', label='CKD')
    plt.title('Hemoglobin and Glucose levels')
    plt.xlabel('Hemoglobin')
    plt.ylabel('Glucose')
    return
# findDistance function is either:
# a) takes in an array and a point and returns an array of distances or the
# minimum distance or
# B) takes in cartesian coordinates and uses a simple use of the distance
# formula to return the distance between the two points.
def findDistance(x1, y1, x2, y2):
    return np.sqrt((x1-x2)**2+(y1-y2)**2)

# createTestCase function creates two random test cases (hemoglobin and 
# glucose) from 0-1 and: 
# creates a new 1D array with the two points
# return the points raw
def createTestCase():
    return np.random.rand(2)

# nearestNeighborIndex takes in the test case point and returns the index of the
# nearest point to the test case
def nearestNeighborIndex(testCase, normArr):
    distArr = np.zeros(normArr.len)
    for i in range(len(distArr)):
        distArr[i] = findDistance(normArr.hemo[i], normArr.gluc[i], testCase[1], testCase[0])
    nni = distArr.argmin()
    return nni

# graphNearestNeighbor void function takes in a 2D numpy array (and a cartesian 
# coordinate depending on createTestCase) and graphs the first column 
# (hemoglobin) as the x-axis and the second column (glucose) as the y-axis
# the third column (classification) determines the color of the points. A 
# randomly generated test case is graphed as a distinct point with a 
# line connecting it to the nearest neighbor whose classification it takes on.
# A legend is generated in a reasonable position.
def graphNearestNeighbor(testCase, normArr):
    nni = nearestNeighborIndex(testCase, normArr)
    graphCSVFile(normArr)
    plt.scatter(testCase[1], testCase[0],
                c = ('b' if normArr.disease[nni]==0 else 'r'),
                label = 'Test Case',
                marker = "x")
    plt.plot([testCase[1], normArr.hemo[nni]], [testCase[0], normArr.gluc[nni]], 'k-')
    plt.legend()
    plt.show()
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in no inputs and graphs both the orginial CSV
# file and the test case. This function returns 0.
def mainDriver():
    graphNearestNeighbor(createTestCase(), normalizeData(openCSVFile('ckd.csv')))
    return 0
# mainDriver()