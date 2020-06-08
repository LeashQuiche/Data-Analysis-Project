# =============================================================================
# KNearestNeighborClassifier.py
# Name: Alycia Wong and Brandon Wong
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
import matlibplot.pyply as plt
import numpy as np
import random as rand
import NearestNeighborClassifier as NNC

# =============================================================================
# Functions
# =============================================================================
# findDistanceArray inputs a numpy array, a random point, and an integer k and
# uses the findDistance function from NearestNeighborClassifier. The function
# outputs a 1D array containing the k number of nearst points to the random
# test case.
def findDistanceArray(dataArr, testCase, k):
    distArr = np.array([])
    return distArr

# graphKNearestNeighbor void function takes in two 1D and one 2D numpy arrays
# to graph. One of the 1D arrays is a random testCase with its own distinct
# points. The other 1D array is used to circle the k number of points closest 
# to the test case. The 2D array contains information parsed from the CSV 
# column. The first column (hemoglobin) is graphed as the x-axis and the second
# column (glucose) as the y-axis. The third column  (classification) determines
# the color of the points. A legend is generated in a reasonable position.
def graphKNearestNeighbor(testCase, distArr, dataArr):
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file,
# the k number of nearest neighbors, and the test case. This function returns 
# 0.
def mainDriver():
    # Open the CSV file using the parsing method from 
    # NearestNeighborClassifier. No input, outputs 2D numpy array.
    NNC.openCSVFile
    
    # Normalize data using method from NearestNeighborClassifier. Input and
    # outputs a 2D numpy array
    NNC.normalizeData()
    
    # Graph CSV file using method from NearestNeighborClassifier. Input 2D 
    # numpy array. Void function.
    NNC.graphCSVFile()
    
    # Create a random test case using the method from 
    # NearestNeighborClassifier. No input, outputs 1D numpy array.
    NNC.createTestCase()
    return 0