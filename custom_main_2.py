import os
from PIL import Image, ImageOps
from custom_augmenter_2 import augmentation

double_augmenter = True
# Opening the images from folder images_pink_background and masks. These paths can of course be changed.
directory_images = 'images_pink_background'
directory_masks = 'masks'
images = os.listdir(directory_images)
masks = os.listdir(directory_masks)

if double_augmenter:
    directory_images_not_cleaned = 'images_pink_background_2'
    directory_masks_not_cleaned = 'masks_2'
    images_not_cleaned = os.listdir(directory_images_not_cleaned)
    masks_not_cleaned = os.listdir(directory_masks_not_cleaned)

# Directory to on of the images in 'directory_images' to get the image's height and width
directory_image0 = directory_images + '/' + images[0]
image0 = Image.open(directory_image0)
width, height = image0.size

# Directory to the pink and black image
directory_pink = 'background.png'
directory_black = 'black.png'

label = 250

# Looping through the images
for i in range(len(images)):
    pink = Image.open(directory_pink)
    black = Image.open(directory_black)
    black = ImageOps.grayscale(black)
    pix_pink = pink.load()
    pix_black = black.load()
    image_name = images[i]
    mask_name = masks[i]
    image_directory = directory_images + '/' + image_name
    mask_directory = directory_masks + '/' + mask_name
    image = Image.open(image_directory)
    mask = Image.open(mask_directory)
    mask = mask.resize((width, height))
    mask = ImageOps.grayscale(mask)

    if double_augmenter:
        pink_nc = pink.copy()
        black_nc = black.copy()
        black_nc = ImageOps.grayscale(black_nc)
        pix_pink_nc = pink_nc.load()
        pix_black_nc = black_nc.load()
        image_not_cleaned_name = images_not_cleaned[i]
        mask_not_cleaned_name = masks_not_cleaned[i]
        image_nc_dir = directory_images_not_cleaned + '/' + image_not_cleaned_name
        mask_nc_dir = directory_masks_not_cleaned + '/' + mask_not_cleaned_name
        img_nc = Image.open(image_nc_dir)
        mask_nc = Image.open(mask_nc_dir)
        mask_nc = mask_nc.resize((width, height))
        mask_nc = ImageOps.grayscale(mask_nc)





    # Calling the method augmentation to start augmenting the images and masks
    if double_augmenter:
        augmentation(double_augmenter, image_name, image, pink, pix_pink, mask, black, pix_black, width, height, label,
                     img_nc, pink_nc, pix_pink_nc, mask_nc, black_nc, pix_black_nc)
    else:
        augmentation(double_augmenter, image_name, image, pink, pix_pink, mask, black, pix_black, width, height, label)
