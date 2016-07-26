"""
    cluster.py
    Nicholas S. Bradford
    April 2016

    Unsupervised learning module.
    
"""

import numpy as np
from sklearn.cluster import KMeans

import matplotlib.pyplot as plt

def calculate_elbow_method(X):
    """ Run calculations for the elbow method of choosing number of clusters."""
    inertia = []
    for i in xrange(15): #range(len(X)):
        print i
        kmeans = KMeans(n_clusters=(i+1))
        kmeans.fit([np.array(x).ravel() for x in X])
        inertia.append(kmeans.inertia_)
    return inertia

def run_clustering_test(train_X, test_X, train_Y, test_Y):
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(train_X)
    reduced_data = train_X
    #train_Y = [x+3 for x in train_Y]

    # Step size of the mesh. Decrease to increase the quality of the VQ.
    h = .02     # point in the mesh [x_min, m_max]x[y_min, y_max].

    # Plot the decision boundary. For that, we will assign a color to each
    x_min, x_max = reduced_data[:, 0].min() - 1, reduced_data[:, 0].max() + 1
    y_min, y_max = reduced_data[:, 1].min() - 1, reduced_data[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # Obtain labels for each point in mesh. Use last trained model.
    Z = kmeans.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure(1)
    plt.clf()
    plt.imshow(Z, interpolation='nearest',
               extent=(xx.min(), xx.max(), yy.min(), yy.max()),
               cmap=plt.cm.Paired,
               aspect='auto', origin='lower')

    plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=train_Y, s=20)
    # Plot the centroids as a white X
    centroids = kmeans.cluster_centers_
    plt.scatter(centroids[:, 0], centroids[:, 1],
                marker='x', s=169, linewidths=3,
                color='w', zorder=10)
    plt.title('K-means clustering.\n'
              'Centroids are marked with white cross')
    plt.xlim(x_min, x_max)
    plt.ylim(y_min, y_max)
    plt.xticks(())
    plt.yticks(())
    plt.show()
    