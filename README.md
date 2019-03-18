# face-extractor

Face Extractor is a tool for creating facial datasets from videos. It simply reads the input data (photo or video), scans for any faces in it and if it finds a face, it crops it and prints it to output folder without modifying original input file.


## Requirements

- OpenCV ```pip install opencv-python```
- Numpy ```pip install numpy```
- haarcascade_frontalface_default.xml [Official @opencv Repository/Haarcascades](https://github.com/opencv/opencv/tree/master/data/haarcascades)


## Usage

- **Photo Mode:**
```py face_extract.py -p image.jpg``` (probably works with all extensions)

- **Video Mode:**
```py facedetect.py -v test.mp4``` (only tested in mp4)


## Licensing:
Do whatever the fuck you want to do with it.


## F.A.Q.
-**Why?**

I am working on a school project with @mustafaalby which is about face-recognition technologies. We need to train a model and we wanted to create our own dataset for training.
