Code description:

# HandTracking_demo.py

### 1. Importing the necessary libraries:
```
import cv2
import mediapipe as mp
import time
```
### 2. Initializing the video capture:
```
cap = cv2.VideoCapture(1)
```
This line creates a VideoCapture object cap to capture video frames from the webcam. The parameter 1 indicates the index of the webcam to be used (usually 0 is the built-in webcam, and 1 is an external webcam).

### 3. Setting up the MediaPipe hands module:
```
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
```
These lines import the MediaPipe hands module and create an instance of the Hands class to detect hand landmarks. The drawing_utils module is imported to draw the landmarks and connections on the image.

### 4. Initializing variables for FPS calculation:
```
pTime = 0
cTime = 0
```
These variables will be used to calculate the frames per second (FPS) of the video stream.

### 5. Main loop for video processing:
```
while True:
```
This loop continuously reads frames from the video stream and performs hand landmark detection and visualization.

### 6. Reading a frame from the video stream:
```
success, img = cap.read()
```
The ```cap.read()``` function reads a frame from the video capture object (cap) and returns two values: success (a boolean indicating if the frame was successfully read) and img (the frame itself).

### 7. Converting the image color space:
```
imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
```
The ```cv2.cvtColor()``` function converts the color space of the image from BGR (the default color space used by OpenCV) to RGB, which is the color space expected by the MediaPipe hands module.

### 8. Processing the image to detect hand landmarks:
```
results = hands.process(imgRGB)
```
The ```hands.process()``` function takes the RGB image as input and returns the results of hand landmark detection. The results object contains information about the detected hands and their landmarks.

### 9. Detecting and visualizing hand landmarks:
```
if results.multi_hand_landmarks:
    for handLms in results.multi_hand_landmarks:
        for id, lm in enumerate(handLms.landmark):
            h, w, c = img.shape
            cx, cy = int(lm.x * w), int(lm.y * h)
            print(id, cx, cy)
            cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
        mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
```
If results.multi_hand_landmarks is not empty, it means that at least one hand was detected. The code then iterates over each detected hand (handLms) and each landmark within the hand (lm). For each landmark, it calculates the pixel coordinates (cx, cy) by scaling the normalized landmark coordinates with respect to the image dimensions. It also draws a filled circle at (cx, cy) on the image using the ```cv2.circle()``` function. Finally, the ```mpDraw.draw_landmarks()``` function is used to draw the hand landmarks and connections on the image.

### 10. Calculating the FPS:
```
cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime
```
These lines calculate the frames per second (FPS) of the video stream by measuring the time difference between the current frame (cTime) and the previous frame (pTime). The FPS value is computed as the reciprocal of the time difference.

### 11. Displaying the FPS on the image:
```
cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
```
This line adds a text annotation to the image using the ```cv2.putText()``` function. It displays the FPS value as text at the position (10, 70) on the image. The text is formatted as an integer, and it uses a purple color (255, 0, 255) with a font size of 3 and a thickness of 3.

### 12. Displaying the processed image:
```
cv2.imshow("Image", img)
cv2.waitKey(1)
```
These lines display the processed image in a window titled ```"Image"``` using the ```cv2.imshow()``` function. The ```cv2.waitKey(1)``` function waits for a keyboard event for 1 millisecond. It allows the image window to be updated and refreshed.

The code continues to loop through the video frames, continuously detecting hand landmarks, visualizing them on the image, calculating the FPS, and displaying the processed image. Pressing the "Esc" key will exit the program and close the image window.