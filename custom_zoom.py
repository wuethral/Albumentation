from PIL import Image
import random
from custom_rotate import check_pixel_pink

def zoom_in(image_name, img, mask, width, height, counter):
    print('zoom_in')

    initial_mask_pixel = mask.load()
    for x in range(width):
        for y in range(height):
            if initial_mask_pixel[x,y] != 0:
                label = initial_mask_pixel[x,y]
                break

    random_nr = 1 - 0.5 * random.random()
    #print('zoom_in:', random_nr)
    # Setting the points for cropped image
    left = int(width/2 - ((random_nr * width)) / 2)
    top = int(height/2 - ((random_nr * height)) / 2)
    right = int(width/2 + ((random_nr * width)) / 2)
    bottom = int(height/2 + ((random_nr * height)) / 2)

    # Cropped image of above dimension
    # (It will not change original image)
    img = img.crop((left, top, right, bottom))
    mask = mask.crop((left, top, right, bottom))

    cropped_width = mask.size[0]
    cropped_height = mask.size[1]
    newsize = (width, height)

    #print(mask.size)

    img = img.resize(newsize)
    print(img.size)
    mask = mask.resize(newsize)

    img_pixel = img.load()
    mask_pixel = mask.load()

    for x in range(width):
        for y in range(height):
            if check_pixel_pink(img_pixel, x, y):
                mask_pixel[x,y] = 0
            else:
                mask_pixel[x,y] = label



    ''' 
    for x in range(0,int((width-cropped_width)/2)):
        for y in range(0, int((height-cropped_height)/2)):
            mask_pixel[x,y] = 0
        for y in range(cropped_height + int((width-cropped_height)/2),height):
            mask_pixel[x,y] = 0
    for x in range(cropped_width + int((width-cropped_width)/2), width):
        for y in range(0, int((height-cropped_height)/2)):
            mask_pixel[x,y] = 0
        for y in range(cropped_height + int((width-cropped_height)/2),height):
            mask_pixel[x,y] = 0
    '''
    ''' 
    print('asdfasdf')
    for x in range(mask.size[0]):
        for y in range(mask.size[1]):
            if mask_pixel[x, y] != 0 and mask_pixel[x, y] != 253:
                print(mask_pixel[x, y])
    print('asdfasdf')
    '''


    # Shows the image in image viewer
    save_name_image = 'zoom_folder/images/' + image_name[:-4] +'_' + str(counter) + '.png'
    save_name_mask = 'zoom_folder/masks/' + image_name[:-4] + '_mask_' +  str(counter) + '.png'
    img.save(save_name_image)
    mask.save(save_name_mask)
    return counter


def zoom_out(image_name, img, mask, black, width, height, pink, counter):
    print('zoom_out')

    random_nr = random.random() * 0.5
    #print('zoom_out:', random_nr)
    new_width = int((1 + random_nr) * width)
    new_height = int((1 + random_nr) * height)
    zoom_out_size = (new_width, new_height)
    pink = pink.resize(zoom_out_size)
    black = black.resize(zoom_out_size)
    pink_pix = pink.load()
    img_pix = img.load()
    black_pix = black.load()
    mask_pix = mask.load()
    difference_in_width_div_by_two = int((new_width - width) /2)
    difference_in_height_div_by_two = int((new_height - height) / 2)
    for x in range(difference_in_width_div_by_two, new_width - difference_in_width_div_by_two-2):
        for y in range(difference_in_height_div_by_two, new_height - difference_in_height_div_by_two-2):
            pink_pix[x, y] = img_pix[x-difference_in_width_div_by_two, y-difference_in_height_div_by_two]
            black_pix[x, y] = mask_pix[x-difference_in_width_div_by_two, y-difference_in_height_div_by_two]

    pink.resize((width,height))
    black.resize((width,height))
    save_name_image = 'zoom_folder/images/' + image_name[:-4] +'_' + str(counter) + '.png'
    save_name_mask = 'zoom_folder/masks/' + image_name[:-4] + '_mask_' +  str(counter) + '.png'
    img.save(save_name_image)
    mask.save(save_name_mask)
    return counter



''' 
directory = 'backgrounded/anglepink1.png'
img = Image.open(directory)
width,height = img.size
random_nr = random.random()
directory_pink = 'background.png'
pink = Image.open(directory_pink)
'''
''' 
random_nr = random.random()
if random_nr < 0.5:
    zoom_in(img, width, height)
else:
    zoom_out(img, width, height, pink)
'''