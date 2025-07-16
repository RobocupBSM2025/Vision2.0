#Test_Object_Detection_And_Tracking
import cv2 #CV2 = Cammera
import numpy as np #Python Library for working with arrays
import time # Python t=libray for timers, and keeping time

# Settings
withCam, heightCam = 640, 420  # Resolution - Does not need to be low as the frames are good and is not intefsive
fps = 15
delay = 1 / fps

# Camera setup
cam = cv2.VideoCapture(1) #Same Cammera sett up
cam.set(3, withCam)
cam.set(4, heightCam)
if not cam.isOpened():
    raise RuntimeError("Failed to open USB camera.")
print(f"QR Camera initialized at {withCam}x{heightCam} @ {fps} FPS")

# https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://www.youtube.com/watch%3Fv%3DO3b8lVF93jU%26pp%3DygUbI21vdGlvbnRyYWNraW5nc3RlcmVvdmlzaW9u&ved=2ahUKEwiN_eTcw7-OAxW6pZUCHZNGMWAQwqsBegQIBBAF&usg=AOvVaw0tTuBenjgpru3fLeLqj9xw
# Above video is the turorial I used to get this code combined with previous code for the Camera
# Not the best possible set up for motion detection but can be improved apon by using something different 
# Channel of video above also has tutorials on keras ocr which I only discoved after crating my own code and that code may be helpful in improving and understanding my own as I do not really undersatand the code the best

#ObjectDetector from Stable Camera (which it is not)
ObjectDetector = cv2.createBackgroundSubtractorMOG2() # There is likely a better procces but this works for now

try: #IDk
    while True: #Streamms the video

        start_time = time.time()

        ret, frame = cam.read() #Gets frame of the video
        if not ret:
            continue

        h_img, w_img, _ = frame.shape #Gets the hight and with of the image / frame

        mask = ObjectDetector.apply(frame) #Creates a black and white version of the frame where the white is I think movement or maybe light or (Likely light or something)
        _, mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY) #Makes it so that the shadows of objects are removed from the mask as the scale is from (0 or 1)to 255 with 255 being white and therefore makes it so only the white is allowed and all other data is removed
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Creates a border around the moving white area on the mask,(Was not explained in the tutorial)
        for cnt in contours: # Makes proccess work for every contour found
            area = cv2.contourArea(cnt) #Takes the total area of the countour to test
            if  area > 200: #Makes sure the area of the coutour and therefore ovement is big enough so little movements of the camera ot flickers of light of movements of the arm causing clothes to shift is not detected
                #The 200 is 200 pixels and is not connected to the resolution but rather something else (The video had it at 100 but in testing it was having to many extra things sensed so we went with 200)

                #cv2.drawContours(frame, [cnt], -1, (0, 255, 0), 1) 
                #Above is original code to just display the contours on the main video being streamed to the computer and not (IDK I lost my though as I was distacted when writing this)

                x, y, w, h = cv2.boundingRect(cnt) #Creates a bounding box around the moving object that takes the furthest x and y for the countours on one object so it displays on the x and y axis only 
                #If I have time I will look for the tutorial I found to make it so you can have bounding boxes that can be at an angle and not just x and y axes's

                rect = cv2.minAreaRect(cnt) # Tutorial for semi working (WIP) rotated bounding boxes - https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
                #Makes it take the minimun area
                box = cv2.boxPoints(rect) # IDK
                box = np.intp(box) #IDK
                cv2.drawContours(frame, [box], 0, (0, 255, 0), 2) #New Code that allows for the bounding boxes to at an angle (The old code and comments are below)
                #v2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2) # Create and displays the bounding box on the x and y axis only for teh collor Green (I think) abd with a line thinkness of 2

        cv2.imshow("Motion Detection", frame) #Creates a window with the alterations and the streamed video

        # cv2.imshow("Motion Detection Mask", mask)
        #Above displayes the black and white masks where the countours are detected if you want to test it and see what is going on behind the end result( If you are doing so I recomend using the draw coundours instead of the bounding box as it will enable more info into what you are rally looking at)

        if cv2.waitKey(1) & 0xFF == ord('q'): #Quites when q is pressed in a window
            break

        elapsed = time.time() - start_time
        time.sleep(max(0, delay - elapsed))

finally: #Closes the windows and stops streaming the video
    cam.release()
    cv2.destroyAllWindows()


#VS Code Run and Debug -> Python Debugger
    #PS C:\Users\Engineering\Desktop\Code_For_Camera>  c:; cd 'c:\Users\Engineering\Desktop\Code_For_Camera'; & 'c:\Users\Engineering\Desktop\Code_For_Camera\.venv\Scripts\python.exe' 'c:\Users\Engineering\.vscode\extensions\ms-python.debugpy-2025.10.0-win32-x64\bundled\libs\debugpy\launcher' '63797' '--' 'C:\Users\Engineering\Desktop\Code_For_Camera\.venv(Not_For_Compition_But_Documentation)\#Test_Object_Detection_And_Tracking.py'
    #QR Camera initialized at 640x420 @ 15 FPS
