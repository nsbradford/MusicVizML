# Musical Machine Learning

This project created a foundation for future work by WPI students in music information retrieval and machine learning. A Python system was first constructed to extract variable-length features from audio files. The problem of determining song structure was then approached with both supervised and unsupervised learning algorithms.

### Dependencies

* [librosa](https://github.com/librosa/librosa)
* [scikit-learn](http://scikit-learn.org/)

### Usage
    
    $ python musicml.py [-h] [-l] [-s {0,1,2,3,4,5,6,7,8,9,10,11}] [-a N_ART_GRAPHS]
                        [-p] [-g] [-c] [-e]
    
    optional arguments:
      -h, --help            show this help message and exit
      -l, --is_all_songs    Run test on all songs.
      -s {0,1,2,3,4,5,6,7,8,9,10,11}, --song_index {0,1,2,3,4,5,6,7,8,9,10,11}
                            Index of the song in song_library.
      -a N_ART_GRAPHS, --n_art_graphs N_ART_GRAPHS
                            Number of output graphs.
      -p, --is_plot_data    Plot the raw data.
      -g, --is_graph        Graph output.
      -c, --is_cluster      Run clustering.
      -e, --is_elbow        Run elbow method for KMeans clustering.
    
### TODO

* Run anomaly detection before K-means to reduce outlier effects
* Segment song and smooth to isolate Verse, Chorus sections

## The End Result

Song Visualization of "One" by Metallica.

<img src="/output/demo/art.jpg" alt="Monster scatterplot" width="1280" height="800"/>


## Workflow

### The Processed Data

<img src="/output/demo/scatter__2016-04-27_12-40-10.png" alt="Monster scatterplot" width="400" height="400"/>

### Supervised Learning

K-nearest neighbor (K=5)

<img src="/output/demo/Monster_KNeighborsClassifier.png" alt="Monster scatterplot" width="400" height="400"/>

### Unsupervised Learning

K-means clustering algorithm:

<img src="/output/demo/kmeans_monster.png" alt="K-means on Monster" width="400" height="400"/>


