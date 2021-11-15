import os
from PIL import Image, ImageOps
from custom_augmenter_2 import augmentation

directory_images = 'D:/trained_models/Cleaned_Training_Data_No_Augmentation/images'
directory_masks = 'D:/trained_models/Cleaned_Training_Data_No_Augmentation/masks'
directory_images_not_cleaned = 'D:/trained_models/No_Cleaned_Training_Data_No_Augmentation/images'
directory_masks_not_cleaned = 'D:/trained_models/No_Cleaned_Training_Data_No_Augmentation/masks'
images = os.listdir(directory_images)
#images = [f.lower() for f in images]   # Convert to lower case
#sorted(images)
masks = os.listdir(directory_masks)
images_not_cleaned = os.listdir(directory_images_not_cleaned)
masks_not_cleaned = os.listdir(directory_masks_not_cleaned)
directory_image0 = directory_images + '/' + images[0]
image0 = Image.open(directory_image0)
width, height = image0.size
directory_pink = 'background.png'
directory_black = 'black.png'
''' 
pink = Image.open(directory_pink)
pink_nc = pink.copy()
black = Image.open(directory_black)
black_nc = black.copy()
black = ImageOps.grayscale(black)
black_nc = ImageOps.grayscale(black_nc)
pix_pink = pink.load()
pix_pink_nc = pink_nc.load()
pix_black = black.load()
pix_black_nc = black_nc.load()
'''

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
    pink = Image.open(directory_pink)
    pink_nc = pink.copy()
    black = Image.open(directory_black)
    black_nc = black.copy()
    black = ImageOps.grayscale(black)
    black_nc = ImageOps.grayscale(black_nc)
    pix_pink = pink.load()
    pix_pink_nc = pink_nc.load()
    pix_black = black.load()
    pix_black_nc = black_nc.load()

    image_name = images[i]
    mask_name = masks[i]
    image_not_cleaned_name = images_not_cleaned[i]
    mask_not_cleaned_name = masks_not_cleaned[i]

    image_directory = directory_images + '/' + image_name
    mask_directory = directory_masks + '/' + mask_name
    image_nc_dir = directory_images_not_cleaned + '/' + image_not_cleaned_name
    mask_nc_dir = directory_masks_not_cleaned + '/' + mask_not_cleaned_name
     #pix_original = Image.open(image_directory).load()
    image = Image.open(image_directory)
    mask = Image.open(mask_directory)
    img_nc = Image.open(image_nc_dir)
    mask_nc = Image.open(mask_nc_dir)
    if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
        mask = ImageOps.grayscale(mask)
        mask_nc = ImageOps.grayscale(mask_nc)

    augmentation(image_name, image, img_nc, pink, pink_nc, pix_pink, pix_pink_nc, mask, mask_nc, black, black_nc, pix_black, pix_black_nc, width, height)
''' 
for x in range(width):
    for y in range(height):
        if mask.load()[x, y] != 0 and mask.load()[x, y] != 253:
            print(mask.load()[x, y])
'''