"""
OPEN FILE "C:\\USERS\\ASHER\\ONEDRIVE\\PICTURES\\SAVED PICTURES\\WEIRD SQUARE (.PNG"
DEFINE A FUNCTION THAT TAKES AS INPUT: FILE, XS, YS AND COLOR
THIS FUNCTION WILL TRY TO FILL THE INPUT FILE STARTING AT LOCATION XS,YS WITH THE PROVIDED COLOR ARG.
"""
import random
from idlelib.squeezer import count_lines_with_wrapping

import cv2
import time
import numpy as np

cv2.namedWindow("The BOX")


def get_neighbors(x, y,img):
    shape=img.shape
    ns=[(x + xx, y + yy) for xx in (-1, 0, 1) for yy in (-1, 0, 1) if xx or yy]
    return [n for n in ns if 0<=n[0]<shape[0] and 0<=n[1]<shape[1]]

def filter_by_color(list_of_tuples, img,color):
    return    [x for x in list_of_tuples if (img[x[0]][x[1]] == color).all()]


def fill_at(img, start, fill_color = [255, 255, 255]):
    stack = [start]
    start_color = np.array(img[start[0], start[1]])

    while stack:
        color_pixel = stack[0]
        stack.remove(color_pixel)

        img[color_pixel[0], color_pixel[1]] = fill_color
        colors = get_neighbors(color_pixel[0], color_pixel[1],img)
        colors = filter_by_color(colors, img,start_color)
        stack.extend(colors)

        cv2.imshow('The BOX', img)
        cv2.waitKey(1)

mouseX,mouseY,clicked=-1,-1,False

def getMouseClick(event,x,y,flags,param):
    global mouseX,mouseY,clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        mouseX,mouseY = x,y
        print(x," ",y)
        clicked=True

img = cv2.imread("C:\\Users\\asher\\OneDrive\\Pictures\\Saved Pictures\\Weird Square.png")
img=cv2.resize(img,None,fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
print(img.shape)
cv2.imshow("The BOX",img)
cv2.setMouseCallback("The BOX",getMouseClick)
while not clicked:
    cv2.waitKey(1)
fill_at(img, [int(mouseY*0.5), int(mouseX*0.5)], [0, 0, 0])
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
