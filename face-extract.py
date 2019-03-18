import sys,os
import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
def detect(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    roi_color = None
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    return roi_color

def read_img(source):
    img = cv.imread(source)
    print("Read complete.")
    return img
def read_vid(source):
    vidcap = cv.VideoCapture(source)
    length = int(vidcap.get(cv.CAP_PROP_FRAME_COUNT))
    success, image = vidcap.read()
    count = 0
    array = []
    while success:
        success, image = vidcap.read()
        array.append(image)
        print("%d of %d frames read." % (count, length), end = "\r")
        count += 1
    print("\nRead complete.")
    return array

def main():
    mode = sys.argv[1] # -p for photo processing. -v for video processing.
    file = sys.argv[2] # video file input
    if not os.path.isdir("./output/"):
        os.mkdir("./output/")
    img = None
    if (mode == "-p"):
        img = read_img(file)
        if img is not None:
            print(detect(img))
    elif (mode == "-v"):
        filename = file.split('\\')[2].split('.')[0]
        folder = "./output/" + file.split('\\')[2].split('.')[0]
        if not os.path.isdir(folder):
            os.mkdir(folder)
        img = read_vid(file)
        count = 0
        for i in img:
            if i is not None:
                roi = detect(i)
                if roi is not None:
                    print("Saving face: %d" % (count), end="\r")
                    cv.imwrite(folder + "/" + filename +  "-" + str(count) + ".jpg", roi)
                    count += 1
        print("\r%d faces found." % (count))
    else:
        print("Error: Invalid parameter.")

    print(str(len(img)))

    #roi = detect(img, mode)
    #print("Detection process complete.")
    #write(roi,file, mode)

main()
#print(str(sys.argv))
