from natural_language_sentiment import *
from vision_face import *
from vision_multiple_objects import *
import glob


def main_func(word, recipient):
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
        return for_family
    elif recipient == 'friends':
        return for_friends


def word_connotation(word):
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
        print(list_objects)
        for objects in list_objects:
            if word in objects:
                new_photos.append(objects)
    return new_photos







