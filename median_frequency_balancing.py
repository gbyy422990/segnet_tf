#coding:utf-8
#GAO Bin

from __future__ import print_function
import os,sys
import numpy as np
import cv2

images_path = './output/label'
image_name = os.listdir(images_path)
print(image_name)

#n_background = 0
n_building = 0
n_river = 0
n_plants = 0
n_roadline = 0
n_roadaera = 0

#pixel_background = 0
pixel_building = 0
pixel_river = 0
pixel_plants = 0
pixel_roadline = 0
pixel_roadaera = 0

def get_median(data):
    data = sorted(data)
    size = len(data)
    if size % 2 == 0:
        median = (data[size//2] + data[size//2-1])/2
        data[0] = median
    if size % 2 == 1:
        median = data[(size - 1) // 2]
        data[0] = median
    return data[0]


def count(img):
    global pixel_background,pixel_roadline,pixel_roadaera,pixel_plants,pixel_building,pixel_river
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 255:
                pixel_background += 1
            #n_background += 1

            if img[i][j][0] == 255 and img[i][j][1] == 0 and img[i][j][2] == 0:
                pixel_building += 1
            #n_building += 1

            if img[i][j][0] == 0 and img[i][j][1] == 255 and img[i][j][2] == 255:
                pixel_river += 1
            #n_river += 1

            if img[i][j][0] == 255 and img[i][j][1] == 255 and img[i][j][2] == 0:
                pixel_plants += 1
            #n_plants += 1

            if img[i][j][0] == 0 and img[i][j][1] == 0 and img[i][j][2] == 255:
                pixel_roadaera += 1
            #n_roadaera += 1
            if img[i][j][0] == 0 and img[i][j][1] == 255 and img[i][j][2] == 0:
                pixel_roadline += 1
            #n_roadline += 1
            else:
                pass
    return pixel_building,pixel_river,pixel_plants,pixel_roadaera,pixel_roadline

for im in image_name:
    print(im)
    #print('before:',pixel_background)
    print('before:',pixel_building)
    print('before:',pixel_river)
    print('before:',pixel_plants)
    print('before:',pixel_roadaera)
    print('before:',pixel_roadline)

    #background_before = pixel_background
    building_before = pixel_building
    river_before = pixel_river
    plants_before = pixel_plants
    roadaera_before = pixel_roadaera
    roadline_before = pixel_roadline

    if im[-4:] == '.tif':

        im = cv2.imread('./output/label/' + im)
        print(im.shape)
        count(im)

        #if background_before - pixel_background != 0:
         #   n_background += 1
          #  print(n_background)
        if building_before - pixel_building != 0:
            n_building += 1
        if river_before - pixel_river != 0:
            n_river += 1
        if plants_before - pixel_plants != 0:
            n_plants += 1
        if roadaera_before - pixel_roadaera != 0:
            n_roadaera += 1
        if roadline_before - pixel_roadline != 0:
            n_roadline += 1
    else:
        pass


w, h, c = im.shape
#f(class) = frequency(class) / (image_count(class) * 480*360)

#f_background = pixel_background/(n_background * w * h)
f_building = pixel_building/(n_building * w * h)
f_river = pixel_river/(n_river * w * h)
f_plants = pixel_plants/(n_plants * w * h)
f_roadaera = pixel_roadaera/(n_roadaera * w * h)
f_roadline = pixel_roadline/(n_roadline * w * h)

median_f = [f_building,f_river,f_plants,f_roadaera,f_roadline]

#weight(class) = median of f(class)) / f(class)
median = get_median(median_f)
#weight_background = median/f_background
weight_building = median/f_building
weight_river = median/f_river
weight_plants = median/f_river
weight_roadaera = median/f_roadaera
weight_roadline = median/f_roadline

#print('weight_background:',weight_background)
print('weight_building:',weight_building)
print('weight_river:',weight_river)
print('weight_plants:',weight_plants)
print('weight_roadaera:',weight_roadaera)
print('weight_roadline:',weight_roadline)
