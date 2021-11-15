from PIL import Image
import cv2 as cv
from random import random

def making_pixels_pink(x_coord, height, pix_pink, pix_black):


    for i in range(height):

        pix_pink[x_coord, i] = (250, 14, 191)
        pix_black[x_coord, i] = 0


def making_pixels_pink_2(y_coord, width, pix, pix_black):

    for i in range(width):
        pix[i, y_coord] = (250, 14, 191)
        pix_black[i, y_coord] = 0

def translate(x_trans, y_trans,x_coord, y_coord, pix_original, pix_mask, pix, pixel_black, x_trans_positiv, y_trans_positiv):

    if x_trans_positiv and y_trans_positiv:
        pix[x_coord, y_coord] = pix_original[x_coord-x_trans, y_coord-y_trans]
        pixel_black[x_coord, y_coord] = pix_mask[x_coord-x_trans, y_coord-y_trans]
        #if pix_mask[x_coord-x_trans, y_coord-y_trans] != 0:
        #    print(pix_mask[x_coord-x_trans, y_coord-y_trans])

    elif x_trans_positiv and not y_trans_positiv:
        pix[x_coord, y_coord] = pix_original[x_coord - x_trans, y_coord + y_trans]
        pixel_black[x_coord, y_coord] = pix_mask[x_coord - x_trans, y_coord + y_trans]
        #if pix_mask[x_coord - x_trans, y_coord - y_trans] != 0:
        #    print(pix_mask[x_coord-x_trans, y_coord-y_trans])
    elif not x_trans_positiv and y_trans_positiv:
        pix[x_coord, y_coord] = pix_original[x_coord + x_trans, y_coord - y_trans]
        pixel_black[x_coord, y_coord] = pix_mask[x_coord + x_trans, y_coord - y_trans]
        #if pix_mask[x_coord - x_trans, y_coord - y_trans] != 0:
        #    print(pix_mask[x_coord-x_trans, y_coord-y_trans])
    else:
        pix[x_coord, y_coord] = pix_original[x_coord + x_trans, y_coord + y_trans]
        pixel_black[x_coord, y_coord] = pix_mask[x_coord + x_trans, y_coord + y_trans]
        #if pix_mask[x_coord - x_trans, y_coord - y_trans] != 0:
        #    print(pix_mask[x_coord-x_trans, y_coord-y_trans])
    #if pix_mask[x_coord - x_trans, y_coord - y_trans] != 0:
        #print('pixel_mask: ', pix_mask[x_coord - x_trans, y_coord - y_trans])

def check_all_edge_pixel_black_y_axis(pix_zoom, width, height):
    check_pixel_black = True
    for y in range(height):
        if pix_zoom[0,y] != 0:
            check_pixel_black = False
            break
        elif pix_zoom[width-1, y] != 0:
            check_pixel_black = False
            break
    return check_pixel_black

def check_all_edge_pixel_black_x_axis(pix_zoom, width, height):
    check_pixel_black = True
    for x in range(width):
        if pix_zoom[x,0] != 0:
            check_pixel_black = False
            break
        elif pix_zoom[x, height-1] != 0:
            check_pixel_black = False
            break
    return check_pixel_black



''' 
directory_image = 'backgrounded/anglepink4.png'
directory_pink = 'background.png'
img = Image.open(directory_image)
pink = Image.open(directory_pink)
pix_original = img.load()
pix = pink.load()
width, height = img.size

for i in range(100):

    x_trans = int(width/2 * random())
    y_trans = int(height/2 * random())
    x_trans_positiv = False
    y_trans_positiv = False
    random_number_for_x_dir = random()
    random_number_for_y_dir = random()

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
            making_pixels_pink(x_coord, height, pix)
    else:
        for x_coord in range(width-x_trans, width):
            making_pixels_pink(x_coord, height, pix)
    if y_trans_positiv:
        for y_coord in range (y_trans):
            making_pixels_pink_2(y_coord, width, pix)
    else:
        for y_coord in range (height-y_trans, height):
            making_pixels_pink_2(y_coord, width, pix)

    if x_trans_positiv:
        for x_coord in range(x_trans, width):
            if y_trans_positiv:
                for y_coord in range(y_trans, height):
                    translate(x_trans, y_trans,x_coord, y_coord, pix_original, pix, x_trans_positiv, y_trans_positiv)
            else:
                for y_coord in range(0 ,height-y_trans):
                    translate(x_trans, y_trans,x_coord, y_coord, pix_original, pix, x_trans_positiv, y_trans_positiv)
    else:
        for x_coord in range(0, width-x_trans):
            if y_trans_positiv:
                for y_coord in range(y_trans, height):
                    translate(x_trans, y_trans,x_coord, y_coord, pix_original, pix, x_trans_positiv, y_trans_positiv)
            else:
                for y_coord in range(0 ,height-y_trans):
                    translate(x_trans, y_trans,x_coord, y_coord, pix_original, pix, x_trans_positiv, y_trans_positiv)
    save_name = 'translation/translated_' + str(i) + '.png'
    pink.save(save_name)
'''