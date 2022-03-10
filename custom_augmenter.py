from PIL import Image, ImageOps
import cv2 as cv
from random import random
from custom_translation import making_pixels_pink, making_pixels_pink_2, translate, check_all_edge_pixel_black_y_axis, check_all_edge_pixel_black_x_axis
from custom_rotate import rotation_making_black_pixels_pink
from custom_zoom import zoom_in, zoom_out
from random import random



def augmentation(image_name, image, pink, pix_pink, mask, black, pix_black, width, height):

    for i in range(2):
        print(image_name)
        i = i+1
        #(i)
         #random()
        '''
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            zoom_random_nr = 0.1
        '''
        zoom_random_nr = random()
        #print(zoom_random_nr)
        if zoom_random_nr < 0.5:
            zoom_in(image_name, image, mask, width, height, i)
        #else:
        #    save_name_image = 'zoom_folder/images/' + image_name[:-4] + '_' + str(i) + '.png'
        #    save_name_mask = 'zoom_folder/masks/' + image_name[:-4] + '_mask_' + str(i) + '.png'
        #    image.save(save_name_image)
        #    mask.save(save_name_mask)

        else:
            zoom_out(image_name, image, mask, black, width, height, pink, i)
        directory_zoom_img = 'zoom_folder/images/' + image_name[:-4] + '_' + str(i) +'.png'
        directory_zoom_mask = 'zoom_folder/masks/'  + image_name[:-4] + '_' + str(i) + '.png'

        img_zoom = Image.open(directory_zoom_img)
        mask_zoom = Image.open(directory_zoom_mask)
        pix_zoom = mask_zoom.load()
        ''' 
        for x in range(width):
            for y in range(height):
                if pix_zoom[x,y] != 0 and pix_zoom[x,y] != 253:
                    print(pix_zoom[x, y])
        
        '''

        random_rotate_nr = int(random() * 365)
        check_all_black_x_axis = True
        check_all_black_y_axis = True
        '''
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            random_rotate_nr = 0

        check_all_black_y_axis = check_all_edge_pixel_black_y_axis(pix_zoom, width, height)
        if check_all_black_y_axis == False:
            #random_rotate_nr = 0
        check_all_black_x_axis = check_all_edge_pixel_black_x_axis(pix_zoom, width, height)
        if check_all_black_x_axis == False:
        '''




        rotated_img = img_zoom.rotate(random_rotate_nr)
        rotated_mask = mask_zoom.rotate(random_rotate_nr)
        pix_image = rotated_img.load()
        #rotated_mask = ImageOps.grayscale(rotated_mask)
        pix_mask = rotated_mask.load()

        for y in range(height):
            rotation_making_black_pixels_pink(y, width, pix_image, pix_mask)
        ''' 
        save_name_img = 'D:/trained_models/Testing_Data_With_Augmentation/images/zoom_trans_rot_' + str(i) + '_' + image_name
        pink.save(save_name_img)
        save_name_mask = 'D:/trained_models/Testing_Data_With_Augmentation/masks/zoom_trans_rot_mask_' + str(i) + '_' + image_name
        black.save(save_name_mask)
        '''
        x_trans = int(width/3 * random())
        y_trans = int(height/3 * random())
        if image_name.startswith('hand') or image_name.startswith('zz_test_hand'):
            y_trans = int(y_trans/6)
        #check_all_black_y_axis = check_all_edge_pixel_black_y_axis(pix_zoom, width, height)
        if check_all_black_y_axis == False:
            x_trans = 0
        #check_all_black_x_axis = check_all_edge_pixel_black_x_axis(pix_zoom, width, height)
        if check_all_black_x_axis == False:
            y_trans = 0
        x_trans_positiv = False
        y_trans_positiv = False
        random_number_for_x_dir = random()
        random_number_for_y_dir = random()
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
            for x_coord in range(x_trans):
                making_pixels_pink(x_coord, height, pix_pink, pix_black)
        else:
            for x_coord in range(width-x_trans, width):
                making_pixels_pink(x_coord, height, pix_pink, pix_black)
        if y_trans_positiv:
            for y_coord in range (y_trans):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)
        else:
            for y_coord in range (height-y_trans, height):
                making_pixels_pink_2(y_coord, width, pix_pink, pix_black)

        if x_trans_positiv:
            for x_coord in range(x_trans, width):
                if y_trans_positiv:
                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans,x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black, x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0 ,height-y_trans):
                        translate(x_trans, y_trans,x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black, x_trans_positiv, y_trans_positiv)
        else:
            for x_coord in range(0, width-x_trans):
                if y_trans_positiv:
                    for y_coord in range(y_trans, height):
                        translate(x_trans, y_trans,x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black, x_trans_positiv, y_trans_positiv)
                else:
                    for y_coord in range(0 ,height-y_trans):
                        translate(x_trans, y_trans,x_coord, y_coord, pix_image, pix_mask, pix_pink, pix_black, x_trans_positiv, y_trans_positiv)

        save_name_img = 'augmented_images/' + image_name[:-4] + '_' + str(i) + '.png'
        pink.save(save_name_img)
        save_name_mask = 'augmented_masks/' + image_name[:-4] + '_' + str(i) + '.png'
        black.save(save_name_mask)

        for x in range(width):
            for y in range(height):
                if black.load()[x,y] != 0  and black.load()[x,y] != 248 and black.load()[x,y] != 249 and black.load()[x,y] != 250 and black.load()[x,y] != 251 and black.load()[x,y] != 252 and black.load()[x,y] != 253 and black.load()[x,y] != 254 and black.load()[x,y] != 255:
                    print(black.load()[x,y])
                    print('WARNING!')





