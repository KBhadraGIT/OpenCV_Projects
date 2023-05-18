# HAND TRACKING PROJECT

This project uses two pre-built libraries:

| Pre-built libraries | Function |
|---------------------|----------|
| *Palm detection* | This library will crop out the images of palm, when a complete image is provided. |
| *Hand Landmarks* | This library will find 21 reference point from the cropped images. |

In the following flow the data will be processed:

``IMAGE DATA --> PALM DETECTION LIBRARY --> HAND LANDMARKS LIBRARY``