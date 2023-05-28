import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

#For the reference you can go through the README.md
mpHands = mp.solutions.hands
hands = mpHands.Hands()
# This daw.utils have prebuilt lines or curve between the landmark points.
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    #NOTE: Here the capture image is always in BGR format
    success, img = cap.read()
    #Converting the capture image to RGB colour since the mediapipe.solution.hands 
    # can only process RGB colour images.
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    #Processing the RGB image
    results = hands.process(imgRGB)
    
    #For multiple hands
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                #Here, to convert the location from decimal to int we are multiplying 
                # x-axis co-ordinate with width and y-axis co-ordinate with height
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(id, cx, cy)
                # if id == 4:
                cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)

            #The mediapipe.solutions.drawing_utils.py uses BGR colour image to locate the Landmarks.
            #Here, HAND_CONNECTIONS will connect the Landmarks.
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    
    #Setup for fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    # To show the fps on the screen
    cv2.putText(img, # Image Object name where we are putting the text, the image object should be in matrix format
                str(int(fps)), # The text we want to put on the image object
                (10, 70), # Position of the text
                cv2.FONT_HERSHEY_PLAIN, # Font type of the text
                3, # Font scale value
                (255, 0, 255), # Colour of the text
                3) # Text thickness
    
    #This is to run the webcam
    cv2.imshow("Image", img)
    cv2.waitKey(1)