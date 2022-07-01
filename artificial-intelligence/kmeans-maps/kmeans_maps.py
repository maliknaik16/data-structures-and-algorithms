
# Note: this file generates the centroids for optimizing the search space for
#       determining the zipcode when the latitude and logitude is provided.

from shapely.geometry import Point
from geopandas import GeoDataFrame
from math import *

import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np
import random
import json

class KMeans:

    def __init__(self, k=5, random_state=42, distance_formula='haversine'):

        # Random seed.
        np.random.seed(random_state)
        random.seed(random_state)

        # The number of clusters.
        self.k = k

        # Initialze centroid with empty array.
        self.centroids = np.empty([self.k, 2])

        # Stores the cluster information.
        self.clusters = None

        # Distance metric used for cluster.
        if distance_formula == 'haversine':
            self.distance_formula = self.haversine_distance
        else:
            self.distance_formula = self.euclidean_distance

    def _init_centroids(self, X):

        # Get the shape of the data.
        m, n = X.shape

        for i in range(self.k):

            # Get random index from the samples.
            idx = np.random.randint(m)

            # Set the point at the random index as the centroid for the ith index.
            self.centroids[i] = X[idx]

    def _find_clusters(self, X):

        # Set all the cluster to empty.
        self.clusters = [[] for _ in range(self.k)]

        for i in range(len(X)):

            # Get the point.
            point = X[i]

            # Determine the cluster for this point.
            cluster = self._determine_cluster(point)

            # Add the point to the respective cluster.
            self.clusters[cluster].append(point)

    def _update_centroids(self):

        for i in range(self.k):

            # Get the points as numpy array.
            points = np.array(self.clusters[i])

            # Update the centroid by taking the mean of all the points in the
            # cluster.
            self.centroids[i] = [np.mean(points[:,0]), np.mean(points[:,1])]

    def fit(self, X, iterations=1000):

        # Initialize the centroids.
        self._init_centroids(X)

        # Store the old centroids.
        old_centroids = self.get_centroids().copy()

        if iterations == 'inf':

            print('Running with infinite iterations...')

            # Goes into the infinite loop.
            iterator = iter(int, 1)
        else:

            # Returns the range of values.
            iterator = range(iterations)

        for _ in iterator:

            # Find the clusters.
            self._find_clusters(X)

            # Update the centroids using the clusters obtained.
            self._update_centroids()

            # Get the new centroid.
            new_centroids = self.get_centroids()

            # Break the loop if there is no change in the centroids.
            if np.count_nonzero(old_centroids - new_centroids) == 0:
                break

            # Update the old centroids.
            old_centroids = new_centroids.copy()


    def get_centroids(self):

        return self.centroids

    def _determine_cluster(self, point):

        # Set the maximum distance.
        dist = float('inf')

        # Set the random initial cluster
        cluster = -1

        for i in range(self.k):

            # Get the i-th centroid from the k clusters.
            centroid = self.centroids[i]

            # Compute the distance.
            d = self.distance_formula(point[0], centroid[0], point[1], centroid[1])

            if d < dist:
                # Update the distance and cluster if the nearest cluster is found.
                dist = d
                cluster = i

        return cluster

    def predict(self, X):

        preds = []

        for i in range(len(X)):

            # Get the point.
            point = X[i]

            #
            preds.append(self._determine_cluster(point))

        return np.array(preds)

    def euclidean_distance(self, lat1, lat2, long1, long2):

        return sqrt((lat2 - lat1)**2 + (long2 - long1)**2) * 3956.0 * pi / 180

    def set_centroids(self, centroids):

        self.centroids = centroids
    def haversine_distance(self, lat1, lat2, long1, long2):
        """
        Returns the distance between two points on earth.
        """

        # Get the radians from the degrees.
        long1 = radians(long1)
        long2 = radians(long2)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        # Haversine formula
        diff_long = long2 - long1
        diff_lat = lat2 - lat1

        a = sin(diff_lat / 2)**2 + cos(lat1) * cos(lat2) * sin(diff_long / 2)**2

        c = 2 * asin(sqrt(a))

        # For Radius of earth in kilometers. Use 6371 for kilometers.
        result = c * 3956

        return result

def get_geometry(points):

    geometry = []

    for i in range(len(points)):

        geometry.append(Point((points[i][2], points[i][1])))

    return geometry

if __name__ == '__main__':

    df = pd.read_csv('zipcodes.csv', index_col=False)

    points = df.to_numpy()[:,[1, 2]]

    k = 50

    kmeans = KMeans(k=k)

    # kmeans.fit(points)

    new_weights = np.array([[43.07245878, -84.39214912],
     [42.38147288, -74.00695386],
     [32.95584781, -97.50016955],
     [36.36576443, -84.99338123],
     [44.00004197, -93.99913292],
     [40.21580017, -94.84209526],
     [45.5368447, -89.79890367],
     [44.10971449, -73.13946343],
     [42.3067397, -71.29921157],
     [40.1284961, -75.94571755],
     [37.64113636, -81.76613433],
     [42.04121672, -89.08077669],
     [46.25374878, -122.3486878],
     [59.51108717, -139.32443954],
     [38.27136055, -77.10497185],
     [29.34165331, -97.26186632],
     [33.96428921, -104.46680051],
     [41.62491734, -98.6197263],
     [46.97223808, -97.79161007],
     [40.12205669, -84.51199016],
     [40.67871054, -81.57127609],
     [45.99501332, -105.92404438],
     [41.59511324, -72.67679897],
     [45.17060048, -68.57649174],
     [20.86258054, -157.39302369],
     [36.39268657, -94.272947],
     [40.1353969, -79.35314131],
     [42.32575107, -78.47051643],
     [38.61841564, -121.53035847],
     [36.74089683, -88.85297613],
     [39.22339154, -90.76345086],
     [27.46373031, -81.41498203],
     [31.11192941, -83.28861455],
     [34.2895016, -81.63898763],
     [18.25087361, -66.2280177],
     [41.10618562, -112.1020483],
     [40.80860218, -74.17371631],
     [34.3194208, -117.66792618],
     [36.869336, -98.41571261],
     [34.57441617, -90.86206251],
     [33.97856149, -111.1418522],
     [42.78811147, -76.03384572],
     [39.11661086, -86.95820907],
     [39.46767352, -105.23224427],
     [46.62519935, -115.49510453],
     [44.00420206, -70.53507211],
     [31.63795052, -93.57116064],
     [33.56859552, -85.92297279],
     [30.96474853, -89.45555448],
     [35.63763617, -78.40790344]])

    kmeans.set_centroids(new_weights)

    weights = np.array([[43.10649244, -84.4161915],
     [44.03026845, -72.84166862],
     [35.33953072, -91.71887809],
     [40.5975789, -82.62212451],
     [42.35459522, -93.31426099],
     [38.11587259, -95.09669018],
     [45.02358117, -89.60638654],
     [44.0929086, -70.39173352],
     [42.28913147, -71.22572708],
     [39.61031357, -75.40887558],
     [37.61579688, -82.07626878],
     [41.71278739, -88.49033975],
     [46.40460846, -116.85263487],
     [46.53617998, -122.84589215],
     [36.5498764, -76.95341859],
     [29.55700294, -97.32818396],
     [34.24651053, -97.26777868],
     [40.84737255, -97.92286393],
     [45.81786832, -95.09870855],
     [38.9226147, -77.53232779],
     [42.34599059, -74.20261036],
     [46.43500744, -101.13505642],
     [41.76341143, -72.6990654],
     [13.758331, 144.9483545],
     [49.45714568, -156.18910008],
     [33.9315436, -87.50803511],
     [40.83225341, -76.40417898],
     [42.31002132, -78.39950911],
     [38.63959109, -121.54299996],
     [39.42739134, -85.42526258],
     [39.31200048, -90.84830911],
     [27.79790432, -81.50011415],
     [31.55684105, -85.03435635],
     [33.25596125, -81.62442055],
     [18.25087361, -66.2280177],
     [40.64289656, -112.06126422],
     [40.80790142, -74.09033733],
     [34.33639561, -117.58146706],
     [33.67468313, -102.25759605],
     [37.40206443, -88.06906736],
     [33.79328758, -109.97304999],
     [43.15738, -75.85865277],
     [40.28601561, -79.94898735],
     [39.17232343, -105.11023993],
     [46.03893842, -109.56917327],
     [45.15967208, -68.49969987],
     [31.83254361, -94.02694045],
     [35.03554684, -84.37559692],
     [31.02582999, -90.19191594],
     [35.65450412, -79.71718455]])

    kmeans_eu = KMeans(k=k, distance_formula='euclidean')
    # kmeans_eu.fit(points, iterations='inf')

    kmeans_eu.set_centroids(weights)

    print(len(points), len(df))

    mycoord = [33.958230, -84.505125]

    cluster = str(kmeans_eu.predict([mycoord])[0])

    data = None

    with open('clustered_zip.json', 'r') as f:

        data = json.load(f)


    def euclidean_distance(lat1, lat2, long1, long2):

        return sqrt((lat2 - lat1)**2 + (long2 - long1)**2) * 3956.0 * pi / 180

    distances = np.empty(len(data[cluster]))
    zips = np.empty(len(data[cluster]), dtype='object')

    i = 0
    for zipcode, coord in data[cluster].items():

        distances[i] = euclidean_distance(coord[0], mycoord[0], coord[1], mycoord[1])
        zips[i] = str(zipcode)

        i += 1

    print(zips[np.argmin(distances)])

