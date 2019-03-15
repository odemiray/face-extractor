import sys,os
import numpy as np
import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
def detect(img, mode):
    if(mode == "-p"):
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        roi_color = None
        for (x,y,w,h) in faces:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            if str(roi_color) != "":
                print("Found!")
        return roi_color
    elif(mode == "-v"):
        print("Detecting...")
        array = []
        for i in range(0,len(img)):
            frame = img[i]
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            roi_color = None
            for (x,y,w,h) in faces:
                cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                print("Face found.")
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                array.append(roi_color)
            return array
    else:
        print("Operation failed during detection.")

def read(source, mode):
    if mode == "-p":
        return cv.imread(source)
    elif mode == "-v":
        array = []
        vidcap = cv.VideoCapture(source)
        success = True
        i = 0
        while success:
            success,image = vidcap.read()
            #xwrite(image, i)
            array.append(image)
            i += 1
        return array
    else:
        print("Invalid argument")
        return np.zeros((1,1))
def write(img, name, mode):
    if (mode == "-p"):
        path = "./img/test_out.jpg"
        print(path)
        if(cv.imwrite(path, img)):
            print("Write complete.")
    elif(mode == "-v"):
        filename = name.replace(str(os.path.dirname), "")
        #os.mkdir(path=str(os.path.dirname) + filename, mode=0o777,dir_fd=None)
        for i in range(0, len(img)):
            cv.imwrite("./img/test/out_" + filename, img[i])
    else:
        print("Operation failed while writing results to disk.")
    #cv.imwrite("/img/out_" + name, img)


def xwrite(image, name):
    cv.imwrite("img/test/a" + str(name) + ".jpg", image)
    return 0
def main():
    mode = sys.argv[1]
    file = sys.argv[2]
    img = read(file, mode)
    print("Read complete.")
    roi = detect(img, mode)
    print("Detection process complete.")
    write(roi,file, mode)

main()
#print(str(sys.argv))
