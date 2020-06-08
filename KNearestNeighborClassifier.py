# =============================================================================
# KNearestNeighborClassifier.py
# Name: Alycia Wong and Brandon Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# create n number of random test cases and determine whether the case is
# likely to have CKD depending on the mode of the classifications of the
# k number of nearest points.
# =============================================================================

# Import statements
import matlibplot.pyply as plt
import numpy as np
import random as rand
import NearestNeighborClassifier as NNC

# Open the CSV file using the parsing method from NearestNeighborClassifier.
NNC.openCSVFile

# Normalize data using method from NearestNeighborClassifier.
NNC.normalizeData(array)

# Graph CSV file using method from NearestNeighborClassifier.
NNC.graphCSVFile()

# Create a random test case using the method from NearestNeighborClassifier.
NNC.createTestCase(array)

# findDistanceArray inputs a numpy array, a random point, and an integer k and
# uses the findDistance function from NearestNeighborClassifier. The function
# outputs a 1D array containing the k number of nearst points to the random
# test case.
def findDistanceArray(array, testCase, k):
    return disanceArray

# graphKNearestNeighbor void function takes in a two 1D and one 2D numpy arrays
# to graph. One of the 1D arrays will be a random testCase with its own 
# distinct points. The other 1D array will be the used to circle the k number
# of points closest to the test case. The 2D array will contain information
# parsed from the CSV column. The first column (hemoglobin) will be graphed as
# the x-axis and the second column (glucose) as the y-axis. The third column 
# (classification) will determine the color of the points. A legend will be
# generated in a reasonable position.
def graphKNearestNeighbor(testCase, distanceArray, array):
    return

# mainDriver function will take in nothing and graph both the orginial CSV
# file, the k number of nearest neighbors, and the test case. This function 
# returns 0.
def mainDriver():
    return 0