# Musical Machine Learning

This project created a foundation for future work by WPI students in music information retrieval and machine learning. A Python system was first constructed to extract variable-length features from audio files. The problem of determining song structure was then approached with both supervised and unsupervised learning algorithms.

### Installation

Optionally use virtualenv, and install requirements:

    $ pip install requirements.txt

### Usage

Demo, which loads up the song "One" and produces a visualization similar to the below:

    $ python musicml.py -g

Full usage:
    
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
      -g, --is_not_graph    Do not graph output.
      -c, --is_cluster      Run clustering.
      -e, --is_elbow        Run elbow method for KMeans clustering.

### Using your own song

* Put your input .wav file in the /input folder (Warning: providing songs with COMPLETELY blank sections will mess with the numerical libraries)
* Create a new instance of `Song` in `library.py` following the convention - the songs and verses are sets up tuples representing the start and end (in seconds) of a song verse or chorus.
* Add a reference to your at index 0 in `analyze.py`'s `Analyst.song_library` list
* Run demo (defaults to picking the first song in the song_library)
    
### Future Work

* Refactor to run in a Jupyter notebook
* Segment song and smooth to isolate Verse, Chorus sections (i.e. that way you don't have to manually specify choruses and verses in the configs)
* Run anomaly detection before K-means to reduce outlier effects


## The End Result

Song Visualization of "One" by Metallica.

<img src="/output/demo/art.jpg" alt="Monster scatterplot" width="1280" height="800"/>


## Workflow

### The Processed Data

<img src="/output/demo/scatter__2016-04-27_12-40-10.png" alt="Monster scatterplot" width="400" height="400"/>

### Supervised Learning

K-nearest neighbor (K=5)

<img src="/output/demo/example.png" alt="Monster scatterplot" width="400" height="400"/>

### Unsupervised Learning

K-means clustering algorithm:

<img src="/output/demo/kmeans_monster.png" alt="K-means on Monster" width="400" height="400"/>


