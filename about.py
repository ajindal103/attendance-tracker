from tkinter import *
from PIL import Image, ImageTk
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
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


class aboutDeveloper:
    def __init__(self, root):
        self.root = root
        self.root.title("About")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # background gif
        label_bg = ImageLabel(root, bg="black")
        label_bg.place(x=0, y=-100, width=window_width,
                       height=window_height+100)
        label_bg.load('images/about/background.webp')

        # main heading
        heading = Label(root, text="ABOUT DEVELOPER", font=(
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

        # main frame
        main_frame = Frame(root, bd=0, bg="black")
        main_frame.place(x=0, y=50*(window_height//70) +
                         90, height=(window_height//8), relwidth=1)

        # about
        about1 = Label(main_frame, text="Developed By:", font=(
            "roboto", 15, "bold"), fg="white", bg="black")
        about1.place(x=0, y=10, relwidth=1)

        about2 = Label(main_frame, text="AKRITI BHAN", font=(
            "roboto", 15, "bold"), fg="white", bg="black")
        about2.place(x=0, y=40, relwidth=1)
        about2 = Label(main_frame, text="ANURAG JINDAL", font=(
            "roboto", 15, "bold"), fg="white", bg="black")
        about2.place(x=0, y=65, relwidth=1)

        # about3 = Label(main_frame, text="ajindal103@gmail.com", font=(
        #     "roboto", 15, "bold"), fg="white", bg="black")
        # about3.place(x=0, y=70, relwidth=1)


if __name__ == "__main__":
    root = Tk()
    app = aboutDeveloper(root)
    root.mainloop()
