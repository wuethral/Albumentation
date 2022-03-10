from PIL import Image
import random
import os


def zoom_in(background_name, background, width, height, i):

    random_nr = 1 - 0.5 * random.random()
    left = int(width/2 - ((random_nr * width)) / 2)
    top = int(height/2 - ((random_nr * height)) / 2)
    right = int(width/2 + ((random_nr * width)) / 2)
    bottom = int(height/2 + ((random_nr * height)) / 2)
    background = background.crop((left, top, right, bottom))
    newsize = (width, height)
    background = background.resize(newsize)
    path = 'D:/Project_Eye_Tracking/Backgrounds_zoom_in/' + str(i) + '_' + background_name
    background.save(path)

background_folder_path = 'D:/Project_Eye_Tracking/Backgrounds'
background_names = os.listdir(background_folder_path)

for i in range(10):

    for background_name in background_names:
        background_path = background_folder_path + '/' + background_name
        background = Image.open(background_path)
        width,height = background.size
        zoom_in(background_name, background, width, height, i)