# Summer-2020-Data-Analysis-Project

# Nearest Neighbor Classifier Script Description:
Process and graph a CSV file containing biomedical data that relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
Create n number of random test cases and determine whether the case is likely to have CKD depending on the classification of the nearest point.

# Nearest Neighbor Classifier Function Descriptions:
openCSVFile function takes in no arguments and parses/organizes data from a CSV file into a 2-D numpy array with the columns being: 
hemoglobin, glucose, classification and each row being a case.

normalizeData function takes in a 2D numpy array and 
scales down the first and second columns to range from 0-1 and 
outputs a 2D array with the normalized data.

graphCSVFile void function takes in a 2D numpy array and graphs with:
the first column (hemoglobin) as the x-axis and second column (glucose) as the y-axis. 
The third column (classification) is used to determine the color of the points on the graph.

findDistance function is either takes in cartesian coordinates and
uses a simple use of the distance formula
to return the distance between the two points.

createTestCase function creates two random test cases (hemoglobin and glucose) from 0-1 and
creates/returns a new 1D array with the two points.

nearestNeighbor function takes in a 2D array of cartesian points and a randomly generated test case.
Returns the index of the closest point in the 2D array to the test case.
Method 1: Use indices and the distance function to create an array of points and return the index of the closest point.
Method 2: Use KDTree

graphNearestNeighbor void function takes in a 2D numpy array (and a cartesian 
coordinate depending on createTestCase) and 
graphs the first column (hemoglobin) as the x-axis and the second column (glucose) as the y-axis.
The third column (classification) determines the color of the points. 
A randomly generated test case is graphed as a distinct point with a line connecting it to the nearest neighbor whose classification it takes on.
A legend is generated in a reasonable position.

mainDriver function takes in no inputs and graphs both the orginial CSV file and the test case. 
This function returns 0.

# K Nearest Nearest Neighbor Classifier Script Description:

Process and graph a CSV file containing biomedical data that relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
Create n number of random test cases and determine whether the case is likely to have CKD depending on the mode of the classifications of the k number of nearest points.

# K Nearest Nearest Neighbor Classifier Functions Descriptions:

kNearestNeighbor function inputs a numpy array, a random point, and an integer k and 
returns an array of length k which holds the indices of the k number of nearest points to the test case.
Method 1: Use the findDistance function from NearestNeighborClassifier. 
Method 2: Use a KD Tree

kNNClass function takes in an 2 arrays. One of the data and the other is a list of indices.
Can use various statistical calculations to find the value of the most common class and return that class.

graphKNearestNeighbor void function takes in two 1D and one 2D numpy arrays to graph.
One of the 1D arrays is a random testCase with its own distinct points.
The other 1D array is used to circle the k number of points closest to the test case.
The 2D array contains information parsed from the CSV column.
The first column (hemoglobin) is graphed as the x-axis and the second column (glucose) as the y-axis.
The third column  (classification) determines the color of the points. 
A legend is generated in a reasonable position.

mainDriver function takes in nothing and graphs both the orginial CSV file, the k number of nearest neighbors, and the test case.
This function returns 0.

# K Means Clustering Script Description:

Process and graph a CSV file containing biomedical data that relates hemoglobin levels, glucose levels, and chronic kidney disease (CKD).
Randomly generate up to 10 centroids without issue. 
Each centroid will have a classification. 
The nearest centroid to a point will determine the point's classicfication (decide what to do if the distances are equal yourself).
Create random test cases until centroids stop mocing and determine whether each case is likely to have CKD depending on the classification of the nearest centroid.

# K Means ClusteringClassifier Functions Descriptions:

randomCentroids function takes in an integer number of clusters to be generated. 
OR asks for k number of integer clusters
Outputs a 2D array filled with random values between 0-1. 
The first column represents hemoglobin and the second column represents glucose.
There are k number of rows representing the number of centroids and the classification of each centroid (i.e.: row index = classification value).
OR you can have a third column with the classification value.

assignCentroids function takes in an array of normalized x (hemoglobin) and y (glucose) values from the CSV file and the randomly generated array of centroids from randomCentroids. 
Method 1: Use shape/KD tree to determine closest point to each centroid.
Method 2: Using the findDistance function from  NearestNeighborClassifier, points are assigned the same classification as the nearest centroid.
A 2D array of the normalized data and its classification are returned.

updateCentroids function inputs the 2D array of centroid locations and of classified and normalized CSV data.
The average x (hemo) and y (gluc) positions of all data points for each classifications are found and
an updated 2D array with these average cartesian points as the location for the new centroids is returned along with the original cartesian points. 

iterate void function can either
a) input information and iterate the original information until centArr ~ upCentArr
b) don't input any information and run by itself. Similar to a main script
The function causes for the centroids to reassign points and update the centroid until the centroids do not move.

graphClusters void function takes in a 1D and a 2D numpy array to graph. 
The 1D array of centroid locations and classifactions have distinct points on the graph. 
The 2D array graphs points of normalized CSV data and colors them the same color as their corresponding centroids.
A legend is generated in a reasonable position.

dataAnalysis void function takes in the original parsed CSV classifications and the final classifications of the data based on K-means clustering (use of centroids) and
compares the two to find false/true positives/negatives.

mainDriver function takes in nothing and graphs both the orginial CSV file, the k number of nearest neighbors, and the test case. 
This function returns 0.
