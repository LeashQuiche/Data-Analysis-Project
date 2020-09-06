# =============================================================================
# KMeansClustering.py
# Name: Alycia Wong and Brandon Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that 
# relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
# Randomly generate up to 10 centroids without issue. Each centroid will have a
# classification. The nearest centroid to a point will determine the point's 
# classicfication (decide what to do if the distances are equal yourself).
# Create random test cases until centroids stop mocing and determine whether 
# each case is likely to have CKD depending on the classification of the
# nearest centroid.
# Bonus: Create lines roughly separating each centroid group
# =============================================================================

# =============================================================================
# Import statements
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import NearestNeighborClassifier as NNC
from scipy.spatial import KDTree as kdt

# =============================================================================
# Functions
# =============================================================================
# randomCentroids function takes in an integer number of clusters to be
# generated. 
# OR asks for k number of integer clusters
# Outputs a 2D array filled with random values between 0-1. The 
# first column represents glucose and the second column represents hemoglobin.
# There are k number of rows representing the number of centroids and the
# classification of each centroid (i.e.: row index = classification value).
# OR you can have a third column with the classification value.
def randomCentroids(k):
    return np.random.rand(k,2)

# assignCentroids function takes in an array of normalized x (hemoglobin) and y 
# (glucose) values from the CSV file and the randomly generated array of 
# centroids from randomCentroids. Using the findDistance function from 
# NearestNeighborClassifier, points are assigned the same classification as the 
# nearest centroid. A 2D array of the normalized data and its classification 
# are returned.
def assignToCentroids(normArr, centArr):
    return kdt(centArr).query(normArr)[1]
# print(assignToCentroids(NNC.normalizeData(NNC.openCSVFile('ckd.csv')).paras, np.array([[.5, .5],[.25,.25]])))

# updateCentroids function inputs the 2D array of centroid locations and of 
# classified and normalized CSV data. The average x (hemo) and y (gluc) 
# positions of all data points for each classifications are found and an 
# updated 2D array with these average cartesian points as the location for the
# new centroids is returned along with the original cartesian points. 
#avg of all 1s will be new cent, avg of all 0s will be new cent

def updateCentroids(centArr, classArr, normArr):
    upCentArr = centArr.copy()
    for i in range(len(centArr[:,0])):
        upCentArr[i,0] = np.mean(normArr.gluc[classArr==i])
        upCentArr[i,1] = np.mean(normArr.hemo[classArr==i])
    return upCentArr
# centArr = np.array([[0.5, 0.5], [.25, .25]])
# print(updateCentroids(
#     centArr, assignToCentroids(
#         NNC.normalizeData(NNC.openCSVFile('ckd.csv')).paras, centArr),
#         NNC.normalizeData(NNC.openCSVFile('ckd.csv'))
#     ))
# print(centArr)

# iterate void function can either
# a) input information and iterate the original information until centArr ~ 
#     upCentArr
def iterate(normArr, centArr):
    # classArr = np.zeros(len(normArr.gluc))
    classArr = assignToCentroids(normArr, centArr)
    upCentArr = updateCentroids(centArr, classArr, normArr)
    # print(classArr)
    if (upCentArr != centArr).any():
        centArr = upCentArr
        return iterate(normArr, centArr)
    return centArr
print(iterate(
    NNC.normalizeData(NNC.openCSVFile('ckd.csv')), np.array([[.5, .5],[.25,.25]])
    ))

# graphClusters void function takes in a 1D and a 2D numpy array to graph. The
# 1D array of centroid locations and classifactions have distinct points on the 
# graph. The 2D array graphs points of normalized CSV data and colors them the
# same color as their corresponding centroids. A legend is generated in a
# reasonable position.
# Bonus: Create lines roughly separating each centroid group
def graphClusters():
    
    return

# dataAnalysis void function takes in the original parsed CSV classifications 
# and the final classifications of the data based on K-means clustering (use of
# centroids) and compares the two to find false/true positives/negatives.
# Note: This should only run when there are two centroids (i.e.: k = 2)
# False positive: Percentage of non-CKD were incorrectly labelled by K-Means as
# being in the CKD cluster
# True positive (sensitivity): Percentage of CKD patients were correctly 
# labeled by K-Means 
# False negative: Percentage of non-CKD were incorrectly labelled by K-Means as
# being in the CKD cluster
# True negative (specificity): Percentage of non-CKD patients were correctly 
# labelled by K-Means 
# Note: True positive (~93 %) + False positive (~7%) = 100%
# Note: True Negative (~100%) + False negative (~0%) = 100%
def dataAnalysis():
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
    
    return 0