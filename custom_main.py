import os
from PIL import Image, ImageOps
from custom_augmenter import augmentation

directory_images = 'D:/trained_models/No_Cleaned_Training_Data_No_Augmentation/images'
directory_masks = 'D:/trained_models/No_Cleaned_Training_Data_No_Augmentation/masks'
images = os.listdir(directory_images)
masks = os.listdir(directory_masks)
directory_image0 = directory_images + '/' + images[0]
image0 = Image.open(directory_image0)
width, height = image0.size
directory_pink = 'background.png'
directory_black = 'black.png'
pink = Image.open(directory_pink)
black = Image.open(directory_black)
black = ImageOps.grayscale(black)
pix_pink = pink.load()
pix_black = black.load()
''' 
for x in range(width):
    for y in range(height):
        if pix_black[x, y] != 0:
            print(pix_black[x, y])
print('ha')
'''
''' 
print('hi')
for x in range(height):
    for y in range(width):
        print(pix_black[x, y])
'''

for i in range(len(images)):
    image_name = images[i]
    mask_name = masks[i]
    image_directory = directory_images + '/' + image_name
    mask_directory = directory_masks + '/' + mask_name
    #pix_original = Image.open(image_directory).load()
    image = Image.open(image_directory)
    mask = Image.open(mask_directory)
    if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
        mask = ImageOps.grayscale(mask)

    augmentation(image_name, image, pink, pix_pink, mask, black, pix_black, width, height)
''' 
for x in range(width):
    for y in range(height):
        if mask.load()[x, y] != 0 and mask.load()[x, y] != 253:
            print(mask.load()[x, y])
'''