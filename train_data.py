from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import os
import numpy as np
import cv2
from time import strftime


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


class trainData:
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
        label_bg.load('images/train_data/background.gif')

        # main heading
        heading = Label(root, text="TRAIN DATA", font=(
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
        back_button = Button(heading, text="Back", command=self.root.destroy, font=(
            "roboto", 15, "bold"), bg="#004e64", fg="white", cursor="hand2", bd=0)
        back_button.place(x=window_width-130, y=16, height=30, width=80)

        # train data button
        train_data_btn = Button(root, command=lambda: self.classifyData(uID), text="Train Data", font=("roboto", 15, "bold"), bg="#004e64", fg="white",
                                relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        train_data_btn.place(x=(window_width//2)-75, y=6 *
                             (window_height//7), width=150)

    # function to train dataset
    def classifyData(self, uID):
        data_dir = os.path.join('data', uID)
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        user_ids = []

        for image in path:
            img = Image.open(image).convert('L')  # gray scale image conversion
            image_np = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(image_np)
            user_ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13

        user_ids = np.array(user_ids)

        # train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, user_ids)
        folder = os.path.join('files', uID)
        file = os.path.join(folder, "classifier.xml")
        clf.write(file)
        cv2.destroyAllWindows()
        messagebox.showinfo(
            "Success", "Dataset Trained Successfully!", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = trainData(root)
    root.mainloop()
