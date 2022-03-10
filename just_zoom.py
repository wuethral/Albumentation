from PIL import Image, ImageOps
import random
import os

def zoom_in(img,mask, screw_name):

    pink = Image.open('background.png')
    black = Image.open('black.png')
    width, height = black.size
    random_nr = random.random()
    # print('zoom_out:', random_nr)
    new_width = int((1 + random_nr) * width)
    new_height = int((1 + random_nr) * height)
    zoom_out_size = (new_width, new_height)
    pink = pink.resize(zoom_out_size)
    black = black.resize(zoom_out_size)
    black = ImageOps.grayscale(black)
    pink_pix = pink.load()
    img_pix = img.load()
    black_pix = black.load()
    mask_pix = mask.load()
    difference_in_width_div_by_two = int((new_width - width) / 2)
    difference_in_height_div_by_two = int((new_height - height) / 2)
    for x in range(difference_in_width_div_by_two, new_width - difference_in_width_div_by_two - 2):
        for y in range(difference_in_height_div_by_two, new_height - difference_in_height_div_by_two - 2):
            pink_pix[x, y] = img_pix[x - difference_in_width_div_by_two, y - difference_in_height_div_by_two]
            black_pix[x, y] = mask_pix[x - difference_in_width_div_by_two, y - difference_in_height_div_by_two]

    pink.resize((width, height))
    black.resize((width, height))
    bl_pix = black.load()
    for x in range(width):
        for y in range(height):
            if bl_pix[x,y] != 0:
                bl_pix[x,y] = 250
    save_name_image = 'D:/Project_Eye_Tracking/DataSetAugmentation/screw/zoom_in/images/' + screw_name
    save_name_mask = 'D:/Project_Eye_Tracking/DataSetAugmentation/screw/zoom_in/masks/' + screw_name
    pink.save(save_name_image)
    black.save(save_name_mask)

screw_folder_path = 'D:/Project_Eye_Tracking/DataSetAugmentation/screw/images'
mask_folder_path = 'D:/Project_Eye_Tracking/DataSetAugmentation/screw/masks'
screw_names = os.listdir(screw_folder_path)
for screw_name in screw_names:
    print(screw_name)
    screw_path = screw_folder_path + '/' + screw_name
    image = Image.open(screw_path)
    mask_path = mask_folder_path + '/' + screw_name
    mask = Image.open(mask_path)
    mask = ImageOps.grayscale(mask)
    zoom_in(image,mask,screw_name)
