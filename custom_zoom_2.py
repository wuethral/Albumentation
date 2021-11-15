from PIL import Image, ImageOps
import random
from custom_rotate import check_pixel_pink, turn_pink_2, turn_black



def zoom_in(image_name, img, img_nc, mask, mask_nc, width, height, counter):
    print(image_name)


    initial_mask_pixel = mask.load()

    for x in range(width):
        for y in range(height):
            if initial_mask_pixel[x,y] != 0:
                label = initial_mask_pixel[x,y]
                break

    random_nr = 1 - 0.5 * random.random()
    print('zoom_in:', random_nr)
    # Setting the points for cropped image
    left = int(width/2 - ((random_nr * width)) / 2)
    top = int(height/2 - ((random_nr * height)) / 2)
    right = int(width/2 + ((random_nr * width)) / 2)
    bottom = int(height/2 + ((random_nr * height)) / 2)

    # Cropped image of above dimension
    # (It will not change original image)
    img = img.crop((left, top, right, bottom))
    img_nc = img_nc.crop((left, top, right, bottom))
    mask = mask.crop((left, top, right, bottom))
    mask_nc = mask_nc.crop((left, top, right, bottom))


    cropped_width = mask.size[0]
    cropped_height = mask.size[1]
    newsize = (width, height)

    #print(mask.size)

    img = img.resize(newsize)
    img_nc = img_nc.resize(newsize)
    #print(img.size)
    mask = mask.resize(newsize)
    mask_nc = mask_nc.resize(newsize)

    img_pixel = img.load()
    img_nc_pixel = img_nc.load()
    mask_pixel = mask.load()
    mask_nc_pixel = mask_nc.load()

    for x in range(width):
        for y in range(height):
            if check_pixel_pink(img_pixel, x, y):
                mask_pixel[x,y] = 0
            else:
                mask_pixel[x,y] = label

    for x in range(width):
        for y in range(height):
            if check_pixel_pink(img_nc_pixel, x, y):
                mask_nc_pixel[x,y] = 0
            else:
                mask_nc_pixel[x,y] = label




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
    save_name_image_nc = 'zoom_folder/no_cleaned_images/' + image_name[:-4] +'_' + str(counter) + '.png'
    save_name_mask_nc = 'zoom_folder/no_cleaned_masks/' + image_name[:-4] + '_mask_' +  str(counter) + '.png'
    img.save(save_name_image)
    mask.save(save_name_mask)
    img_nc.save(save_name_image_nc)
    mask_nc.save(save_name_mask_nc)
    return counter




def zoom_out(image_name, img, img_nc, mask, mask_nc, black, black_nc, width, height, pink, pink_nc, counter):

    print(image_name)
    '''
    directory_black = 'black.png'
    directory_pink = 'pink.pnk'
    black = Image.open(directory_black)
    black_nc = black.copy()
    black = ImageOps.grayscale(black)
    black_nc = ImageOps.grayscale(black_nc)
    pink = Image.open(directory_pink)
    pink_nc= pink.copy()
    '''

    initial_mask_pixel = mask.load()
    for x in range(width):
        for y in range(height):
            if initial_mask_pixel[x,y] != 0:
                label = initial_mask_pixel[x,y]
                break

    random_nr = random.random() * 0.5
    print('zoom_out:',random_nr)
    #print('zoom_out:', random_nr)
    new_width = int((1 + random_nr) * width)
    new_height = int((1 + random_nr) * height)
    zoom_out_size = (new_width, new_height)
    pink = pink.resize(zoom_out_size)
    pink_nc = pink_nc.resize(zoom_out_size)
    black = black.resize(zoom_out_size)
    black_nc = black_nc.resize(zoom_out_size)
    pink_pix = pink.load()
    pink_for_clean_pix = pink_nc.load()
    img_pix = img.load()
    img_nc_pix = img_nc.load()
    black_pix = black.load()
    black_for_clean_pix = black_nc.load()
    mask_pix = mask.load()
    mask_nc_pix = mask_nc.load()
    difference_in_width_div_by_two = int((new_width - width) /2)
    difference_in_height_div_by_two = int((new_height - height) / 2)
    for x in range(difference_in_width_div_by_two, new_width - difference_in_width_div_by_two-2):
        for y in range(difference_in_height_div_by_two, new_height - difference_in_height_div_by_two-2):
            pink_pix[x, y] = img_pix[x-difference_in_width_div_by_two, y-difference_in_height_div_by_two]
            black_pix[x, y] = mask_pix[x-difference_in_width_div_by_two, y-difference_in_height_div_by_two]
            pink_for_clean_pix[x, y] = img_nc_pix[x - difference_in_width_div_by_two, y - difference_in_height_div_by_two]
            black_for_clean_pix[x, y] = mask_nc_pix[x - difference_in_width_div_by_two, y - difference_in_height_div_by_two]


    ''' 
    for x in range(0, difference_in_width_div_by_two):
        for y in range(0, difference_in_height_div_by_two):
            turn_pink_2(x, y, pink_pix)
            turn_pink_2(x, y, pink_for_clean_pix)
            turn_black(x, y, black_pix)
            turn_black(x, y, black_for_clean_pix)

        for y in range(new_height - difference_in_height_div_by_two, new_height):
            turn_pink_2(x, y, pink_pix)
            turn_pink_2(x, y, pink_for_clean_pix)
            turn_black(x, y, black_pix)
            turn_black(x, y, black_for_clean_pix)
    for x in range(new_width-difference_in_width_div_by_two,new_width):
        for y in range(0, difference_in_height_div_by_two):
            turn_pink_2(x, y, pink_pix)
            turn_pink_2(x, y, pink_for_clean_pix)
            turn_black(x, y, black_pix)
            turn_black(x, y, black_for_clean_pix)
        for y in range(new_height - difference_in_height_div_by_two, new_height):
            turn_pink_2(x, y, pink_pix)
            turn_pink_2(x, y, pink_for_clean_pix)
            turn_black(x, y, black_pix)
            turn_black(x, y, black_for_clean_pix)
    '''





    for x in range(width):
        for y in range(height):
            if check_pixel_pink(pink_pix, x, y):
                black_pix[x,y] = 0
            else:
                black_pix[x,y] = label

    for x in range(width):
        for y in range(height):
            if check_pixel_pink(pink_for_clean_pix, x, y):
                black_for_clean_pix[x,y] = 0
            else:
                black_for_clean_pix[x,y] = label


    pink.resize((width,height))
    black.resize((width,height))
    pink_nc.resize((width,height))
    black_nc.resize((width,height))
    save_name_image = 'zoom_folder/images/' + image_name[:-4] +'_' + str(counter) + '.png'
    save_name_mask = 'zoom_folder/masks/' + image_name[:-4] + '_mask_' +  str(counter) + '.png'
    save_name_image_nc = 'zoom_folder/no_cleaned_images/' + image_name[:-4] +'_' + str(counter) + '.png'
    save_name_mask_nc = 'zoom_folder/no_cleaned_masks/' + image_name[:-4] + '_mask_' +  str(counter) + '.png'


    pink.save(save_name_image)
    black.save(save_name_mask)
    pink_nc.save(save_name_image_nc)
    black_nc.save(save_name_mask_nc)
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