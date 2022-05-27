from doctest import testmod
from tkinter import Label, font
import fontTools

from numpy import testing
import pygame, sys
from pygame.locals import *
import numpy as np
from keras.models import load_model
import cv2



#initializing pygame

WINDOWSIZEX = 640
WINDOWSIZEY = 480


BOUNDRYINC = 5
WHITE =(255,255,255)
BLACK =(0,0,0)
RED = (255,0,0)

IMAGESAVE = False

MODEL = load_model("himanshu.h5")

LABELS ={ 0 : "Zero",1 : "one",2 : "Two",3 : "Three",4 : "Four",5 : "Five",6 : "Six",7 : "Seven",8 : "Eight",9: "Nine"} 

pygame.init()

global display_s

font = pygame.font.Font('freesansbold.ttf', 32)

display_s = pygame.display.set_mode((WINDOWSIZEX,WINDOWSIZEY))
pygame.display.set_caption("Digit Board")

iswriting =False
image_cnt =1
PREDICT=True 
number_xcord=[]
number_ycord=[]
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

        if event.type == MOUSEMOTION and iswriting :
            xcord , ycord = pygame.mouse.get_pos()
            pygame.draw.circle(display_s,WHITE,(xcord,ycord),4,0)

            number_xcord.append(xcord)
            number_ycord.append(ycord)

        if event.type == MOUSEBUTTONDOWN:
            iswriting = True

        if event.type == MOUSEBUTTONUP:
            iswriting = False
            
            number_xcord = sorted(number_xcord)
            number_ycord = sorted(number_ycord)

            rect_min_x , rect_max_x =  max(number_xcord[0]-BOUNDRYINC,0) , min(WINDOWSIZEX,number_xcord[-1]+BOUNDRYINC)
            rect_min_y , rect_max_y =  max(number_ycord[0]-BOUNDRYINC,0) , min(number_ycord[-1]+BOUNDRYINC,WINDOWSIZEX)

            number_xcord=[]
            number_ycord=[]
            img_arr = np.array(pygame.PixelArray(display_s))[rect_min_x : rect_max_x , rect_min_y : rect_max_y].T.astype(np.float32)

            if IMAGESAVE:
                cv2.imwrite("image.png")
                image_cnt +=1


            if PREDICT:
                image =cv2.resize(img_arr,(28,28))
                image =np.pad(image,(10,10),'constant',constant_values=0)
                image=cv2.resize(image,(28,28))/255

                label =str(LABELS[np.argmax(MODEL.predict(image.reshape(1,28,28,1)))])

                textsurface = font.render(label,True,RED,WHITE)
                textRecObj = textsurface.get_rect()
                
                textRecObj.left = rect_min_x
                textRecObj.bottom = rect_max_y
                
                display_s.blit(textsurface,textRecObj)


            if event.type == KEYDOWN:
                if event.unicode == "n":
                 display_s.fill(BLACK)
    pygame.display.update()
