"""
    songs.py
    Nicholas S. Bradford
    April 2016

    Contains classes for creating and comparing songs.
    
"""

import numpy as np
import mir

#==================================================================================================

class Song(object):
    def __init__(self, name, filepath, verses, chorus):
        """ Constructor."""
        self.name = name
        self.filepath = filepath
        self.verses = verses # the section markers
        self.chorus = chorus # the section markers
        self.data = None
        self.fs = None
        self.verses_section = None
        self.chorus_section = None

    def load(self):
        """ Setup the Song."""
        self.data, self.fs = mir.load_song(self.filepath) # duration=173.0
        self.verses_section = Song.identify_sections(self.data, self.fs, self.verses)
        self.chorus_section = Song.identify_sections(self.data, self.fs, self.chorus)
        #return self.data, self.fs

    def get_features(self, frame_duration):
        """ Split the songs into Frames and get their Feature Vectors."""
        return (mir.extract_features(Song.create_frames(self.verses_section, self.fs, frame_duration)), 
                mir.extract_features(Song.create_frames(self.chorus_section, self.fs, frame_duration)))

    @staticmethod
    def identify_sections(data, fs, markers):
        """ 
        Args:
            markers: set of tuples
        Returns:
            section: nparray with only the selected sections of the song
        """
        sections = []
        for begin, end in markers:
            sections.append(data[(begin * fs) : (end * fs)])
        section = np.concatenate(sections)
        return section

    @staticmethod
    def create_frames(data, fs, frame_duration):
        """ Create a list of frames from the song.
        Args:
            song: array containing the audio signal
            fs: corresponding sampling frequency
            frame_duration: seconds per frame
            song_duration: seconds that the songs lasts for
        Returns:
            list of frames
        """
        frame_size = int(frame_duration * fs) # one second
        frames = []
        for i in xrange(0, len(data), frame_size):
            frames += [np.array(data[i : i + frame_size])]
        #frames = librosa.util.frame(data, frame_length=frame_size, hop_length=frame_size)
        return frames

#==================================================================================================

class SongComparison(Song):
    def __init__(self, name, verses, chorus, filepath_verses, filepath_chorus):
        """ Constructor."""
        super(SongComparison, self).__init__(name, None, verses, chorus)
        self.filepath_verses = filepath_verses
        self.filepath_chorus = filepath_chorus

    def load(self):
        self.verses_data, self.fs = mir.load_song(self.filepath_verses)
        self.verses_section = Song.identify_sections(self.verses_data, self.fs, self.verses)
        
        self.chorus_data, self.fs = mir.load_song(self.filepath_chorus)
        self.chorus_section = Song.identify_sections(self.chorus_data, self.fs, self.chorus)
