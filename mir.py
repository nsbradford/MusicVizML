"""
    mir.py
    Nicholas S. Bradford
    April 2016

    Contains functions for performing MIR (music information retrieval).

"""

import numpy as np
import librosa
import time

def load_song(file_path):
    return librosa.load(file_path)


def old_feature_vector(signal):
    """
    Returns:
        A 2x1 feature vector for the signal.
    """
    return [
        librosa.feature.zero_crossing_rate(signal)[0, 0],
        librosa.feature.spectral_centroid(signal)[0, 0]
    ]

def feature_vector(signal):
    """
    Returns:
        A 2x1 feature vector for the signal.
    """
    return [
        (librosa.feature.zero_crossing_rate(signal).mean() / librosa.feature.spectral_centroid(signal).mean()),
        librosa.feature.spectral_centroid(signal).mean()
    ]

def extract_features(frames):
    """ 
    Args:
        frames: list of nparray frames
    Returns:
        list of feature vectors (one for each frame)
    """
    return [feature_vector(x) for x in frames]

def output_wav(filepath, data, fs):
    librosa.output.write_wav('output/verses.wav', verses, fs)
