from PIL import Image, ImageOps

from custom_translation import making_pixels_pink, making_pixels_pink_2, translate, check_all_edge_pixel_black_y_axis, \
    check_all_edge_pixel_black_x_axis
from custom_rotate import rotation_making_black_pixels_pink, turn_pink_2, turn_black
from custom_zoom_2 import zoom_in, zoom_out
from random import random

''' 
directory_image = 'backgrounded/anglepink4.png'
directory_pink = 'background.png'
imageimage = Image.open(directory_image)
pink = Image.open(directory_pink)
pix_original = imageimage.load()
pix_pink = pink.load()
width, height = imageimage.size
print(type(imageimage))
'''


def augmentation(*args):
    '''In this method, all the augmentation methods for zoom, rotation and translation are called'''
    double_augmenter = args[0]
    image_name = args[1]
    image = args[2]
    pink = args[3]
    pix_pink = args[4]
    mask = args[5]
    black = args[6]
    pix_black = args[7]
    width = args[8]
    height = args[9]
    label = args[10]
    if double_augmenter:
        img_nc = args[11]
        pink_nc = args[12]
        pix_pink_nc = args[13]
        mask_nc = args[14]
        black_nc = args[15]
        pix_black_nc = args[16]

     # This number decides, how many augmentations images should be generated for the current image
    number_of_augmentations = 2

    # Creating an augmented image with every loop
    for i in range(number_of_augmentations):
        # Description of first image should be 1 and not 0
        i = i + 1

        # random() creates number between 0 and 1. zoom_random_nr is for deciding if it should be zoomed in or out
        zoom_random_nr = random()
        # if zoom_random_nr is smaller than 0.5, we zoom in
        if zoom_random_nr < 0.5:
            if double_augmenter:
                zoom_in(double_augmenter, image_name, image, mask, width, height, i, label, img_nc, mask_nc)
            else:
                zoom_in(double_augmenter, image_name, image, mask, width, height, i, label)


        # else zoom out
        else:
            if double_augmenter:
                zoom_out(double_augmenter, image_name, image, mask, black, width, height, pink, i, label, img_nc, mask_nc,
                         black_nc, pink_nc)
            else:
                zoom_out(double_augmenter, image_name, image, mask, black, width, height, pink, i, label)


        directory_zoom_img = 'zoom_folder/images/' + image_name[:-4] + '_' + str(i) + '.png'
        directory_zoom_mask = 'zoom_folder/masks/' + image_name[:-4] + '_' + str(i) + '.png'
        if double_augmenter:
            directory_zoom_img_not_cleaned = 'zoom_folder/no_cleaned_images/' + image_name[:-4] + '_' + str(i) + '.png'
            directory_zoom_mask_not_cleaned = 'zoom_folder/no_cleaned_masks/' + image_name[:-4] + '_' + str(i) + '.png'

        img_zoom = Image.open(directory_zoom_img)
        mask_zoom = Image.open(directory_zoom_mask)
        mask_zoom = ImageOps.grayscale(mask_zoom)
        pix_zoom = mask_zoom.load()
        pixel = pix_zoom

        if double_augmenter:
            img_zoom_nc = Image.open(directory_zoom_img_not_cleaned)
            mask_zoom_nc = Image.open(directory_zoom_mask_not_cleaned)
            mask_zoom_nc = ImageOps.grayscale(mask_zoom_nc)
            pix_zoom_nc = mask_zoom_nc.load()
            pixel = pix_zoom_nc

        random_rotate_nr = int(random() * 365)
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            random_rotate_nr = 0

        check_all_black_y_axis = check_all_edge_pixel_black_y_axis(pixel, width, height)
        if check_all_black_y_axis == False:
            random_rotate_nr = 0
        check_all_black_x_axis = check_all_edge_pixel_black_x_axis(pixel, width, height)
        if check_all_black_x_axis == False:
            random_rotate_nr = 0
        print('rotation_nr:', random_rotate_nr)

        rotated_img = img_zoom.rotate(random_rotate_nr)
        rotated_mask = mask_zoom.rotate(random_rotate_nr)
        pix_image = rotated_img.load()
        pix_mask = rotated_mask.load()

        if double_augmenter:
            rotated_img_nc = img_zoom_nc.rotate(random_rotate_nr)
            rotated_mask_nc = mask_zoom_nc.rotate(random_rotate_nr)
            pix_image_nc = rotated_img_nc.load()
            pix_mask_nc = rotated_mask_nc.load()


        for y in range(height):
            rotation_making_black_pixels_pink(y, width, pix_image, pix_mask)
            if double_augmenter:
                rotation_making_black_pixels_pink(y, width, pix_image_nc, pix_mask_nc)


        
        #save_name_img = 'D:/trained_models/Testing_Data_With_Augmentation/images/zoom_trans_rot_' + str(i) + '_' + image_name
        #pink.save(save_name_img)
        #save_name_mask = 'D:/trained_models/Testing_Data_With_Augmentation/masks/zoom_trans_rot_mask_' + str(i) + '_' + image_name
        #black.save(save_name_mask)
        
        x_trans = int(width / 3 * random())
        y_trans = int(height / 3 * random())
        if image_name.startswith('hand'):
            y_trans = int(y_trans / 6)
        # check_all_black_y_axis = check_all_edge_pixel_black_y_axis(pix_zoom, width, height)
        if check_all_black_y_axis == False:
            x_trans = 0
        # check_all_black_x_axis = check_all_edge_pixel_black_x_axis(pix_zoom, width, height)
        if check_all_black_x_axis == False:
            y_trans = 0
        x_trans_positiv = False
        y_trans_positiv = False
        random_number_for_x_dir = random()
        random_number_for_y_dir = random()
        print('x_number:', random_number_for_x_dir)
        print('y_number:', random_number_for_y_dir)
        if image_name.startswith('hand'):
            random_number_for_y_dir = 0.1

        if random_number_for_x_dir < 0.5:
            x_trans_positiv = True
        else:
            x_trans_positiv = False

        if random_number_for_y_dir < 0.5:
            y_trans_positiv = True
        else:
            y_trans_positiv = False

        if x_trans_positiv:
            print('x_trans_positiv')
            for x_coord in range(x_trans):
                making_pixels_pink(x_coord, height, pix_pink, pix_black)
                if double_augmenter:
                    making_pixels_pink(x_coord, height, pix_pink_nc, pix_black_nc)

        else:
            print('x_trans_negativ')
            for x_coord in range(width - x_trans, width):
                making_pixels_pink(x_coord, height, pix_pink, pix_black)
                if double_augmenter:
                    making_pixels_pink(x_coord, height, pix_pink_nc, pix_black_nc)
        if y_trans_positiv:
            print('y_trans_positiv')
            for y_coord in range(y_trans):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)
                if double_augmenter:
                    making_pixels_pink_2(y_coord, width, pix_pink_nc, pix_black_nc)
        else:
            print('y_trans_negativ')
            for y_coord in range(height - y_trans, height):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)
                if double_augmenter:
                    making_pixels_pink_2(y_coord, width, pix_pink_nc, pix_black_nc)

        if x_trans_positiv:
            for x_coord in range(x_trans, width):
                if y_trans_positiv:
                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        if double_augmenter:
                            translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc, pix_black_nc,
                                      x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0, height - y_trans):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        if double_augmenter:
                            translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                      pix_black_nc, x_trans_positiv, y_trans_positiv)
        else:
            for x_coord in range(0, width - x_trans):
                if y_trans_positiv:

                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        if double_augmenter:
                            translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                      pix_black_nc, x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0, height - y_trans):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        if double_augmenter:
                            translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                      pix_black_nc, x_trans_positiv, y_trans_positiv)

        save_name_img = 'augmented_images/' + image_name[:-4] + '_' +  str(i) + '.png'
        pink.save(save_name_img)
        save_name_mask = 'augmented_masks/' + image_name[:-4] + '_' +  str(i) + '.png'
        black.save(save_name_mask)

        if double_augmenter:
            save_name_img_nc = 'augmented_images_no_clean/' + image_name[:-4] + '_' +  str(i) + '.png'
            pink_nc.save(save_name_img_nc)
            save_name_mask_nc = 'augmented_masks_no_clean/' + image_name[:-4] + '_' +  str(i) + '.png'
            black_nc.save(save_name_mask_nc)


        for x in range(0,width):
            for y in range(0,height):
                turn_pink_2(x,y, pix_pink)
                turn_black(x, y, pix_black)
                if double_augmenter:
                    turn_pink_2(x,y, pix_pink_nc)
                    turn_black(x,y, pix_black_nc)


        warning_pixels_masks = False
        for x in range(width):
            for y in range(height):
                if black.load()[x, y] != 0 and black.load()[x, y] != label:
                    warning_pixels_masks = True
                if double_augmenter:
                    if black_nc.load()[x, y] != 0 and black_nc.load()[x, y] != label:
                        warning_pixels_masks = True

        if warning_pixels_masks:
            print('WARNING, Masks have wrong pixels!')
            print(' ')





