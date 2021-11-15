import cv2 as cv
import numpy as np

def fill_hole(mask):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    len_contour = len(contours)
    contour_list = []
    for i in range(len_contour):
        drawing = np.zeros_like(mask, np.uint8)  # create a black image
        img_contour = cv.drawContours(drawing, contours, i, (249,249,249), -1)
        contour_list.append(img_contour)

    out = sum(contour_list)
    return out