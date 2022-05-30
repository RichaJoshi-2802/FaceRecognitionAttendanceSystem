from tkinter import *
import cv2
import numpy as np
import face_recognition
import os
import pyodbc
from datetime import datetime


conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-0R0Q8IQ;'
                              'Database=attendance;'
                              'Trusted_Connection=yes;')

cursor = conn.cursor()


class attendance:
    def __init__(self, root):
        self.root = root

        path = "Images/studentImages"
        img = []
        classNames = []

        myList = os.listdir(path)    # file
        print(myList)

        for cls in myList:
            curImg = cv2.imread(f'{path}/{cls}')
            img.append(curImg)
            classNames.append(os.path.splitext(cls)[0])
        print(classNames)


        def findEncodings(img):
            encodeList = []
            for i in img:
                i = cv2.cvtColor(i, cv2.COLOR_BGR2RGB)
                encode = face_recognition.face_encodings(i)[0]
                encodeList.append(encode)
            print("encoding complete")
            return encodeList


        def markAttendance(name, dept):
            with open('attendance.csv', 'r+') as f:
                myDataList = f.readlines()
                namelist = []
                for line in myDataList:
                    entry = line.split(',')
                    namelist.append(entry[0])
                if name not in namelist:
                    now = datetime.now()
                    dstring = now.strftime('%d/%m/%Y')
                    tstring = now.strftime('%H:%M:%S')
                    f.writelines(f'\n{name},{tstring},{dstring},{dept}')


        encodeListKnown = findEncodings(img)
        print(encodeListKnown)
        print(len(encodeListKnown))

        cap = cv2.VideoCapture(0)   # to open web cam

        # phone as webcam
        # address = "https://192.168.43.1:8080/video"
        # cap.open(address)

        while True:
            success, im = cap.read()
            imgS = cv2.resize(im, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            faceCurFrame = face_recognition.face_locations(imgS)
            encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)



            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:

                    name = classNames[matchIndex].upper()
                    name1 = name.lower()
                    cursor.execute("select * from attendance.dbo.stu_detail where name = ?", name1)
                    record = cursor.fetchone()
                    new = record[0]

                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                    cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    cv2.putText(im, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                    cv2.putText(im, new, (y1+6,y2), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

                    markAttendance(name, new)

                else:
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(im, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(im, "Unknown", (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)


            cv2.imshow("Web Cam", im)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = attendance(root)
