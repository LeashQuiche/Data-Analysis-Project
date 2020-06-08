# =============================================================================
# NearestNeighborClassifier.py
# Name: Alycia Wong and Brandon Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# create n number of random test cases and determine whether the case is
# likely to have CKD depending on the classification of the nearest point.
# =============================================================================

# Import statements
import matlibplot.pyply as plt
import numpy as np
import random as rand

# openCSVFile function takes in no arguments and parses/organizes data from
# a CSV file into a 2-D numpy array with the columns being: hemoglobin, 
# glucose, classification and each row being a case.
def openCSVFile():
    data = np.zeros((200,3))
    return data

# normalizeData function takes in a 2D numpy array and scales down the first 
# and second columns to range from 0-1 and outputs a 2D array with the
# normalized data.
def normalizeData(array):
    return array

# graphCSVFile void function takes in a 2D numpy array and graphs with the
# first column (hemoglobin) as the x-axis and second column (glucose) as the 
# y-axis. The third column (classification) will be used to determine the
# color of the points on the graph.
def graphCSVFile():
    return

# findDistance function is either:
# a) takes in an array and a point and returns an array of distances or the
# minimum distance or
# b) takes in cartesian coordinates and uses a simple use of the distance
# formula to return the distance between the two points.
def findDistance():
    return 

# createTestCase function creates two random test cases (hemoglobin and 
# glucose) from 0-1 and either: 
# a) adds the points to the inputted array as a new row
# b) returns two points
# c) creates a new 1D array with the two points
# and
# a) creates a classification for the points using the findDistance function
# b) return the points raw
def createTestCase(array):
    return array

# graphNearestNeighbor void function takes in a 2D numpy array (and a cartesian 
# coordinate depending on createTestCase) and graphs the first column 
# (hemoglobin) as the x-axis and the second column (glucose) as the y-axis
# the third column (classification) will determine the color of the points.
# a randomly generated test case will be graphed as a distinct point with a 
# line connecting it to the nearest neighbor whose classification it will 
# take on. A legend will be generated in a reasonable position.
def graphNearestNeighbor(array):
    return

# mainDriver function will take in no inputs and graph both the orginial CSV
# file and the test case. This function returns 0.
def mainDriver():
    return 0