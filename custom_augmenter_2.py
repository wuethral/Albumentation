from PIL import Image
import cv2 as cv
from random import random
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


def augmentation(image_name, image, img_nc, pink, pink_nc, pix_pink, pix_pink_nc, mask, mask_nc, black, black_nc, pix_black, pix_black_nc, width, height):
    for i in range(2):
        #print(image_name)
        i = i + 1

        # (i)
        zoom_random_nr = random()
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            zoom_random_nr = 0.1

        # print(zoom_random_nr)
        if zoom_random_nr < 0.5:
            zoom_in(image_name, image, img_nc, mask, mask_nc, width, height, i)

        else:
            zoom_out(image_name, image, img_nc, mask, mask_nc, black, black_nc, width, height, pink, pink_nc, i)
            #print('zoomout')

        directory_zoom_img = 'zoom_folder/images/' + image_name[:-4] + '_' + str(i) + '.png'
        directory_zoom_mask = 'zoom_folder/masks/' + image_name[:-4] + '_mask_' + str(i) + '.png'
        directory_zoom_img_not_cleaned = 'zoom_folder/no_cleaned_images/' + image_name[:-4] + '_' + str(i) + '.png'
        directory_zoom_mask_not_cleaned = 'zoom_folder/no_cleaned_masks/' + image_name[:-4] + '_mask_' + str(i) + '.png'
        img_zoom = Image.open(directory_zoom_img)
        img_zoom_nc = Image.open(directory_zoom_img_not_cleaned)
        mask_zoom = Image.open(directory_zoom_mask)
        mask_zoom_nc = Image.open(directory_zoom_mask_not_cleaned)
        pix_zoom_nc = mask_zoom_nc.load()


        #for x in range(width):
        #    for y in range(height):
        #        if pix_zoom[x,y] != 0 and pix_zoom[x,y] != 253:
        #            print(pix_zoom[x, y])

    

        random_rotate_nr = int(random() * 365)
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            random_rotate_nr = 0

        check_all_black_y_axis = check_all_edge_pixel_black_y_axis(pix_zoom_nc, width, height)
        if check_all_black_y_axis == False:
            random_rotate_nr = 0
        check_all_black_x_axis = check_all_edge_pixel_black_x_axis(pix_zoom_nc, width, height)
        if check_all_black_x_axis == False:
            random_rotate_nr = 0
        print('rotation_nr:', random_rotate_nr)

        rotated_img = img_zoom.rotate(random_rotate_nr)
        rotated_img_nc = img_zoom_nc.rotate(random_rotate_nr)
        rotated_mask = mask_zoom.rotate(random_rotate_nr)
        rotated_mask_nc = mask_zoom_nc.rotate(random_rotate_nr)
        pix_image = rotated_img.load()
        pix_image_nc = rotated_img_nc.load()
        pix_mask = rotated_mask.load()
        pix_mask_nc = rotated_mask_nc.load()


        for y in range(height):
            rotation_making_black_pixels_pink(y, width, pix_image, pix_mask)
            rotation_making_black_pixels_pink(y, width, pix_image_nc, pix_mask_nc)


        
        #save_name_img = 'D:/trained_models/Testing_Data_With_Augmentation/images/zoom_trans_rot_' + str(i) + '_' + image_name
        #pink.save(save_name_img)
        #save_name_mask = 'D:/trained_models/Testing_Data_With_Augmentation/masks/zoom_trans_rot_mask_' + str(i) + '_' + image_name
        #black.save(save_name_mask)
        
        x_trans = int(width / 3 * random())
        y_trans = int(height / 3 * random())
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
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
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
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
                making_pixels_pink(x_coord, height, pix_pink_nc, pix_black_nc)

        else:
            print('x_trans_negativ')
            for x_coord in range(width - x_trans, width):
                making_pixels_pink(x_coord, height, pix_pink, pix_black)
                making_pixels_pink(x_coord, height, pix_pink_nc, pix_black_nc)
        if y_trans_positiv:
            print('y_trans_positiv')
            for y_coord in range(y_trans):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)
                making_pixels_pink_2(y_coord, width, pix_pink_nc, pix_black_nc)
        else:
            print('y_trans_negativ')
            for y_coord in range(height - y_trans, height):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)
                making_pixels_pink_2(y_coord, width, pix_pink_nc, pix_black_nc)

        if x_trans_positiv:
            for x_coord in range(x_trans, width):
                if y_trans_positiv:
                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc, pix_black_nc,
                                  x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0, height - y_trans):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                  pix_black_nc,
                                  x_trans_positiv, y_trans_positiv)
        else:
            for x_coord in range(0, width - x_trans):
                if y_trans_positiv:

                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                  pix_black_nc,
                                  x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0, height - y_trans):
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black,
                                  x_trans_positiv, y_trans_positiv)
                        translate(x_trans, y_trans, x_coord, y_coord, pix_image_nc, pix_mask_nc, pix_pink_nc,
                                  pix_black_nc,
                                  x_trans_positiv, y_trans_positiv)

        save_name_img = 'D:/trained_models/Training_Data_With_Augmentation_3/images/' + 'zz_' +  image_name[:-4] + '_' +  str(i) + '.png'
        pink.save(save_name_img)
        save_name_mask = 'D:/trained_models/Training_Data_With_Augmentation_3/masks/' + 'zz_' + image_name[:-4] + '_mask_' +  str(i) + '.png'
        black.save(save_name_mask)

        save_name_img_nc = 'D:/trained_models/Training_Data_With_Augmentation_3/images_no_clean/' + 'zz_' + image_name[:-4] + '_' +  str(i) + '.png'
        pink_nc.save(save_name_img_nc)
        save_name_mask_nc = 'D:/trained_models/Training_Data_With_Augmentation_3/masks_no_clean/' + 'zz_' + image_name[:-4] + '_mask_' +  str(i) + '.png'
        black_nc.save(save_name_mask_nc)
        for x in range(0,width):
            for y in range(0,height):
                turn_pink_2(x,y, pix_pink)
                turn_pink_2(x,y, pix_pink_nc)
                turn_black(x,y,pix_black)
                turn_black(x,y, pix_black_nc)


        warning_4 = False
        for x in range(width):
            for y in range(height):
                if black.load()[x, y] != 0 and black.load()[x, y] != 249 and black.load()[x, y] != 250 and black.load()[
                    x, y] != 251 and black.load()[x, y] != 252 and black.load()[x, y] != 253 and black.load()[
                    x, y] != 254 and black.load()[x, y] != 255:
                    warning_4 = True
                if black_nc.load()[x, y] != 0 and black_nc.load()[x, y] != 249 and black_nc.load()[x, y] != 250 and black_nc.load()[
                    x, y] != 251 and black_nc.load()[x, y] != 252 and black_nc.load()[x, y] != 253 and black_nc.load()[
                    x, y] != 254 and black_nc.load()[x, y] != 255:
                    warning_4 = True


        if warning_4:
            print('WARNING_4!')
        print(' ')





