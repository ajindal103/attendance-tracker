from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import attendanceTrackingSystem
import string
import random
import os

def main():
    win = Tk()
    app = loginWindow(win)
    win.mainloop()


# login window
class loginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # login page background
        image = Image.open('images/background.png')
        dim: tuple = (window_width, window_height)
        image = image.resize(dim)
        self.bg = ImageTk.PhotoImage(image)
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # login section frame
        frame = Frame(self.root, bg="white",)
        frame.place(x=(window_width/2)-170, y=(window_height/2) -
                    225, width=340, height=450)

        # login head image
        login_image = Image.open("images/login/login.png")
        login_image = login_image.resize((100, 100))
        self.photo_login_image = ImageTk.PhotoImage(login_image)
        label_login_image = Label(self.root,
                                  image=self.photo_login_image, bg="white", borderwidth=0)
        label_login_image.place(x=(window_width/2)-50,
                                y=(window_height/2)-220, width=100, height=100)

        # login label
        log_in = Label(frame, text="LOGIN", font=(
            "roboto", 20, "bold"), bg="white", fg="#004e64")
        log_in.place(x=127, y=100)

        # username label
        username_label = Label(frame, text="Username", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        username_label.place(x=35, y=170)

        # username entry
        self.txtuser = Entry(frame, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtuser.place(x=30, y=195, width=280, height=24)

        # password label
        password_label = Label(frame, text="Password", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        password_label.place(x=35, y=240)

        # password entry
        self.txtpass = Entry(frame, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64", show="*")
        self.txtpass.place(x=30, y=265, width=280, height=24)

        # login button
        login_button = Button(frame, command=self.login, text="Login", font=(
            "roboto", 12, "bold"), relief=FLAT, fg="white", bg="#004e64", activeforeground="white", activebackground="#004e64", cursor="hand2", bd=0)
        login_button.place(x=110, y=310, width=120, height=35)

        # new user button
        register_button = Button(frame, text="Not Registered? Click Here!", command=self.registerWin, font=(
            "roboto", 11), borderwidth=0, relief=FLAT, bg="white", fg="#004e64", activebackground="white", activeforeground="#004e64", cursor="hand2")
        register_button.place(x=35, y=375)

        # forgot password button
        forgot_button = Button(frame, command=self.forgotPasswordWindow, text="Forgot Password?", font=(
            "roboto", 11), borderwidth=0, relief=FLAT, bg="white", fg="#004e64", activebackground="white", activeforeground="#004e64", cursor="hand2")
        forgot_button.place(x=35, y=400)

    # function to open register window by clicking on register button
    def registerWin(self):
        self.new_window = Toplevel(self.root)
        self.app = registerWindow(self.new_window)

    # login function
    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror(
                "Error", "Enter Username/Password!", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Anurag@2001", database="mydata")
            crsr = conn.cursor()
            crsr.execute("select * from face_recognition where email=%s and password=%s", (
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row = crsr.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Invalid Username/Password!", parent=self.root)
            else:
                self.new_window = Toplevel(self.root)
                self.app = attendanceTrackingSystem(self.new_window, row[0])
            conn.commit()
            conn.close()

    # function to reset password
    def reset_password(self):
        if self.combosecq.get() == "--Select":
            messagebox.showerror(
                "Error", "Select Security Question!", parent=self.root2)
        elif self.txtseca.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Security Answer!", parent=self.root2)
        elif self.txtnewpass.get() == "":
            messagebox.showerror(
                "Error", "Please Enter New Password!", parent=self.root2)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Anurag@2001", database="mydata")
            crsr = conn.cursor()
            query = (
                "select * from face_recognition where email=%s and securityQ=%s and securityA=%s")
            value = (self.txtuser.get(),
                     self.combosecq.get(), self.txtseca.get())
            crsr.execute(query, value)
            row = crsr.fetchone()
            if row == None:
                messagebox.showerror(
                    "Error", "Please Enter Correct Security Answer!", parent=self.root2)
            else:
                query = ("update face_recognition set password=%s where email=%s")
                value = (self.txtnewpass.get(), self.txtuser.get())
                crsr.execute(query, value)

                conn.commit()
                conn.close()
                messagebox.showinfo(
                    "Success", "Password Changed Successfully!", parent=self.root2)
                self.root2.destroy()

    # reset password window
    def forgotPasswordWindow(self):
        if self.txtuser.get() == "":
            messagebox.showerror(
                "Error", "Please Enter Username!", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Anurag@2001", database="mydata")
            crsr = conn.cursor()
            query = ("select * from face_recognition where email=%s")
            value = (self.txtuser.get(),)
            crsr.execute(query, value)
            row = crsr.fetchone()
            if row == None:
                messagebox.showerror(
                    "Invalid", "Invalid Username!", parent=self.root)
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forgot Password?")
                self.root2.geometry("340x420+550+170")

                forgot_password_label = Label(self.root2, text="Forgot Password?", font=(
                    "roboto", 20, "bold"), fg="#004e64")
                forgot_password_label.place(x=0, y=20, relwidth=1)

                # security ques label
                securityq_label = Label(self.root2, text="Select Security Question", font=(
                    "roboto", 12, "bold"), fg="#004e64")
                securityq_label.place(x=35, y=90)

                # security ques entry
                self.combosecq = ttk.Combobox(
                    self.root2, font=("roboto", 12), state="readonly")
                self.combosecq["values"] = (
                    "--Select--", "Your Birth Place", "Your Father's Last Name", "Your Best Friend's Name")
                self.combosecq.place(x=30, y=115, width=280, height=24)
                self.combosecq.current(0)

                # security ans label
                securitya_label = Label(self.root2, text="Security Answer", font=(
                    "roboto", 12, "bold"), fg="#004e64")
                securitya_label.place(x=35, y=160)

                # security ans entry
                self.txtseca = Entry(self.root2,  font=(
                    "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
                self.txtseca.place(x=30, y=185, width=280, height=24)

                # new password label
                new_password_label = Label(self.root2, text="New Password", font=(
                    "roboto", 12, "bold"), fg="#004e64")
                new_password_label.place(x=35, y=230)

                # new password entry
                self.txtnewpass = Entry(self.root2,  font=(
                    "roboto", 12), bd=1, relief=SOLID, fg="#004e64", show="*")
                self.txtnewpass.place(x=30, y=255, width=280, height=24)

                # reset password button
                reset_password_button = Button(self.root2, command=self.reset_password, text="Reset Password", font=(
                    "roboto", 12, "bold"), relief=FLAT, fg="white", bg="#004e64", activeforeground="white", activebackground="#004e64")
                reset_password_button.place(x=100, y=330, width=140, height=35)


# register window
class registerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_cfmpass = StringVar()

        # register page background
        image1 = Image.open('images/background.png')
        dim: tuple = (window_width, window_height)
        image1 = image1.resize(dim)
        self.bg = ImageTk.PhotoImage(image1)
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # register section frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=(window_width/2)-390, y=(window_height/2) -
                     275, width=780, height=550)

        # register head image
        register_image = Image.open("images/register/register.png")
        register_image = register_image.resize((100, 100))
        self.photo_register_image = ImageTk.PhotoImage(register_image)
        label_register_image = Label(self.root,
                                     image=self.photo_register_image, bg="white", borderwidth=0)
        label_register_image.place(x=(window_width/2)-50,
                                   y=(window_height/2)-270, width=100, height=100)

        # register label
        register_new = Label(frame1, text="REGISTER", font=(
            "roboto", 20, "bold"), bg="white", fg="#004e64")
        register_new.place(x=325, y=100)

        # firstname label
        firstname_label = Label(frame1, text="First Name", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        firstname_label.place(x=45, y=170)

        # firstname entry
        self.txtfname = Entry(frame1, textvariable=self.var_fname, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtfname.place(x=40, y=195, width=280, height=24)

        # lastname label
        lastname_label = Label(frame1, text="Last Name", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        lastname_label.place(x=465, y=170)

        # lastname entry
        self.txtlname = Entry(frame1, textvariable=self.var_lname, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtlname.place(x=460, y=195, width=280, height=24)

        # contact label
        contact_label = Label(frame1, text="Contact", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        contact_label.place(x=45, y=240)

        # contact entry
        self.txtcontact = Entry(frame1, textvariable=self.var_contact, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtcontact.place(x=40, y=265, width=280, height=24)

        # email label
        email_label = Label(frame1, text="Email", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        email_label.place(x=465, y=240)

        # email entry
        self.txtemail = Entry(frame1, textvariable=self.var_email, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtemail.place(x=460, y=265, width=280, height=24)

        # security ques label
        securityq_label = Label(frame1, text="Select Security Question", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        securityq_label.place(x=45, y=310)

        # security ques entry
        self.combosecq = ttk.Combobox(
            frame1, textvariable=self.var_securityQ, font=("roboto", 12), state="readonly")
        self.combosecq["values"] = (
            "--Select--", "Your Birth Place", "Your Father's Last Name", "Your Best Friend's Name")
        self.combosecq.place(x=40, y=335, width=280, height=24)
        self.combosecq.current(0)

        # security ans label
        securitya_label = Label(frame1, text="Security Answer", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        securitya_label.place(x=465, y=310)

        # security ans entry
        self.txtseca = Entry(frame1, textvariable=self.var_securityA, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64")
        self.txtseca.place(x=460, y=335, width=280, height=24)

        # password label
        password_label = Label(frame1, text="Password", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        password_label.place(x=45, y=380)

        # password entry
        self.txtpassword = Entry(frame1, textvariable=self.var_pass, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64", show="*")
        self.txtpassword.place(x=40, y=405, width=280, height=24)

        # Confirm Password label
        confirm_password_label = Label(frame1, text="Confirm Password", font=(
            "roboto", 12, "bold"), bg="white", fg="#004e64")
        confirm_password_label.place(x=465, y=380)

        # confirm password entry
        self.txtcfmpassword = Entry(frame1, textvariable=self.var_cfmpass, font=(
            "roboto", 12), bd=1, relief=SOLID, fg="#004e64", show="*")
        self.txtcfmpassword.place(x=460, y=405, width=280, height=24)

        # register button
        register_button = Button(frame1, command=self.register, text="Register", font=(
            "roboto", 12, "bold"), relief=FLAT, fg="white", bg="#004e64", activeforeground="white", activebackground="#004e64", cursor="hand2", bd=0)
        register_button.place(x=330, y=465, width=120, height=35)

        # already registered button
        log_in_button = Button(frame1, command=self.return_login, text="Already Registered? Login Now!", font=(
            "roboto", 11), borderwidth=0, relief=FLAT, bg="white", fg="#004e64", activebackground="white", activeforeground="#004e64", cursor="hand2")
        log_in_button.place(x=280, y=510)

    # register function
    def register(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_email.get() == "" or self.var_contact.get() == "" or self.var_securityA.get() == "" or self.var_pass.get() == "" or self.var_cfmpass.get() == "" or self.var_securityQ.get() == "--Select--":
            messagebox.showerror(
                "Error", "All fields are required!", parent=self.root)
        elif self.var_pass.get() != self.var_cfmpass.get():
            messagebox.showerror(
                "Error", "Password & Confirm Password Must be Same!", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", user="root", password="Anurag@2001", database="mydata")
            crsr = conn.cursor()
            query = ("select * from face_recognition where email=%s")
            value = (self.var_email.get(),)
            crsr.execute(query, value)
            row = crsr.fetchone()
            if row != None:
                messagebox.showerror(
                    "Error", "User Already Exists!", parent=self.root)
            else:
                n = 12
                uID = ''.join(random.choices(string.ascii_letters, k=n))
                crsr.execute("insert into face_recognition values(%s,%s,%s,%s,%s,%s,%s,%s)", (
                    str(uID),
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                messagebox.showinfo(
                    "Success", "Successfully Registered!", parent=self.root)
                os.mkdir(os.path.join('data', uID))
                os.mkdir(os.path.join('files', uID))
                file = os.path.join('files', uID+'.csv')
                with open(file, "a+") as f:
                    pass
            conn.commit()
            conn.close()

    # return to login window on clicking already registered button
    def return_login(self):
        self.root.destroy()


if __name__ == "__main__":
    main()
