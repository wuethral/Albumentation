from PIL import Image
import cv2 as cv
from random import random



def check_pixel_pink(pix, x, y):
    #flag_pink = False
    #while flag_pink == False:
    if pix[x,y][0] == 250 and pix[x,y][1] == 14 and pix[x,y][2] == 191:
        return True
    else:
        return False

def turn_pink(x_2, y, pix, width):
    for x in range(x_2, width):
        pix[x, y] = (250,14,191)
        #pix_mask[x, y] = 0
def turn_pink_2(x,y,pix):
    pix[x, y] = (250, 14, 191)

def turn_black(x,y,pix):
    pix[x, y] = 0




def rotation_making_black_pixels_pink(y, width, pix_image, pix_mask):
    #for x in range(width):
    #        if pix_mask[x,y] != 0: #and pix_mask[x,y] != 253:
    #            print(pix_mask[x, y])

    if pix_image[0, y][0] == 0 and pix_image[0, y][1] == 0 and pix_image[0, y][2] == 0:
        flag_pink = False
        x = 0
        while flag_pink == False:
            #if check_pixel_pink(pix_image, x, y):
            if pix_image[x, y][0] != 0 or pix_image[x, y][1] != 0 or pix_image[x, y][2] != 0:
                flag_pink = True

            else:
                pix_image[x, y] = (250, 14, 191)
                #pix_mask[x, y] = 0

                x += 1

    flag_pink_black = False
    while flag_pink_black == False:
        for x_2 in range(0, width-1):
            #if ((pix_image[x_2, y][0] == 250 and pix_image[x_2, y][1] == 14 and pix_image[x_2, y][2] == 191)) and ((pix_image[x_2 + 1, y][0] == 0 and pix_image[x_2 + 1, y][1] == 0 and pix_image[x_2 + 1, y][2] == 0)):
             #   turn_pink(x_2, y, pix_image, width)
            if ((pix_image[x_2, y][0] != 0 and pix_image[x_2, y][1] != 0 and pix_image[x_2, y][2] != 0)) and ((pix_image[x_2 + 1, y][0] == 0 and pix_image[x_2 + 1, y][1] == 0 and pix_image[x_2 + 1, y][2] == 0)) and pix_mask[x_2, y] == 0:

                turn_pink(x_2, y, pix_image, width)

                flag_pink_black = True
            #elif x_2 == width-2:
            #    print('end:',x_2)
            #    flag_pink_black = True
        flag_pink_black = True





    '''
    for x_2 in range(0, width - 1):
        if check_pixel_pink(pix_image, x_2, y) == False and pix_mask[x_2, y] == 0:
            turn_pink(x_2, y, pix_image, width)
    '''


''' 
directory_image = 'backgrounded/anglepink4.png'
directory_pink = 'background.png'
img = Image.open(directory_image)
pink = Image.open(directory_pink)
pix_original = img.load()
pix = pink.load()
width, height = img.size
rotated_img = img.rotate(235)
pix_rotated_img = rotated_img.load()
for y in range(height):
    rotation_making_black_pixels_pink(y, width, pix_rotated_img)
rotated_img.save('rotated.png')

'''
