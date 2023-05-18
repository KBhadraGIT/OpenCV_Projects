# HAND TRACKING PROJECT

This project uses two pre-built libraries:

| Pre-built libraries | Function |
|---------------------|----------|
| *Palm detection* | This library will crop out the images of palm, when a complete image is provided. |
| *Hand Landmarks* | This library will find 21 reference point from the cropped images. |

```mermaid
graph TD;
    [**IMAGE DATA**]-->[**PALM DETECTION Library**];
    [**PALM DETECTION Library**]--*Cropping hand images from the given image*-->[**HAND DETECTION LIBRARY**];
    [**HAND DETECTION LIBRARY**];
```