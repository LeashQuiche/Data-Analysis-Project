# =================================================================================================
# KMeansClustering.py
# Name: Alycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin
# levels, glucose levels, and chronic kidney disease (CKD). Randomly generate up to 10 centroids
# without issue. Each centroid will have a classification. The nearest centroid to a point will
#  determine the point's classicfication (decide what to do if the distances are equal yourself).
# Create random test cases until centroids stop mocing and determine whether each case is likely to
# have CKD depending on the classification of the nearest centroid.
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
# randomCentroids function takes in an integer number of clusters to be generated. 
# OR asks for k number of integer clusters
# Outputs a 2D array filled with random values between 0-1. The first column represents hemoglobin
# and the second column represents glucose.
# There are k number of rows representing the number of centroids and the classification of each 
# centroid (i.e.: row index = classification value).
# OR you can have a third column with the classification value.
def randomCentroids(k):
    centArr = np.array([])
    return centArr

# assignCentroids function takes in an array of normalized x (hemoglobin) and y (glucose) values 
# from the CSV file and the randomly generated array of centroids from randomCentroids. 
# Method 1: Use shape/KD tree to determine closest point to each centroid.
# Method 2: Using the findDistance function from  NearestNeighborClassifier, points are assigned 
# the same classification as the nearest centroid. A 2D array of the normalized data and its 
# classification are returned.
def assignToCentroids(array, centArr):
    classArr = np.array([])
    return classArr

# updateCentroids function inputs the 2D array of centroid locations and of classified and 
# normalized CSV data. The average x (hemo) and y (gluc) positions of all data points for each 
# classifications are found and an updated 2D array with these average cartesian points as the 
# location for the new centroids is returned along with the original cartesian points. 
def updateCentroids(dataArr, centArr, classArr):
    upCentArr = np.array([])
    return centArr, upCentArr

# iterate void function can either
# a) input information and iterate the original information until centArr = upCentArr (recursion)
# b) don't input any information and run by itself. Similar to a main script
# The function causes for the centroids to reassign points and update the
# centroid until the centroids do not move.
def iterate():
    return


# graphClusters void function takes in a 1D and a 2D numpy array to graph. The 1D array of centroid
# locations and classifactions have distinct points on the graph. The 2D array graphs points of
# normalized CSV data and colors them the same color as their corresponding centroids. A legend is 
# generated in a reasonable position.
# Bonus: Create lines roughly separating each centroid group
def graphClusters(dataArr, classArr, centArr):
    return

# dataAnalysis void function takes in the original parsed CSV classifications and the final
# classifications of the data based on K-means clustering (use of centroids) and compares the two
# to find false/true positives/negatives.
# Note: This should only run when there are two centroids (i.e.: k = 2)
# False positive: Percentage of non-CKD were incorrectly labelled by K-Means as being in the CKD 
# cluster
# True positive (sensitivity): Percentage of CKD patients were correctly labeled by K-Means 
# False negative: Percentage of non-CKD were incorrectly labelled by K-Means as being in the CKD 
# cluster
# True negative (specificity): Percentage of non-CKD patients were correctly labelled by K-Means 
# Note: True positive (~93 %) + False positive (~7%) = 100%
# Note: True Negative (~100%) + False negative (~0%) = 100%
def dataAnalysis():
    return 

# =============================================================================
# Main Script
# =============================================================================
# mmainDriver function takes in nothing and graphs both the orginial CSV file, the k number of 
# nearest neighbors, and the test case. 
# This function returns 0.
def mainDriver():
   # Open the CSV file and normalize data using method from NearestNeighborClassifier.
    dataArr = NNC.openCSVFile("CKD")
    normArr = NNC.normalizeData(dataArr)
    return 0