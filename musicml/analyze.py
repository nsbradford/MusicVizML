"""
    analyze.py
    Nicholas S. Bradford
    April 2016

    Analyze music.
    
"""

import numpy as np
import random       # shuffle()
import sys          # stdout
import matplotlib.pyplot as plt

# working with data
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split

# machine learning algorithms
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
# from sklearn.linear_model import LinearRegression
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.ensemble import AdaBoostClassifier
# from sklearn.naive_bayes import GaussianNB

# from this project
import library
from visual import scatterplot, plot_classification, graph_elbow_method
from cluster import run_clustering_test, calculate_elbow_method

#==================================================================================================

class Analyst(object):

    song_library = [
        library.monster,
        library.howyouloveme,
        library.feelgood,
        library.confutatis,
        library.one,
        library.champions, #5
        library.remember,
        library.rock_v_classical,
        library.pop_v_classical,
        library.pop_v_rock_choruses,
        library.rap_v_classical, #10
        library.entire_monster_v_confutatis
    ]

    algo_classes = [
        #LinearRegression(), # "normalize" severely decreases performance
        #KNeighborsClassifier(n_neighbors=15),
        KNeighborsClassifier(n_neighbors=15),
        #SVC(kernel="rbf", C=1), # increase C to decrease regularization
        #SVC(kernel="rbf", C=10), # increase C to decrease regularization
        #SVC(kernel="rbf", C=100), # increase C to decrease regularization
        # DecisionTreeClassifier(),
        # RandomForestClassifier(), 
        # AdaBoostClassifier(),
        # GaussianNB(),
    ]

    def __init__(self):
        pass

    #==================================================================================================

    @staticmethod
    def primary_function(   song_index, algo, n_art_graphs=1, n_test_runs=100, is_plot_data=False, 
                            is_graph=False, is_cluster=False, is_elbow=False):
        """ """
        
        song = Analyst.song_library[song_index]

        print "\n======================================================"
        print "Load song", song.name, "..."
        song.load()

        duration_list = [0.10] #, 0.5, 1.0, 2.0]
        print '\nALGORITHM:', algo.__class__.__name__
        avg_results = {}
        for frame_duration in duration_list:
            print "\n--Begin test with duration", frame_duration
            print "Create frames and extract features..."
            verses_features, chorus_features = song.get_features(frame_duration)
            
            if is_plot_data:
                print "Plotting training/test data..."
                scatterplot(verses_features, chorus_features)

            result = Analyst.run_test(song.name, algo, verses_features, chorus_features, 
                n_art_graphs, n_test_runs, is_plot_data, is_graph, is_cluster, is_elbow)
            avg_results[frame_duration] = result
        print avg_results

    #==================================================================================================

    @staticmethod
    def run_test(song_name, algo, verses_features, chorus_features, n_art_graphs, n_test_runs,
                    is_plot_data, is_graph, is_cluster, is_elbow):
        """ Will add command-line arguments eventually."""

        print "Compute average results over", n_test_runs, "runs..."
        results = []
        for i in xrange(n_test_runs):
            # randomize
            random.shuffle(verses_features)
            random.shuffle(chorus_features)
            size = min(len(verses_features), len(chorus_features))
            v_features = verses_features[0:size]
            c_features = chorus_features[0:size]

            # verse is 0, chorus is 1
            X = np.array(v_features + c_features)
            y = np.array([0 for x in xrange(len(v_features))] + [1 for x in xrange(len(c_features))])
            X = StandardScaler().fit_transform(X)
            train_X, test_X, train_Y, test_Y = train_test_split(X, y, train_size=.75)
            algo.fit(train_X, train_Y)
            score = algo.score(test_X, test_Y)
            results.append(score)

            sys.stdout.write("\tProgress: %d%%  \r" % int(i * 100/float(n_test_runs)))
            sys.stdout.flush()

            if i >= n_test_runs - n_art_graphs:
                print i
                if is_graph:
                    plot_classification(song_name, algo, train_X, train_Y, test_X, test_Y, X, y, isScatter=False)
                if is_cluster:
                    run_clustering_test(train_X, test_X, train_Y, test_Y)
                if is_elbow:
                    graph_elbow_method(X)
                if i != n_test_runs - 1:
                    plt.cla()

        print "Average performance:", np.mean(results)
        if is_graph:
            plt.show()
        return np.mean(results)
