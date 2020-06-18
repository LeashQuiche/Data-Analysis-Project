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

# =================================================================================================
# Functions
# =================================================================================================
# openCSVFile function takes in no arguments and parses/organizes data from a CSV file into a 2-D
# numpy array with the columns being: hemoglobin, glucose, classification and each row being a 
# case.
# Note: np.array[row][column]
def openCSVFile():
    dataArr = np.zeros((159,3))
    return dataArr

# normalizeData function takes in a 2D numpy array and scales down the first and second columns to
# range from 0-1 and outputs a 2D array with the normalized data.
def normalizeData(dataArr):
    return dataArr

# graphCSVFile void function takes in a 2D numpy array and graphs with the first column 
# (hemoglobin) as the x-axis and second column (glucose) as the y-axis. The third column 
# (classification) is used to determine the color of the points on the graph.
def graphCSVFile(dataArr):
    return

# findDistance function is either:
# a) takes in an array and a point and returns an array of distances or the minimum distance or
# b) takes in cartesian coordinates and uses a simple use of the distance formula to return the 
# distance between the two points.
def findDistance():
    return 

# createTestCase function creates two random test cases (hemoglobin and glucose) from 0-1 and 
# either: 
# a) adds the points to the inputted array as a new row
# b) returns two points
# c) creates a new 1D array with the two points
# and
# a) creates a classification for the points using the findDistance function
# b) return the points without alteration
def createTestCase():
    return 

# nearestNeighborIndex function takes in a 2D array of cartesian points and a randomly generated 
# test case.
# Method 1: Use indices and the distance function to create an array of points and return the index
# of the closest point.
# Method 2: Use KDTree
# Returns the index of the closest point in the 2D array to the test case.
def nearestNeighborIndex(dataArr, testCase):
    index = 0
    return index

# graphNearestNeighbor void function takes in a 2D numpy array (and a cartesian coordinate
# depending on createTestCase) and graphs the first column (hemoglobin) as the x-axis and the
# second column (glucose) as the y-axis the third column (classification) determines the color of 
# the points. A  randomly generated test case is graphed as a distinct point with a line connecting
# it to the nearest neighbor whose classification it takes on. A legend is generated in a
# reasonable position.
def graphNearestNeighbor(dataArr):
    return

# =================================================================================================
# Main Script
# =================================================================================================
# mainDriver function takes in no inputs and graphs both the orginial CSV file and the test case. 
# This function returns 0.
def mainDriver():
    return 0

# mainDriver()