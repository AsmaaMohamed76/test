#Ahmed Magdy & Ahmed Nabil & Asmaa Mohamed
import numpy as np
import cv2
import math
import copy

drawing = False # true if mouse is pressed
ix,iy = -1,-1

# Adding Function Attached To Mouse Callback
def draw_rect(event,x,y,flags,param):
    global ix,iy,drawing
    global img
    global cache
     # Add the rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        # store mouse location
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        drawing == True
    elif event == cv2.EVENT_LBUTTONUP:
        cache = copy.deepcopy(img)
        # For Drawing Rectangle
        cv2.rectangle(img,(ix,iy),(x,y),(100,120,45), thickness=4)
        drawing = False
        # Delete all
    elif event == cv2.EVENT_RBUTTONDOWN:
        img = copy.deepcopy(cache)
        cv2.imshow('image', img)
        
# add 4 images
img_1 = cv2.imread("/Users/heidikonswah/Desktop/Software/computer_vision/computer_vision_tasks/images/task_6/coral3.jpg")
img_2 = cv2.imread("/Users/heidikonswah/Desktop/Software/computer_vision/computer_vision_tasks/images/task_6/coral4.jpg")
img_3 = np.zeros([512,512,3],np.uint8)
img_4 = np.zeros([512,512,3],np.uint8)
#resize the two image
resized_img1 = cv2.resize(img_1,(512,512))
resized_img2 = cv2.resize(img_2,(512,512))
img_stack = np.hstack([resized_img2,resized_img1])
img_stack2 = np.hstack([img_3,img_4])
#the final image after join 
img = np.vstack([img_stack,img_stack2])

def text():
    #  position for text:
    menu1 = (45, 800)
    menu2 = (45, 820)
    menu3 = (45, 840)
    menu4 = (45, 860)
    # the menu:
    cv2.putText(img, 'simple left click and drag : add blue rectangle', menu1, cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255,255))
    cv2.putText(img, 'simple right click and drag : add green rectangle', menu2, cv2.FONT_HERSHEY_TRIPLEX, 0.5,(255, 255, 255))
    cv2.putText(img, 'press "r" : clear the screen', menu3, cv2.FONT_HERSHEY_TRIPLEX, 0.5,(255, 255, 255))
    cv2.putText(img, 'Press "q" to exit', menu4, cv2.FONT_HERSHEY_TRIPLEX, 0.5, (255, 255, 255))
text()
cv2.namedWindow('image')
# Connects the mouse button to our callback function
cv2.setMouseCallback('image',draw_rect)

while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    #press 'r' to reset the image
    if k == ord("r"):
        img = np.vstack([img_stack,img_stack2])
    #  pressed'q'to exit:    
    if k == ord("q"):
        break
    cv2.imshow('image',img)
    
cv2.destroyAllWindows()