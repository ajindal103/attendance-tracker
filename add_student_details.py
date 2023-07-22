from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
from time import strftime
import os


class addStudentDetails:
    def __init__(self, root, uID):
        self.root = root
        self.root.title("Add Student Details")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # variables to enter data
        self.var_sid = IntVar()
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_name = StringVar()
        self.var_rollNo = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_phone = StringVar()
        self.var_email = StringVar()

        # background image
        image = Image.open('images/background.png')
        dim: tuple = (window_width, window_height)
        image = image.resize(dim)
        # image = image.resize((2500,1000))
        self.bg = ImageTk.PhotoImage(image)
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # main heading
        heading = Label(label_bg, text="ADD STUDENT DETAILS", font=(
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
        main_frame = Frame(label_bg, bd=2, bg="white")
        main_frame.place(x=window_width//70, y=(window_height//20) + 90, width=window_width -
                         (window_width//35), height=(window_height)-4*(window_height//20))

        main_frame_width: int = window_width - (window_width//35)
        main_frame_height: int = (window_height)-(window_height//5)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=SOLID, bg="white",
                                text="ADD DATA", font=("roboto", 12, "bold"))
        left_frame.place(x=10, y=10, width=(
            main_frame_width//2)-20, height=main_frame_height-20)

        left_frame_width: int = (main_frame_width//2)-20
        left_frame_height: int = main_frame_height-20

        # course information frame
        course_frame = LabelFrame(left_frame, bd=1, relief=SOLID, bg="white",
                                  text="COURSE INFORMATION", font=("roboto", 12, "bold"))
        course_frame.place(x=10, y=20, width=left_frame_width -
                           22, height=left_frame_height//6)

        course_frame_width: int = left_frame_width-22
        course_frame_height: int = left_frame_height//6

        # course frame label and entry
        # department label
        department_label = Label(course_frame, text="Department", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        department_label.grid(row=0, column=0, padx=course_frame_width //
                              25, pady=course_frame_height//25, sticky=E)

        # department combo
        department_combo = ttk.Combobox(course_frame, textvariable=self.var_department, font=(
            "roboto", 10), width=course_frame_width//30, state="readonly")
        department_combo["values"] = ("--Select Department--", "Computer Department",
                                      "Mechanical Department", "Electrical Department", "Civil Department")
        department_combo.current(0)
        department_combo.grid(row=0, column=1, padx=3, sticky=W)

        # course label
        course_label = Label(course_frame, text="Course", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        course_label.grid(row=0, column=3, padx=course_frame_width //
                          25, pady=course_frame_height//25, sticky=E)

        # course combo
        course_combo = ttk.Combobox(course_frame, textvariable=self.var_course, font=(
            "roboto", 10), width=course_frame_width//30, state="readonly")
        course_combo["values"] = ("--Select Course--", "B.Tech. CE", "B.Tech. IT", "B.Tech. CEDS",
                                  "B.Tech. ME", "B.Tech. ENC", "B.Tech. ECE", "B.Tech. IOT", "B.Tech. Civil")
        course_combo.current(0)
        course_combo.grid(row=0, column=4, padx=3, sticky=W)

        # year label
        year_label = Label(course_frame, text="Year", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        year_label.grid(row=1, column=0, padx=course_frame_width //
                        25, pady=course_frame_height//25, sticky=E)

        # year combo
        year_combo = ttk.Combobox(course_frame, textvariable=self.var_year, font=(
            "roboto", 10), width=course_frame_width//30, state="readonly")
        year_combo["values"] = ("--Select Year--", "1st", "2nd", "3rd", "4th")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=3, sticky=W)

        # semester label
        semester_label = Label(course_frame, text="Semester", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        semester_label.grid(row=1, column=3, padx=course_frame_width //
                            25, pady=course_frame_height//25, sticky=E)

        # semester combo
        semester_combo = ttk.Combobox(course_frame, textvariable=self.var_semester, font=(
            "roboto", 10), width=course_frame_width//30, state="readonly")
        semester_combo["values"] = (
            "--Select Semester--", "1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=4, padx=3, sticky=W)

        # student information frame
        student_info_frame = LabelFrame(left_frame, bd=1, relief=SOLID, bg="white",
                                        text="STUDENT INFORMATION", font=("roboto", 12, "bold"))
        student_info_frame.place(x=10, y=60+(left_frame_height//6),
                                 width=left_frame_width-22, height=left_frame_height//1.45)

        student_info_frame_width: int = left_frame_width-22
        student_info_frame_height: int = left_frame_height//1.45

        # student info frame label and entry
        # student_id label
        student_id_label = Label(student_info_frame, text="Id:", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        student_id_label.grid(row=0, column=1, padx=student_info_frame_width //
                              25, pady=student_info_frame_height//35, sticky=E)

        # student_id entry
        student_id_entry = Entry(student_info_frame, textvariable=self.var_sid, width=student_info_frame_width//45, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        student_id_entry.grid(row=0, column=3, padx=3, sticky=W)

        # Name label
        name_label = Label(student_info_frame, text="Name", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        name_label.grid(row=1, column=0, padx=student_info_frame_width //
                        25, pady=student_info_frame_height//25, sticky=E)

        # Name entry
        name_entry = Entry(student_info_frame, textvariable=self.var_name, width=student_info_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID)
        name_entry.grid(row=1, column=1, padx=3, sticky=W)

        # roll number label
        roll_label = Label(student_info_frame, text="Roll Number", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        roll_label.grid(row=1, column=3, padx=student_info_frame_width //
                        25, pady=student_info_frame_height//25, sticky=E)

        # roll number entry
        roll_entry = Entry(student_info_frame, textvariable=self.var_rollNo, width=student_info_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID)
        roll_entry.grid(row=1, column=4, padx=3, sticky=W)

        # gender label
        gender_label = Label(student_info_frame, text="Gender", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        gender_label.grid(row=2, column=0, padx=student_info_frame_width //
                          25, pady=student_info_frame_height//25, sticky=E)

        # gender combo
        gender_combo = ttk.Combobox(student_info_frame, textvariable=self.var_gender, font=(
            "roboto", 10), width=student_info_frame_width//30, state="readonly")
        gender_combo["values"] = (
            "--Select Gender--", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=3, sticky=W)

        # dob label
        dob_label = Label(student_info_frame, text="DOB", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        dob_label.grid(row=2, column=3, padx=student_info_frame_width //
                       25, pady=student_info_frame_height//25, sticky=E)

        # dob entry
        dob_entry = Entry(student_info_frame, textvariable=self.var_dob, width=student_info_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID)
        dob_entry.grid(row=2, column=4, padx=3, sticky=W)

        # email label
        email_label = Label(student_info_frame, text="Email Id", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        email_label.grid(row=3, column=0, padx=student_info_frame_width //
                         25, pady=student_info_frame_height//25, sticky=E)

        # email entry
        email_entry = Entry(student_info_frame, textvariable=self.var_email, width=student_info_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID)
        email_entry.grid(row=3, column=1, padx=3, sticky=W)

        # phone label
        phone_label = Label(student_info_frame, text="Phone No.", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        phone_label.grid(row=3, column=3, padx=student_info_frame_width //
                         25, pady=student_info_frame_height//25, sticky=E)

        # phone entry
        phone_entry = Entry(student_info_frame, textvariable=self.var_phone, width=student_info_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID)
        phone_entry.grid(row=3, column=4, padx=3, sticky=W)

        # buttons frame
        btn_frame = Frame(student_info_frame, bd=0, relief=SOLID, bg="white")
        btn_frame.place(x=10, y=(left_frame_height//2.5), width=student_info_frame_width -
                        20, height=student_info_frame_height//6)

        btn_frame_width: int = student_info_frame_width-20
        btn_frame_height: int = student_info_frame_height//6

        # save button
        save_btn = Button(btn_frame, command=lambda: self.addData(uID), text="Save", font=("roboto", 12, "bold"), bg="#004e64", fg="white",
                          width=btn_frame_width//25, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        save_btn.grid(row=0, column=0, padx=btn_frame_width //
                      17, pady=btn_frame_height//10)

        # update button
        update_btn = Button(btn_frame, command=lambda: self.updateData(uID), text="Update", font=("roboto", 12, "bold"), bg="#004e64", fg="white",
                            width=btn_frame_width//25, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        update_btn.grid(row=0, column=1, padx=btn_frame_width //
                        17, pady=btn_frame_height//10)

        # delete button
        delete_btn = Button(btn_frame, command=lambda: self.deletedata(uID), text="Delete", font=("roboto", 12, "bold"), bg="#004e64", fg="white",
                            width=btn_frame_width//25, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        delete_btn.grid(row=1, column=0, padx=btn_frame_width //
                        17, pady=btn_frame_height//10)

        # reset button
        reset_btn = Button(btn_frame, command=self.resetData, text="Reset", font=("roboto", 12, "bold"), bg="#004e64", fg="white",
                           width=btn_frame_width//25, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        reset_btn.grid(row=1, column=1, padx=btn_frame_width //
                       17, pady=btn_frame_height//10)

        # buttons frame 1
        btn_frame1 = Frame(student_info_frame, bd=0, relief=SOLID, bg="white")
        btn_frame1.place(x=10, y=(left_frame_height//2.5)+(btn_frame_height)+10, width=student_info_frame_width -
                         20, height=student_info_frame_height//6)

        btn_frame_width1: int = student_info_frame_width-20
        btn_frame_height1: int = student_info_frame_height//6

        # update photo sample button
        update_photo_sample_btn = Button(btn_frame1, command=lambda: self.takePhotoSample("XX", uID), text="Update Photo Sample", font=(
            "roboto", 12, "bold"), bg="#004e64", fg="white", width=btn_frame_width1//19, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        update_photo_sample_btn.place(
            x=(btn_frame_width1//2)-170, y=15, height=40)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=SOLID, bg="white",
                                 text="STUDENT DETAILS", font=("roboto", 12, "bold"))
        right_frame.place(x=((main_frame_width)//2)+8, y=10, width=(
            main_frame_width//2)-20, height=main_frame_height-20)

        right_frame_width: int = (main_frame_width//2)-20
        right_frame_height: int = main_frame_height-20

        # search frame
        search_frame = LabelFrame(right_frame, bd=1, relief=SOLID, bg="white",
                                  text="SEARCH", font=("roboto", 12, "bold"))
        search_frame.place(x=10, y=20, width=right_frame_width -
                           22, height=right_frame_height//6)

        search_frame_width: int = right_frame_width-22
        search_frame_height: int = right_frame_height//6

        # search system
        # search label
        search_label = Label(search_frame, text="Search:", font=(
            "roboto", 15, "bold"), fg="#004e64", bg="white")
        search_label.place(x=(search_frame_width//36)-10, y=20,
                           width=(search_frame_width//6)-20)

        # search combo
        self.var_searchC = StringVar()
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchC, font=(
            "roboto", 14), state="readonly")
        search_combo["values"] = (
            "Select", "Dep", "Course", "Year", "Semester", "Name", "RollNo")
        search_combo.current(0)
        search_combo.place(x=(search_frame_width//18)-40 +
                           (search_frame_width//6), y=20, width=(search_frame_width//6)+50)

        # search entry
        self.var_searchE = StringVar()
        search_entry = Entry(search_frame, textvariable=self.var_searchE, font=(
            "roboto", 15), fg="#004e64", bg="white", bd=1, relief=SOLID)
        search_entry.place(x=((search_frame_width//12) +
                           (search_frame_width//3)), y=20, width=(search_frame_width//6)+60)

        # search button
        search_btn = Button(search_frame, command=lambda: self.searchData(uID), text="Search", font=("roboto", 12), bg="#004e64", fg="white",
                            relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        search_btn.place(x=((search_frame_width//9) +
                         (search_frame_width//2))+60, y=20, width=(search_frame_width//6)-20)

        # show all button
        showAll_btn = Button(search_frame, command=lambda: self.fetchData(uID), text="Show All", font=("roboto", 12), bg="#004e64", fg="white",
                             relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        showAll_btn.place(x=(5*(search_frame_width//36) +
                             4*(search_frame_width//6))+30, y=20, width=(search_frame_width//6)-20)

        # student list frame
        student_list_frame = LabelFrame(right_frame, bd=1, relief=SOLID, bg="white",
                                        text="STUDENT LIST", font=("roboto", 12, "bold"))
        student_list_frame.place(x=10, y=60+(right_frame_height//6),
                                 width=right_frame_width-22, height=right_frame_height//1.45)

        student_list_frame_width: int = right_frame_width-22
        student_list_frame_height: int = right_frame_height//1.45

        # scroll bars & headings
        scrollX = ttk.Scrollbar(student_list_frame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(student_list_frame, orient=VERTICAL)

        self.student_list = ttk.Treeview(student_list_frame, columns=("studentID", "dep", "course", "year", "sem", "name", "rollNo",
                                                                      "gen", "dob", "email", "phone"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.student_list.xview)
        scrollY.config(command=self.student_list.yview)

        self.student_list.heading("studentID", text="Id")
        self.student_list.heading("dep", text="Department")
        self.student_list.heading("course", text="Course")
        self.student_list.heading("year", text="Year")
        self.student_list.heading("sem", text="Semester")
        self.student_list.heading("name", text="Name")
        self.student_list.heading("rollNo", text="Roll No.")
        self.student_list.heading("gen", text="Gender")
        self.student_list.heading("dob", text="DOB")
        self.student_list.heading("email", text="Email")
        self.student_list.heading("phone", text="Phone No.")

        self.student_list["show"] = "headings"

        self.student_list.column("studentID", width=60)
        self.student_list.column("dep", width=150)
        self.student_list.column("course", width=100)
        self.student_list.column("year", width=60)
        self.student_list.column("sem", width=70)
        self.student_list.column("name", width=120)
        self.student_list.column("rollNo", width=90)
        self.student_list.column("gen", width=60)
        self.student_list.column("dob", width=80)
        self.student_list.column("email", width=150)
        self.student_list.column("phone", width=90)

        self.student_list.pack(fill=BOTH, expand=1)
        self.student_list.bind("<ButtonRelease>", self.getData)
        self.fetchData(uID)

    # function to add data
    def addData(self, uID):
        if self.var_department.get() == "--Select Department--" or self.var_course.get() == "--Select Year--" or self.var_year.get() == "--Select Year--" or self.var_semester.get() == "--Select Semester--" or self.var_name.get() == "" or self.var_rollNo.get() == "" or self.var_dob.get() == "" or self.var_phone.get() == "" or self.var_gender.get() == "--Select Gender--" or self.var_email.get() == "":
            messagebox.showerror(
                "Error", "All fields are required!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Anurag@2001", database="mydata")
                crsr = conn.cursor()
                crsr.execute("insert into student_details values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_sid.get(),
                    self.var_department.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_name.get(),
                    self.var_rollNo.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    uID
                ))
                conn.commit()
                user_id = crsr.lastrowid
                messagebox.showinfo(
                    "Success", "Student Details Added Successfully!", parent=self.root)
                messagebox.showinfo(
                    "Add", "Add Photo Sample", parent=self.root)
                self.takePhotoSample(user_id, uID)
                conn.close()
                self.fetchData(uID)
                self.resetData()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root)

    # adding data to right frame table
    def fetchData(self, uID):
        conn = mysql.connector.connect(
            host="localhost", user="root", password="Anurag@2001", database="mydata")
        crsr = conn.cursor()
        crsr.execute("select * from student_details where userID=%s", (uID,))
        data = crsr.fetchall()
        if len(data) != 0:
            self.student_list.delete(*self.student_list.get_children())
            for i in data:
                self.student_list.insert("", END, values=i[:-1])
            conn.commit()
        conn.close()

    # function to get data in form by click in row of the table
    def getData(self, event=""):
        cursor_focus = self.student_list.focus()
        content = self.student_list.item(cursor_focus)
        data = content["values"]

        self.var_sid.set(data[0])
        self.var_department.set(data[1])
        self.var_course.set(data[2])
        self.var_year.set(data[3])
        self.var_semester.set(data[4])
        self.var_name.set(data[5])
        self.var_rollNo.set(data[6])
        self.var_gender.set(data[7])
        self.var_dob.set(data[8])
        self.var_email.set(data[9])
        self.var_phone.set(data[10])

    # function to update data
    def updateData(self, uID):
        if self.var_department.get() == "--Select Department--" or self.var_course.get() == "--Select Year--" or self.var_year.get() == "--Select Year--" or self.var_semester.get() == "--Select Semester--" or self.var_name.get() == "" or self.var_rollNo.get() == "" or self.var_dob.get() == "" or self.var_phone.get() == "" or self.var_gender.get() == "--Select Gender--" or self.var_email.get() == "":
            messagebox.showerror(
                "Error", "All fields are required!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to Update Student Details?", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Anurag@2001", database="mydata")
                    crsr = conn.cursor()
                    crsr.execute("update student_details set dep=%s,course=%s,year=%s,semester=%s,name=%s,gender=%s,dob=%s,email=%s,phone=%s, rollNo=%s where studentID=%s and userID=%s", (
                        self.var_department.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_rollNo.get(),
                        self.var_sid.get(),
                        uID
                    ))
                    conn.commit()
                    self.fetchData(uID)
                    conn.close()
                    messagebox.showinfo(
                        "Updated", "Student Details updated successfully!", parent=self.root)
                    self.resetData()
                else:
                    if not Update:
                        return

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root)

    # function to delete data
    def deletedata(self, uID):
        if self.var_sid.get() == "0":
            messagebox.showerror(
                "Error", "Id is required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete?", "Do you want to delete this Student Details?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", user="root", password="Anurag@2001", database="mydata")
                    crsr = conn.cursor()
                    crsr.execute(
                        "delete from student_details where studentID=%s and userID=%s", (self.var_sid.get(), uID))
                    for i in range(1, 101):
                        path = os.path.join('data', uID)
                        filename = "user." + \
                            str(self.var_sid.get()) + "." + str(i) + ".jpg"
                        filepath = os.path.join(path, filename)
                        os.remove(filepath)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Deleted", "Student Details has been Deleted!", parent=self.root)
                    self.fetchData(uID)
                    self.resetData()
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root)

    # function to reset data
    def resetData(self):
        self.var_sid.set("0")
        self.var_department.set("--Select Department--")
        self.var_course.set("--Select Course--")
        self.var_year.set("--Select Year--")
        self.var_semester.set("--Select Semester--")
        self.var_name.set("")
        self.var_rollNo.set("")
        self.var_gender.set("--Select Gender--")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")

    # function to take photo sample
    def takePhotoSample(self, id, uID):
        try:

            if id == "XX":
                user_id = self.var_sid.get()
                self.resetData()
            else:
                user_id = id

            # load face data using haarcascade classifier
            faceClassifier = cv2.CascadeClassifier(
                "files/haarcascade_frontalface_default.xml")

            def faceCropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                # scaling factor=1.3, min neighbour=5
                faces = faceClassifier.detectMultiScale(gray, 1.3, 5)

                for (x, y, w, h) in faces:
                    faceCropped = img[y:y+h, x:x+w]
                    return faceCropped

            capture = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, frame = capture.read()
                if faceCropped(frame) is not None:
                    img_id += 1
                    face = cv2.resize(faceCropped(frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                    sample = os.path.join('data', uID)

                    data_path = "user." + \
                        str(user_id)+"."+str(img_id)+".jpg"
                    data_path2 = os.path.join(sample, data_path)
                    cv2.imwrite(data_path2, face)
                    cv2.putText(face, str(img_id), (50, 50),
                                cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("Cropped Face", face)
                if cv2.waitKey(1)==13 or int(img_id) == 100:
                    break

            capture.release()
            cv2.destroyAllWindows()
            messagebox.showinfo(
                "Success", "Photo Sample Added Successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to:{str(es)}", parent=self.root)

    # function to search data
    def searchData(self, uID):
        if self.var_searchC.get() == "Select" or self.var_searchE.get() == "":
            messagebox.showerror(
                "Error", "Enter data to search!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="Anurag@2001", database="mydata")
                crsr = conn.cursor()
                crsr.execute("select * from student_details where " + str(
                    self.var_searchC.get()) + " LIKE '%"+str(self.var_searchE.get())+"%'" + " and userID LIKE '%" + uID + "%'")
                # crsr.execute('select * from student_details where userID=%s and ')
                data = crsr.fetchall()
                if len(data) != 0:
                    self.student_list.delete(*self.student_list.get_children())
                    for i in data:
                        self.student_list.insert("", END, values=i)
                    conn.commit()
                else:
                    messagebox.showerror(
                        "Not found", "No such entry found!", parent=self.root)
                conn.close()
            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = addStudentDetails(root)
    root.mainloop()
