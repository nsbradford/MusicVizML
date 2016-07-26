"""
    visual.py
    Nicholas S. Bradford
    April 2016

    Contains functions for visualizing the data and results.

"""

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import numpy as np
import time
from sklearn.preprocessing import StandardScaler

from cluster import *


#==================================================================================================

def graph_elbow_method(song_data):
    print "Calculating for elbow method..."
    inertia = calculate_elbow_method(song_data)
    plt.figure("Elbow Method")
    plt.plot(inertia)
    plt.show()

def histograms(verses_features, chorus_features):
    """ Plot histogram of data."""
    verses_features = np.array(verses_features)
    chorus_features = np.array(chorus_features)
    plt.hist(verses_features[:,0], color='b', range=(0, 0.1))
    plt.hist(chorus_features[:,0], color='r', range=(0, 0.1))
    plt.legend(('verses_features', 'chorus_features'))
    plt.xlabel('Zero Crossing Rate')
    plt.ylabel('Count')
    plt.show()

def scatterplot(verses_features, chorus_features):
    """ Plot scatterplot of data."""
    size = 6
    linewidth = 0.4

    print "Scatterplot..."
    feature_table = np.vstack((verses_features, chorus_features)) #np.array(chorus_features) #
    training_features = StandardScaler().fit_transform(feature_table)

    #print training_features.min(axis=0)
    #print training_features.max(axis=0)
    plt.scatter(training_features[:len(verses_features),0], 
        training_features[:len(verses_features),1], s=size, lw=linewidth, c='r')
    plt.scatter(training_features[len(verses_features):,0], 
        training_features[len(verses_features):,1], s=size, lw=linewidth, c='b')
    plt.xlabel('Zero Crossing Rate / Spectral Centroid') #plt.xlabel('Zero Crossing Rate')
    plt.ylabel('Spectral Centroid')
    plt.legend(('verses_features', 'chorus_features'))
    plt.savefig('output/scatter__' + str(time.strftime("%Y-%m-%d_%H-%M-%S")) + '.png', 
    bbox_inches='tight', format='png', dpi=300) # dpi=1200 svg
    plt.show()

#==================================================================================================

def plot_classification(song_name, clf, X_train, y_train, X_test, y_test, X, y):
    """ Plot classification boundary."""
    
    color_maps_raw = """Spectral, summer, coolwarm, Wistia_r, pink_r, Set1, Set2, Set3, 
        brg_r, Dark2, prism, PuOr_r,
        afmhot_r, terrain_r, PuBuGn_r, RdPu, gist_ncar_r, gist_yarg_r, Dark2_r, YlGnBu,
        RdYlBu, hot_r, gist_rainbow_r, gist_stern, PuBu_r, cool_r, cool, gray, copper_r, 
        Greens_r, GnBu, gist_ncar, spring_r, gist_rainbow, gist_heat_r, Wistia, OrRd_r,
        CMRmap, bone, gist_stern_r, RdYlGn, Pastel2_r, spring, terrain, YlOrRd_r, Set2_r, 
        winter_r, PuBu, RdGy_r, spectral, rainbow, flag_r, jet_r, RdPu_r, gist_yarg,
        BuGn, Paired_r, hsv_r, bwr, cubehelix, Greens, PRGn, gist_heat, spectral_r, Paired, 
        hsv, Oranges_r, prism_r, Pastel2, Pastel1_r, Pastel1, gray_r, jet, Spectral_r, gnuplot2_r, 
        gist_earth, YlGnBu_r, copper, gist_earth_r, Set3_r, OrRd, gnuplot_r, ocean_r, brg, gnuplot2, 
        PuRd_r, bone_r, BuPu, Oranges, RdYlGn_r, PiYG, CMRmap_r, YlGn, binary_r, gist_gray_r, Accent, 
        BuPu_r, gist_gray, flag, bwr_r, RdBu_r,
        BrBG, Reds, Set1_r, summer_r, GnBu_r, BrBG_r, Reds_r, RdGy, PuRd, Accent_r, Blues,
        autumn_r, autumn, cubehelix_r, nipy_spectral_r, ocean, PRGn_r, Greys_r, pink,
        binary, winter, gnuplot, RdYlBu_r, hot, YlOrBr, coolwarm_r, rainbow_r, Purples_r,
        PiYG_r, YlGn_r, Blues_r, YlOrBr_r, seismic, Purples, seismic_r, RdBu, Greys,
        BuGn_r, YlOrRd, PuOr, PuBuGn, nipy_spectral, afmhot"""
    #color_maps = "".join(color_maps_raw.split()).split(',')
    color_maps = ['RdBu'] #, 'pink']#['RdBu','gray', 'pink', 'PuBu', 'Reds', 'RdGy', 'Purples']

    print "Plot classification..."
    size = 20
    alpha = 1.0
    linewidth = 0.5

    h = .01
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    for color_map in color_maps:

        # just plot the dataset first
        #cm = plt.cm.RdBu
        cm = plt.cm.get_cmap(color_map)
        cm_bright = ListedColormap(['#FF0000', '#0000FF']) # red and blue
        #cm_bright = ListedColormap(['#FF00FF', '#ffdf00']) # 

        ax = plt.subplot()
        score = clf.score(X_test, y_test)

        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        if hasattr(clf, "decision_function"):
            Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
        else:
            Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

        # Plot also the training points and testing points
        ax.scatter(X_train[:, 0], X_train[:, 1], s=size, lw=linewidth, c=y_train, cmap=cm_bright, 
            alpha=alpha)
        ax.scatter(X_test[:, 0], X_test[:, 1], s=size, lw=linewidth, c=y_test, cmap=cm_bright, 
            alpha=alpha)
        #ax.legend(('verses_features', 'chorus_features'))
        ax.legend((mpatches.Rectangle((0,0),1,1,color='b'), 
            mpatches.Rectangle((0,0),1,1,color='r')), ('Chorus', 'Verse'))

        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        ax.contourf(xx, yy, Z, cmap=cm, alpha=0.8)

        ax.set_xlim(xx.min(), xx.max())
        ax.set_ylim(yy.min(), yy.max())
        ax.set_xticks(())
        ax.set_yticks(())
        title = (song_name + '_' + color_map + '_' + clf.__class__.__name__ 
            + '_' + str(time.strftime("%Y-%m-%d_%H-%M-%S")))
        ax.set_title(title)
        ax.text(xx.max() - .3, yy.min() + .3, ('%.2f' % score).lstrip('0'),
                size=15, horizontalalignment='right')
        
        plt.xlabel('Zero Crossing Rate / Spectral Centroid') #plt.xlabel('Zero Crossing Rate')
        plt.ylabel('Spectral Centroid')

        print "\tSaving figure..."

        # dpi=1200 svg for high-quality
        plt.savefig('output/' + title  + '.png', bbox_inches='tight', format='png', dpi=300) 
        #plt.cla()
        #plt.show()
