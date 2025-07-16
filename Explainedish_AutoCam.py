#How to access the camera's name to call with the following code

"""

go to 

/dev/v4l/by-id 

directory

"""

import cv2
import threading
#Resolution of Photo (With/Hight)
w=160 #852
h=120 #480

""" Start of Setting up a video resolution to camera and connecting to the camera 
(Copy Past with minor edits to numbers for each additional camera) """
cam0 = cv2.VideoCapture()

#Connecting to a specific camera (You have to set this up before hand [there may be muliple of each type, 
#test until you get the one that works and it will alwasy work. NEED TO UPDATE FOR NEW CAMERA'S AND MAYBE COMPUTER
cam0.open("/dev/v4l/by-id/usb-HD_Camera_Manufacturer_USB_2.0_Camera-video-index0")

print ('Default Resolution is ' + str(int(cam0.get(3))) + 'x' + str(int(cam0.get(4))))
cam0.set(3,w)
cam0.set(4,h)
print ('Now resolution is set to ' + str(w) + 'x' + str(h))
""" END if setting specs for camera """

#Code to show the video as a file on the deskto
def CamZero():
	ret, frame0 = cam0.read()
	cv2.imshow('Cam 0', frame0)

""" Start of Setting up a video resolution to camera and connecting to the camera 
(Copy Past with minor edits to numbers for each additional camera) """
cam1 = cv2.VideoCapture()

#Connecting to a specific camera (You have to set this up before hand [there may be muliple of each type, 
#test until you get the one that works and it will alwasy work. NEED TO UPDATE FOR NEW CAMERA'S AND MAYBE COMPUTER
cam1.open("/dev/v4l/by-id/usb-HD_Camera_Manufacturer_HD_USB_Camera_SN0001-video-index0")

print ('Default Resolution is ' + str(int(cam1.get(3))) + 'x' + str(int(cam1.get(4))))
cam1.set(3,w)
cam1.set(4,h)
print ('Now resolution is set to ' + str(w) + 'x' + str(h))
""" END if setting specs for camera """

#Code to show the video as a file on the desktop
def CamOne():
	ret, frame1 = cam1.read()
	cv2.imshow('Cam 1', frame1)

#Code to call the set ups and to allow for the video to work, also allows for exiting / closing camra's by using #1
while (True):
	
    # Capture frame-by-frame
    c1 = threading.Thread(target=CamZero)
    c2 = threading.Thread(target=CamOne)
    # Display the resulting frame
    c1.start()
    c2.start()
    c1.join()
    c2.join()
	#cv2.imshow(frame0 & frame1)
    # Wait for Escape Key
    if cv2.waitKey(1) == 27 :
        break

       

# When everything done, release the capture
cam0.release()
cam1.release()

cv2.destroyAllWindows()
