# =============================================================================
# KNearestNeighborClassifier.py
# Name: Alycia Wong and Brandon Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# Create a random test case and determine whether the case is
# likely to have CKD depending on the mode of the classifications of the
# k number of nearest points.
# =============================================================================

# =============================================================================
# Import statements
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import NearestNeighborClassifier as NNC
from statistics import mode

# =============================================================================
# Functions
# =============================================================================
# findDistanceArray inputs a numpy array, a random point, and an integer k and
# uses the findDistance function from NearestNeighborClassifier. The function
# outputs a 1D array containing the k number of nearst points to the random
# test case.
def findDistanceArray(normArr, testCase, k):
    distArr = np.zeros(normArr.len)
    for i in range(len(distArr)):
        distArr[i] = NNC.findDistance(normArr.hemo[i], normArr.gluc[i], testCase[1], testCase[0])
        kindex = np.argsort(distArr)[:k]
    return kindex

# graphKNearestNeighbor void function takes in two 1D and one 2D numpy arrays
# to graph. One of the 1D arrays is a random testCase with its own distinct
# points. The other 1D array is used to circle the k number of points closest 
# to the test case. The 2D array contains information parsed from the CSV 
# column. The first column (hemoglobin) is graphed as the x-axis and the second
# column (glucose) as the y-axis. The third column  (classification) determines
# the color of the points. A legend is generated in a reasonable position.
def graphKNearestNeighbor(testCase, normArr, k):
    kindex = findDistanceArray(normArr, testCase, k)
    NNC.graphCSVFile(normArr)
    plt.scatter(testCase[1], testCase[0],
                c = ('b' if mode(normArr.disease[kindex])==0 else 'r'),
                label = 'Test Case',
                marker = "x")
    plt.scatter(normArr.hemo[kindex], normArr.gluc[kindex],
                c='y', label = 'Nearest neighbor(s)')
    print("butts")
    plt.legend(fontsize="small")
    plt.show()
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file,
# the k number of nearest neighbors, and the test case. This function returns 
# 0.5
def mainDriver():
    val = int(input("How many neighbors are you looking for: "))
    test = NNC.createTestCase()
    normal = NNC.normalizeData(NNC.openCSVFile('ckd.csv'))
    graphKNearestNeighbor(test, normal, val)
    return 0
mainDriver()