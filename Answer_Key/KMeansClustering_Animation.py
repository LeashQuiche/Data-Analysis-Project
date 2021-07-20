# =============================================================================
# KMeansClustering_Animation.py
# Name: Aycia Wong
# Date: June 2020
# Description: Process and graph a CSV file containing biomedical data that relates hemoglobin
# levels, glucose levels, and chronic kidney disease (CKD). Randomly generate up to 10 centroids
# without issue. Each centroid will have a classification. The nearest centroid to a point will
# determine the point's classicfication (decide what to do if the distances are equal yourself).
# Create random test cases until centroids stop moving and determine whether each case is likely to
# have CKD depending on the classification of the nearest centroid. Create a gif (short, repeatable 
# video file) of the original centroids and classifications, the graph of every iteration process, 
# and the final graph of the centroids and their classifications. You can add percentages as well 
# in the margin/legend if you like.
# =============================================================================

# =============================================================================
# Import Statements
# =============================================================================
import NearestNeighborClassifier_AnswerKey as NNC
import KMeansClustering_AnswerKey as KMC
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import imageio
import os
# imageio.plugins.freeimage.download()

# =============================================================================
# Functions
# =============================================================================
# animateIterate funcion takes in a DataArr class, a list of random cenroids, an integer, and a list
# of strings that are the labels for the x and y axes.
# The function uses recursion to update/reassign points to centroids until centroids stop moving. 
# This function also calls the animateGraph function and counts the number of graphs created.
# The function returns the final centroid locations and the number of graphs created.
def animateIterate(normArr, centArr, j, headers):    
    classArr = KMC.assignToCentroids(normArr, centArr)
    animateGraph(normArr, centArr, j, headers)
    centArr, upCentArr = KMC.updateCentroids(normArr, centArr, classArr)
    if (centArr != upCentArr).any():
        return animateIterate(normArr, upCentArr, j + 1, headers)
    return upCentArr, (j + 1)

# animateGraph function takes in a DataArr class, a list of centroid locations, an integer, and a 
# list of strings  that are the labels for the x and y axes.
# The function draws a figure based on the parameters and then saves the graph as a png file.
def animateGraph(normArr, centArr, j, headers):
    classArr = KMC.assignToCentroids(normArr, centArr)
    fig, ax = plt.subplots(figsize = (20, 10))
    colors = cm.rainbow(np.linspace(0, 1, len(centArr)))
    for i in range(len(centArr)):
        ax.plot(normArr.h[classArr == i], normArr.g[classArr == i], ls = 'None', c = colors[i],
                    marker = '.', markersize = 15, label = "Class " + str(i)+ ", " + 
                    str(round((100 * np.count_nonzero(classArr == i))/len(classArr))) + "%")
        ax.plot(centArr[i, 0], centArr[i, 1], ls = 'None', c = colors[i], marker = '*', 
                    markersize = 20, label = "Centroid" + str(i))
    fig.suptitle(headers[0] + " vs. " + headers[1], fontsize = 30)
    ax.set_xlabel(headers[0],  fontsize = 24)
    ax.set_ylabel(headers[1], fontsize = 24)
    ax.grid()
    ax.legend(loc = "best", prop = {"size": 20}, fontsize = 18)
    fig.canvas.draw()
    plt.savefig("KMC" + str(j) + ".png", bbox_inches='tight')
    return

# makeGif function takes in an integer that is the number of images being used in the gif file.
# The function creates a list of all of the images being used, deletes the png files, and converts
# the list of images into a gif file.
def makeGif(j):
    kwargs_write = {'fps':2.0, 'quantizer':'nq'}
    frames = [0]*(j)
    for i in range(j):
        frames[i] = (imageio.imread("KMC" + str(i) + ".png"))
        os.remove("KMC" + str(i) + ".png")
    imageio.mimsave("KMC.gif", frames, 'GIF-FI', **kwargs_write)
    return

# =============================================================================
# Main Script
# =============================================================================
# mainDriver function takes in nothing and graphs both the orginial CSV file, the centroids, and 
# the points with the same classification as the centroids. Creates a gif file that is saved to the
# working directory. This function returns 0.
def mainDriver():
    # Get user input and parse in, normalize, and convert csv file.
    k = int(input("How many centroids? "))
    fileName = input("Name of file? ")
    dataArr, headers = NNC.openCSVFile(fileName)
    normArr = NNC.normalizeData(dataArr)
    
    # Graph and save information as a gif file.
    centArr = KMC.randomCentroids(k)
    finalCentArr, j = animateIterate(normArr, centArr, 0, headers)
    print(j)
    makeGif(j)
    return 0

# mainDriver()