import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as m
import math

img = np.zeros([150,150,3],np.uint8)
img.fill(145)
for i in range(0, 150, 5):
    p1 =(i,0)
    p2 =(i,150)
    cv2.line(img,p1,p2,(0,0,0),1)
for i in range(0,150,5):
    p3 = (0,i)
    p4 = (150 ,i)
    cv2.line(img,p3,p4,(0,0,0),1)
initial = (0, 70)
speed = float(input("Enter your speed : "))
angle = int(input("Enter your angle : "))
time = int(input("Enter the time : "))
height = abs((speed*18/5)*(time*60*60)*m.sin(m.radians(angle)))
width = abs((speed*18/5)*(time*60*60)*m.cos(m.radians(angle)))
cord = (initial[0] + int(width), initial[1] + int(height))
imgLine = cv2.line(img,initial,cord,(255,0,0),1)
plt.imshow(imgLine)
plt.show() 
