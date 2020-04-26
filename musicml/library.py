"""
    library.py
    Nicholas S. Bradford
    April 2016

    Contains relevant markers for song sections.
    
"""

from songs import Song, SongComparison

#==================================================================================================
# Songs       

#================================================
sweetdreams_verses = [
    (0, 63)
]
sweetdreams_chorus = [
    (64, 95)
]

#================================================
monster_verses = [
    (0, 14)
]
monster_chorus = [
    (44, 65)
]

#================================================
complete_monster_verse = [
    (14, 44),
    (65, 89)
]
complete_monster_chorus = [
    (44, 65),
    (89, 117),
    (138, 173)
]

#================================================
howyouloveme_verses = [
    (8, 38)
]
howyouloveme_chorus = [
    (68, 97)
]

#================================================
feelgood_verses = [
    #(12, 39)
    #(39, 71)
    (39, 52)
]
feelgood_chorus = [
    (71, 84)
    #(71, 100)
]

#================================================
# maledictus
confutatis_chorus = [
    (1, 17),
    (36, 52)
    # (0, 18),
    # (35, 54)
]
# boca me
confutatis_verses = [
    (19, 33),
    (55, 89)
    # (18, 34),
    # (54, 90)
]
# boca me extra
confutatis_bridge = [
    (90, 160)
]

#================================================
# soft verse
one_verses = [
    (19, 105),
    (105, 134)
]
# metal bridge
one_chorus = [
    #(278, 320)# 4:33 - 5:20, 
    (320, 443) #5:20-5:46, 7:23 guitar solo
]

#================================================

champions_verses = [
    (1, 24), #23?
    (76, 100) # 110?
]
champions_chorus = [
    (34, 66),
    (110, 174)
]

#================================================
remember_verses = [
    (34, 100)
]
remember_chorus = [
    (22, 33),
    (101, 111),
    (180, 191)
]

#================================================
entire_confutatis = [(0, 90)]
entire_monster = [(0, 173)]

#==================================================================================================
# Complete Song data


sweetdreams = Song('sweetdreams', 'input/sweetdreams.wav', 
    verses=sweetdreams_verses, 
    chorus=sweetdreams_chorus)
monster = Song('Monster', 'input/monster.wav', 
    verses=monster_verses, 
    chorus=monster_chorus)
howyouloveme = Song('How You Love Me', 'input/howyouloveme.wav', 
    verses=howyouloveme_verses, 
    chorus=howyouloveme_chorus)
feelgood = Song('Feel Good Inc.', 'input/feelgood.wav', 
    verses=feelgood_verses, 
    chorus=feelgood_chorus)
confutatis = Song('Confutatis Maledictis', 'input/confutatis.wav',
    verses=confutatis_verses,
    chorus=confutatis_chorus)
one = Song('One', 'input/one.wav',
    verses=one_verses,
    chorus=one_chorus)
champions = Song('We are the Champions', 'input/champions.wav',
    verses=champions_verses,
    chorus=champions_chorus)
remember = Song('Remember the Name', 'input/remember.wav',
    verses=remember_verses,
    chorus=remember_chorus)

rock_v_classical = SongComparison(
    name='Monster v Confutatis',
    verses=monster_verses,
    chorus=confutatis_chorus,
    filepath_verses='input/monster.wav',
    filepath_chorus='input/confutatis.wav')

pop_v_classical = SongComparison(
    name='HowYouLoveMe v Confutatis',
    verses=howyouloveme_verses,
    chorus=confutatis_chorus,
    filepath_verses='input/howyouloveme.wav',
    filepath_chorus='input/confutatis.wav')

pop_v_rock_choruses = SongComparison(
    name='HowYouLoveMe v Monster',
    verses=howyouloveme_chorus,
    chorus=monster_chorus,
    filepath_verses='input/howyouloveme.wav',
    filepath_chorus='input/monster.wav')

rap_v_classical = SongComparison(
    name='RememberTheName v Confutatis',
    verses=remember_verses,
    chorus=confutatis_chorus,
    filepath_verses='input/remember.wav',
    filepath_chorus='input/confutatis.wav')

entire_monster_v_confutatis = SongComparison(
    name='Entire Monster v Confutatis',
    verses=entire_monster,
    chorus=entire_confutatis,
    filepath_verses='input/monster.wav',
    filepath_chorus='input/confutatis.wav')
