import cv2
import easyocr
import  regex as re


# Frame Width
frameWidth = 640
# Frame Height
frameHeight = 480
# Setting the minimum area of the contour it is specific to the region
minArea = 500
# loading the pretrained engine for detecting the registration tag in the image
plateCascade = cv2.CascadeClassifier("C:/Users/s555694/Desktop/Gdp/haarcascade_russian_plate_number.xml")
# Emergency Vehicle detecting haarcascasde file
emgCascade = cv2.CascadeClassifier("C:/Users/s555694/Desktop/Gdp/cascade.xml")

ip = "https://192.168.1.148:8080/video"
# initializing the video camera
a = "C:/Users\s555694\Desktop\Gdp\p/4771.jpg"
#a = "C:/Users\s555694\Desktop\Gdp/n/0000.jpg"
cap =cv2.VideoCapture(a)
# setting the frame width
cap.set(3,frameWidth)
# setting the frame height
cap.set(4,frameHeight)
# setting the frame position
cap.set(10,150)
count = 0
text_in = ""
while True:
    # Reading the captured image
    success , img  = cap.read()
    # Converting image to gray scale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # finding plate co-ordinates
    numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
    # Emergency vehicle detection
    emgVehicle = emgCascade.detectMultiScale(imgGray, 1.11, 2)
    # looping through all the contours that are detected by the haarcascade_russian_plate_number.xml
    for (x, y, w, h) in emgVehicle:
        if w*h > 90000:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
            imgRoi1 = img[y:y + h, x:x + w]
            cv2.imwrite("C:/Users/s555694/Desktop/IMAGES/emgimg" + str(count) + ".jpg", imgRoi1)
            print("emg")
    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            # Drawing the rectangle where the contour is detected
            #  img lower left corner and upper right corner BGR and thickness
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            # make the img more darker to identify LPR
            #kernel = np.ones((1, 1), np.uint8)
            #imgRoi = cv2.dilate(imgRoi, kernel, iterations=1)
            #imgRoi = cv2.erode(imgRoi, kernel, iterations=1)
            #plate_gray = cv2.cvtColor(imgRoi, cv2.COLOR_BGR2GRAY)
            #(thresh, imgRoi) = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY)
            cv2.imshow("ROI",imgRoi)
            cv2.imwrite("C:/Users/s555694/Desktop/IMAGES/img" + str(count) + ".jpg", imgRoi)
            # setting the language for the OCR
            reader = easyocr.Reader(['en'])
            # getting the ROI image and extracting the text init
            output = reader.readtext("C:/Users/s555694/Desktop/IMAGES/img"+str(count)+".jpg")
            #print(output)
            # cleaning a string
            # checking whether the text is there or not in the ROI image
            if not (not output):
                text_in = output[0][-2]
            # Allow only alphanumaric in the text
            cleanString = re.sub('\W+', '', text_in)
            print(cleanString)
            # search in the data base.

            # predit the word
            cv2.waitKey(500)
            count += 1

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("C:/Users/s555694/Desktop/IMAGES/img"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    def remove(string):
        return string.replace(" ", "")