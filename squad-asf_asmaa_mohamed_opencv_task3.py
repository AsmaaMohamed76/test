import cv2
import numpy as np
from matplotlib import pyplot as plt
import math as m
import math

# rows = 500
# cols = 500
# newMat_3ch = np.zeros((rows, cols, 3), dtype = "uint8") #3channel

# step = 20
# x = np.linspace(start=0, stop=rows, num=step)
# y = np.linspace(start=0, stop=cols, num=step)
# v_xy = []
# h_xy = []
# for i in range(step):
    
#     v_xy.append( [int(x[i]), 0, int(x[i]), rows-1] )
#     h_xy.append( [0, int(y[i]), cols-1, int(y[i])] )

# for i in range(step):
#     [x1, y1, x2, y2] = v_xy[i]
#     [x1_, y1_, x2_, y2_] = h_xy[i]


# cv2.line(newMat_3ch, (x1,y1), (x2, y2), (0,0,255),1 )
# cv2.line(newMat_3ch, (x1_,y1_), (x2_, y2_), (255,0,0),1 )
# cv2.namedWindow('newMat_3ch',0)
# cv2.imshow('newMat_3ch', newMat_3ch)
# cv2.waitKey(0)
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
