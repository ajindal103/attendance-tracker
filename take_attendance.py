from fileinput import filename
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import os
import mysql.connector
import cv2
from time import strftime
from datetime import datetime
from tkinter import filedialog

filename = ""
var = 0


# gif display
class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


class takeAttendance:
    def __init__(self, root, uID):
        self.root = root
        self.root.title("Take Attendance")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # background gif
        label_bg = ImageLabel(root, bg="black")
        label_bg.place(x=0, y=0, width=window_width, height=window_height)
        label_bg.load('images/take_attendance/background.gif')

        # main heading
        heading = Label(root, text="TAKE ATTENDANCE", font=(
            "roboto", 35, "bold"), fg="#004e64", bg="white")
        heading.place(x=0, y=50, relwidth=1)

        # timer
        def time():
            string = strftime("%H:%M:%S %p")
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(heading, font=("roboto", 12, "bold"),
                    fg="#004e64", bg="white")
        lbl.place(x=10, y=5, width=100, height=50)
        time()

        # back button
        back_button = Button(heading, text="Back", command=self.backbutton, font=(
            "roboto", 15, "bold"), bg="#004e64", fg="white", cursor="hand2", bd=0)
        back_button.place(x=window_width-130, y=16, height=30, width=80)

        # take attendance button
        take_attendance_btn = Button(root, command=lambda: self.faceRecognition(uID), text="Take Attendance", font=("roboto", 15, "bold"), bg="#004e64", fg="white",
                                     relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        take_attendance_btn.place(
            x=(window_width//2)-100, y=6*(window_height//7), width=200)

    # function to take attendance
    def mark_attendance(self, d, c, ye, s, n, r, ask, uID):
        global filename
        global var
        if (ask > 0 or var == 1):
            with open(filename, "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = []
                for line in myDataList:
                    entry = line.split((","))
                    name_list.append(entry[0])

                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                if (n not in name_list) and (r not in name_list) and (date not in name_list):
                    f.writelines(
                        f"\n{n},{r},{date},{time},{d},{c},{ye},{s}, Present")
        else:
            with open(filename, "a+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = []
                for line in myDataList:
                    entry = line.split((","))
                    name_list.append(entry[0])
                var = 1

                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                if (n not in name_list) and (r not in name_list) and (date not in name_list):
                    f.writelines(
                        f"{n},{r},{date},{time},{d},{c},{ye},{s}, Present")

        default = 'files'
        defaultFile = os.path.join(default, uID+'.csv')
        with open(defaultFile, "r+", newline="\n") as f:
            defaultMyDataList = f.readlines()
            default_name_list = []
            for line in defaultMyDataList:
                entry = line.split((","))
                default_name_list.append(entry[0])

            now = datetime.now()
            date = now.strftime("%d/%m/%Y")
            time = now.strftime("%H:%M:%S")
            if (n not in default_name_list) and (r not in default_name_list) and (date not in default_name_list):
                if default_name_list == []:
                    f.writelines(
                        f"{n},{r},{date},{time},{d},{c},{ye},{s}, Present")
                else:
                    f.writelines(
                        f"\n{n},{r},{date},{time},{d},{c},{ye},{s}, Present")

    # function to recognize face
    def faceRecognition(self, uID):
        global filename
        global var
        ask = messagebox.askyesno(
            "?", "Use an existing csv file?", parent=self.root)
        if ask > 0:
            var = 1
            filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select CSV File", filetypes=(
                ("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
        else:
            var = 0
            path = filedialog.askdirectory(
                title="Select Save Location", parent=self.root)
            date = datetime.now().strftime('%d_%m_%Y_%I_%M_%S')
            filename = os.path.join(path, "attendance"+f'_{date}' + ".csv")

        # function to draw rectangle and compare with classifier
        def draw_rectangle(img, classifier, scaleFactor, minNeigh, clf, ask, uID):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeigh)

            coordinates = []

            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int(100*(1-predict/300))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Anurag@2001", database="mydata")
                crsr = conn.cursor()

                crsr.execute(
                    "select name from student_details where userID=%s and studentID=" + str(id), (uID,))
                n = crsr.fetchone()
                n = "+".join(n)

                crsr.execute(
                    "select rollNo  from student_details where userID=%s and studentID=" + str(id), (uID,))
                r = crsr.fetchone()
                r = "+".join(r)

                crsr.execute(
                    "select course from student_details where userID=%s and studentID=" + str(id), (uID,))
                c = crsr.fetchone()
                c = "+".join(c)

                crsr.execute(
                    "select dep from student_details where userID=%s and studentID=" + str(id), (uID,))
                d = crsr.fetchone()
                d = "+".join(d)

                crsr.execute(
                    "select year from student_details where userID=%s and studentID=" + str(id), (uID,))
                ye = crsr.fetchone()
                ye = "+".join(ye)

                crsr.execute(
                    "select semester from student_details where userID=%s and studentID=" + str(id), (uID,))
                s = crsr.fetchone()
                s = "+".join(s)

                if confidence > 75:
                    cv2.putText(
                        img, f"Name: {n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll No.: {r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Course: {c}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(d, c, ye, s, n, r, ask, uID)
                else:
                    cv2.rectangle(
                        img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coordinates = [x, y, w, h]
            return coordinates

        def recognize(img, clf, faceCascade, ask, uID):
            coordinates = draw_rectangle(
                img, faceCascade, 1.1, 10, clf, ask, uID)
            return img

        faceCascade = cv2.CascadeClassifier(
            "files/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        folder = os.path.join('files', uID)
        file = os.path.join(folder, "classifier.xml")
        clf.read(file)

        capture = cv2.VideoCapture(0)

        while True:
            ret, frame = capture.read()
            frame = recognize(frame, clf, faceCascade, ask, uID)
            cv2.imshow("Recognizing Face...Press Enter to Stop", frame)

            if cv2.waitKey(1) == 13:
                break

        capture.release()
        cv2.destroyAllWindows()

    def backbutton(self):
        global filename
        filename = ""
        global var
        var = 0
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = takeAttendance(root)
    root.mainloop()
