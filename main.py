from time import strftime
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from add_student_details import addStudentDetails
from train_data import trainData, ImageLabel
from take_attendance import takeAttendance, ImageLabel
from attendance import attend
from about import aboutDeveloper
from tkinter import messagebox
from time import strftime


class attendanceTrackingSystem:
    def __init__(self, root, uID):
        self.root = root
        self.root.title("Attendance Tracking System")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # background image
        image = Image.open('images/background.png')
        dim: tuple = (window_width, window_height)
        image = image.resize(dim)
        self.bg = ImageTk.PhotoImage(image)
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # main heading
        heading = Label(label_bg, text="FACE RECOGNITION ATTENDANCE TRACKING SYSTEM", font=(
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

        # student details button
        img1 = Image.open('images/main_page/student_details.png')
        dim: tuple = (window_width//6, window_width//6)
        img1 = img1.resize(size=dim)
        self.photoimage1 = ImageTk.PhotoImage(img1)

        button1 = Button(label_bg, command=lambda: self.funcAddStudentDetails(uID),
                         image=self.photoimage1, cursor="hand2")
        button1.place(x=((window_width//6)-(window_width//12)), y=250, width=(
            window_width/6), height=(window_width/6))

        button1a = Button(label_bg, command=lambda: self.funcAddStudentDetails(uID), text="Add Student Details", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button1a.place(x=((window_width//6)-(window_width//12)), y=250+(window_width//6), width=(
            window_width/6)-1, height=40)

        # train data button
        img2 = Image.open('images/main_page/train_data.png')
        dim: tuple = (window_width//6, window_width//6)
        img2 = img2.resize(size=dim)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        button2 = Button(label_bg, command=lambda: self.funcTrainData(uID),
                         image=self.photoimage2, cursor="hand2")
        button2.place(x=((window_width//12)+(window_width//6)+(window_width//18)), y=250, width=(
            window_width/6), height=(window_width/6))

        button2a = Button(label_bg, command=lambda: self.funcTrainData(uID), text="Train Data", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button2a.place(x=((window_width//12)+(window_width//6)+(window_width//18)), y=250+(window_width//6), width=(
            window_width/6)-1, height=40)

        # face recognition button
        img3 = Image.open('images/main_page/face_recognition.png')
        dim: tuple = (window_width//6, window_width//6)
        img3 = img3.resize(size=dim)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        button3 = Button(label_bg, command=lambda: self.funcTakeAttendance(uID),
                         image=self.photoimage3, cursor="hand2")
        button3.place(x=((window_width//3)+(window_width//9)+(window_width//12)), y=250, width=(
            window_width/6), height=(window_width/6))

        button3a = Button(label_bg, command=lambda: self.funcTakeAttendance(uID), text="Take Attendance", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button3a.place(x=((window_width//3)+(window_width//9)+(window_width//12)), y=250+(window_width//6), width=(
            window_width/6)-1, height=40)

        # attendance tracking button
        img4 = Image.open('images/main_page/attendance.png')
        dim: tuple = (window_width//6, window_width//6)
        img4 = img4.resize(size=dim)
        self.photoimage4 = ImageTk.PhotoImage(img4)

        button4 = Button(label_bg, command=lambda: self.funcAttendance(uID),
                         image=self.photoimage4, cursor="hand2")
        button4.place(x=((window_width//2)+(window_width//12)+(window_width//6)), y=250, width=(
            window_width/6), height=(window_width/6))

        button4a = Button(label_bg, command=lambda: self.funcAttendance(uID), text="Attendance Details", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button4a.place(x=((window_width//2)+(window_width//12)+(window_width//6)), y=250+(window_width//6), width=(
            window_width/6)-1, height=40)

        # about button
        button3b = Button(label_bg, command=self.funcAbout, text="About", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button3b.place(x=((window_width//12)+(window_width//6)+(window_width//18)), y=700, width=(
            window_width/6)-1, height=40)

        # exit Button
        button4b = Button(label_bg, command=self.funcExit, text="Exit", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white", cursor="hand2", relief=FLAT, bd=0, activebackground="white", activeforeground="#004e64")
        button4b.place(x=((window_width//3)+(window_width//8)+(window_width//12)), y=700, width=(
            window_width/6)-1, height=40)

    # function of buttons
    def funcAddStudentDetails(self, uID):
        self.newWindow = Toplevel(self.root)
        self.app = addStudentDetails(self.newWindow, uID)

    def funcTrainData(self, uID):
        self.newWindow = Toplevel(self.root)
        self.app = trainData(self.newWindow, uID)

    def funcTakeAttendance(self, uID):
        self.newWindow = Toplevel(self.root)
        self.app = takeAttendance(self.newWindow, uID)

    def funcAttendance(self, uID):
        self.newWindow = Toplevel(self.root)
        self.app = attend(self.newWindow, uID)

    def funcAbout(self):
        self.newWindow = Toplevel(self.root)
        self.app = aboutDeveloper(self.newWindow)

    def funcExit(self):
        self.funcExit = messagebox.askyesno(
            "Exit", "Do you want to Exit?", parent=self.root)
        if self.funcExit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    app = attendanceTrackingSystem(root)
    root.mainloop()
