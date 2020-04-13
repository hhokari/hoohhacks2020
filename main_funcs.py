from natural_language_sentiment import *
from vision_face import *
from vision_multiple_objects import *
import glob
import logging

logger = logging.getLogger("main_func")


def main_func(word, recipient):
    logger.debug("word=" + word + ", recipient=" + recipient)
    photos = glob.glob(r"C:\Users\harum\PycharmProjects\hoohacks2020\photos\*.*")
    relevant_photos = object_identification(word, photos)
    connotation = word_connotation(word)
    for_family = []
    for_friends = []
    if connotation == 'positive':
        for photo in relevant_photos:
            res_emotion_comp = detect_faces(photo)
            if res_emotion_comp[1] > res_emotion_comp[0]:
                for_family.append(photo)
            else:
                for_friends.append(photo)
    else:
        for photo in relevant_photos:
            res_emotion_comp = detect_faces(photo)
            if res_emotion_comp[0] > res_emotion_comp[1]:
                for_family.append(photo)
            else:
                for_friends.append(photo)
    if recipient == 'family':
        print(for_family)
    elif recipient == 'friends':
        print(for_friends)
    logger.error("ERROR: Unknown recipient")


def word_connotation(word):
    logger.debug("word=" + word)
    connotation = sample_analyze_sentiment(word)
    if connotation >= 0.5:
        res_connotation = 'positive'
    elif 0.0 < connotation < 0.5:
        res_connotation = 'neutral'
    else:
        res_connotation = 'negative'
    return res_connotation


def object_identification(word, photos):
    new_photos = []
    for photo in photos:
        list_objects = localize_objects(photo)
        for objects in list_objects:
            if word.lower() in objects.lower():
                new_photos.append(photo)
    return new_photos
