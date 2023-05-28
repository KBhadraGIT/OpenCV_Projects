# HAND TRACKING PROJECT

This project uses two pre-built libraries:

| Pre-built libraries | Function |
|---------------------|----------|
| *Palm detection* | This library will crop out the images of palm, when a complete image is provided. |
| *Hand Landmarks* | This library will find 21 reference/Landmark point from the cropped images. You can go through the code of Mediapipe's hand function here -> https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/hands.py|

In the following flow the data will be processed:

```IMAGE DATA --> PALM DETECTION LIBRARY --> HAND LANDMARKS LIBRARY```

*HandTracking_demo.py*: this code demonstrates how to use the MediaPipe hands module in OpenCV to detect and track hand landmarks in real-time from a webcam feed and visualize them on the captured frames.

```NOTE: For better understanding of the code go through CODE_DESCRIPTION.md file```