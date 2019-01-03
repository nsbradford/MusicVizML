"""
    Analyst.py
    Nicholas S. Bradford
    April 2016

    Dependencies:
        Anaconda
        librosa - http://bmcfee.github.io/librosa/index.html
        essentia - http://essentia.upf.edu/documentation/installing.html
            not supported on Windows!!

    Supervised: predict whether a given segment is part of Verse or Chorus
        Divide song into Verse/Chorus sections
        Combine all alike sections
        Chop up sections into [1]-second frames
            Use scatterplot to visualize the differences (zero-crossing rate, 
                spectral center, amplitude...)
        Feed 75 percent of frames into learning algorithm as Training set
        Feed 25 percent of frames into learning algorithm as Test set, and report results.
            Potential Algorithms: 
                SVM: must be regularized, should perform well on sparse data
                LinearRegression
                K-NN
                Naive Bayes
                Neural Networks
                AdaBoost (Ensemble)
                *Random Forests (Ensemble)
                *Decision Trees
            Then move onto multiclass algorithms!
    Unsupervised: try to cluster songs into different segments

    Week 6:
        Fixed scatterplot issues (legends, wrongly labeled data, ...)
        Made graphs of before/after using the new linear feature
        More songs:
            Confutatis Meledictis
            We Are the Champions
            One
            Remember the Name
        Output graphs:
            Produce multiple copies of output files (so you can choose your favorite)
            Experiment with colors
        Run Test (using monster.wav as a baseline)
            Vary percent of data used in the training set;
                Originally 75%:                     .90 accurate for both K-NN and SVM
                Minimal K-NNperformance hit at 25%  .88 accurate
                K-NN slipping at 10%:               .76 accurate
                K-NN totally gone at 5%:            .58 accurate
        Structural:
            Added more command-line arguments
            Run KMeans clustering:
                On Monster/Confutatis, comparable results to LinearRegression (not good - ~60%)
                Elbow Method suggests # of clusters per song:
                    Monster         3-4 
                    HowYouLoveMe    3-4
                    FeelGood        3
                    Confutatis      2
                    One             3
                    Champtions      2
                    Remember        3
            Use "average" features computed over the entire frame: MAJOR improvement!
            Add option for ALL songs to be tested
            Compare different songs together (SongComparison class)
                Not surprisingly, this is a much easier problem to solve (nearly perfect performance)
                Clustering works very well here as well
                Even with Entire Monster v Confutatis @1.0 second test, separates very cleanly
    TODO:
        Output graphs:
            Produce two different graphs: one artsy, one for actual data
        Major:
            *Use SVM with linear kernel (instead of RBF) as a better approximation of "true" clustering
            *Cluster an entire song in 1-s segements, then use a Gaussian KDE to smooth out classification.
                This can then be used to actually mark "segments" of a song
            *Create website where people can upload a MIDI file, and then listen to RNN improvise over it
        For future people:
            wiki entry
            README
            IPython notebook demo (https://ipython.org/notebook.html)
    
    Long-term:
        Working on this Verse/Chorus system:
            Find additional features other than spectral centroid and zero-crossing rate
                Play with how the features are generated and averaged
            Include outlier detection in the data preprocessing stage
                (http://scikit-learn.org/stable/modules/outlier_detection.html)
            Optimize the different classifiers
            Optimize song loading times (store in database? alternative form?)
            Add option of multiple sections (bridge?)       
        Expansions:
            Develop an actual algorithm for finding switches from Verse -> Chorus (already discovered by others)
            Train a massive Deep Neural Net to try to automatically distinguish between parts
        Composition
            Create a LSTM recurrent neural net to learn from MIDI input
            Combine with Verse/Chorus algorithm/work to give songs more structure



"""

import argparse
from musicml.analyze import Analyst

#==================================================================================================

def main():
    """ """
    print "\nFinished imports."

    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--is_all_songs', action='store_true',
            help='Run test on all songs.')

    parser.add_argument('-s', '--song_index', default=0, type=int, 
            choices=[x for x in xrange(len(Analyst.song_library))],
            help='Index of the song in song_library.')
    parser.add_argument('-a', '--n_art_graphs', default=1, type=int,
            help='Number of output graphs.')
    parser.add_argument('-p', '--is_plot_data', action='store_true',
            help='Plot the raw data.')
    parser.add_argument('-g', '--is_not_graph', action='store_false',
            help='Graph output.')
    parser.add_argument('-c', '--is_cluster', action='store_true',
            help='Run clustering.')
    parser.add_argument('-e', '--is_elbow', action='store_true',
            help='Run elbow method for KMeans clustering.')
    args = parser.parse_args()

    test_songs = []
    if args.is_all_songs:
        test_songs += range(len(Analyst.song_library))
    else:
        test_songs.append(args.song_index)

    for i in test_songs:
        for algo in Analyst.algo_classes:
            Analyst.primary_function(song_index=i, #args.song_index, #=i
                                    algo=algo,
                                    n_art_graphs=args.n_art_graphs,
                                    n_test_runs=100,
                                    is_plot_data=args.is_plot_data,
                                    is_graph=not args.is_not_graph,
                                    is_cluster=args.is_cluster,
                                    is_elbow=args.is_elbow)

#==================================================================================================

if __name__ == "__main__":
    main()
