import os
from PIL import Image, ImageOps
from custom_augmenter_2 import augmentation


# Opening the images from folder images_pink_background and masks. These paths can of course be changed.
directory_images = 'images_pink_background'
directory_masks = 'masks'
directory_images_not_cleaned = 'images_pink_background'
directory_masks_not_cleaned = 'masks'
images = os.listdir(directory_images)
masks = os.listdir(directory_masks)
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
    # Opening the pink image and copying it
    pink = Image.open(directory_pink)
    pink_nc = pink.copy()
    # Opening the black image and copying it
    black = Image.open(directory_black)
    black_nc = black.copy()
    # Turning black and black_nc images into grayscale color mode
    black = ImageOps.grayscale(black)
    black_nc = ImageOps.grayscale(black_nc)
    # Loading the pixels of the black and pink images
    pix_pink = pink.load()
    pix_pink_nc = pink_nc.load()
    pix_black = black.load()
    pix_black_nc = black_nc.load()

    # Getting the image names of the images and masks at the position i in order to get their directions
    image_name = images[i]
    mask_name = masks[i]
    image_not_cleaned_name = images_not_cleaned[i]
    mask_not_cleaned_name = masks_not_cleaned[i]
    image_directory = directory_images + '/' + image_name
    mask_directory = directory_masks + '/' + mask_name
    image_nc_dir = directory_images_not_cleaned + '/' + image_not_cleaned_name
    mask_nc_dir = directory_masks_not_cleaned + '/' + mask_not_cleaned_name
    # Opening the images and masks, resizing the masks and turning the masks to grayscale
    image = Image.open(image_directory)
    img_nc = Image.open(image_nc_dir)
    mask = Image.open(mask_directory)
    mask = mask.resize((width,height))
    mask = ImageOps.grayscale(mask)
    mask_nc = Image.open(mask_nc_dir)
    mask_nc = mask_nc.resize((width,height))
    mask_nc = ImageOps.grayscale(mask_nc)

    # Calling the method augmentation to start augmenting the images and masks
    augmentation(image_name, image, img_nc, pink, pink_nc, pix_pink, pix_pink_nc, mask, mask_nc, black, black_nc,
                 pix_black, pix_black_nc, width, height, label)
