from PIL import Image, ImageOps
import random
import os
import cv2 as cv

def translate(img,mask, screw_name):

    pink = cv.imread('background.png')
    black = cv.imread('black.png')
    width = black.shape[1]
    height = black.shape[0]
    random_nr = random.random()

    black = cv.cvtColor(black, cv.COLOR_BGR2GRAY)


    random_trans_number = int(0.2*height + (random.random() * 0.3 * height))
    print(random_trans_number)
    for y in range(height- random_trans_number):
        for x in range(width):
            black[y + random_trans_number, x] = mask[y, x]
            pink[y + random_trans_number, x] = img[y, x]

    for x in range(width):
        for y in range(height):
            if black[y,x] != 0:
                black[y,x] = 249
    save_name_image = 'D:/Project_Eye_Tracking/DataSetAugmentation/hands/translated/images/' + screw_name
    save_name_mask = 'D:/Project_Eye_Tracking/DataSetAugmentation/hands/translated/masks/' + screw_name
    cv.imwrite(save_name_image, pink)
    cv.imwrite(save_name_mask, black)

hands_folder_path = 'D:/Project_Eye_Tracking/DataSetAugmentation/hands/images'
hands_mask_path = 'D:/Project_Eye_Tracking/DataSetAugmentation/hands/masks'
hands_names = os.listdir(hands_folder_path)
for hand_name in hands_names:
    mask_name = hand_name.split('rot_')[0] + 'rot_mask' + hand_name.split('rot')[1]
    hands_path = hands_folder_path + '/' + hand_name
    image = cv.imread(hands_path)
    mask_path = hands_mask_path + '/' + mask_name
    mask = cv.imread(mask_path)
    mask = cv.cvtColor(mask, cv.COLOR_BGR2GRAY)
    translate(image,mask,hand_name)
