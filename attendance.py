from fileinput import filename
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import csv
from tkinter import filedialog
from time import strftime

myData = []
filename = ""


class attend:
    def __init__(self, root, uID):
        self.root = root
        self.root.title("Attendance Data")
        window_width = self.root.winfo_screenwidth()
        window_height = self.root.winfo_screenheight()
        self.root.geometry(f'{window_width}x{window_height}')
        root.state('zoomed')

        self.root.wm_iconbitmap("face.ico")

        # variables to enter data
        self.var_name = StringVar()
        self.var_rollNo = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_department = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_status = StringVar()
        self.var_rid = IntVar()

        # background image
        image = Image.open('images/background.png')
        dim: tuple = (window_width, window_height)
        image = image.resize(dim)
        self.bg = ImageTk.PhotoImage(image)
        label_bg = Label(self.root, image=self.bg)
        label_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # main heading
        heading = Label(label_bg, text="ATTENDANCE DATA", font=(
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

        # main frame
        main_frame = Frame(label_bg, bd=2, bg="white")
        main_frame.place(x=window_width//70, y=(window_height//20) + 90, width=window_width -
                         (window_width//35), height=(window_height)-4*(window_height//20))

        main_frame_width: int = window_width - (window_width//35)
        main_frame_height: int = (window_height)-(window_height//5)

        # left frame
        left_frame = LabelFrame(main_frame, bd=2, relief=SOLID, bg="white",
                                text="ATTENDANCE DETAILS", font=("roboto", 12, "bold"))
        left_frame.place(x=10, y=10, width=(
            main_frame_width//2)-20, height=main_frame_height-20)

        left_frame_width: int = (main_frame_width//2)-20
        left_frame_height: int = main_frame_height-20

        # Name label
        name_label = Label(left_frame, text="Name", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        name_label.grid(row=0, column=0, padx=left_frame_width //
                        25, pady=left_frame_height//25, sticky=E)

        # Name entry
        name_entry = Entry(left_frame, textvariable=self.var_name, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        name_entry.grid(row=0, column=1, padx=3, sticky=W)

        # roll number label
        roll_label = Label(left_frame, text="Roll Number", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        roll_label.grid(row=0, column=3, padx=left_frame_width //
                        25, pady=left_frame_height//25, sticky=E)

        # roll number entry
        roll_entry = Entry(left_frame, textvariable=self.var_rollNo, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        roll_entry.grid(row=0, column=4, padx=3, sticky=W)

        # department label
        department_label = Label(left_frame, text="Department", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        department_label.grid(row=1, column=0, padx=left_frame_width //
                              25, pady=left_frame_height//25, sticky=E)

        # department entry
        department_entry = Entry(left_frame, textvariable=self.var_department, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        department_entry.grid(row=1, column=1, padx=3, sticky=W)

        # course label
        course_label = Label(left_frame, text="Course", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        course_label.grid(row=1, column=3, padx=left_frame_width //
                          25, pady=left_frame_height//25, sticky=E)

        # course entry
        course_entry = Entry(left_frame, textvariable=self.var_course, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        course_entry.grid(row=1, column=4, padx=3, sticky=W)

        # year label
        year_label = Label(left_frame, text="Year", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        year_label.grid(row=2, column=0, padx=left_frame_width //
                        25, pady=left_frame_height//25, sticky=E)

        # year entry
        year_entry = Entry(left_frame, textvariable=self.var_year, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        year_entry.grid(row=2, column=1, padx=3, sticky=W)

        # semester label
        semester_label = Label(left_frame, text="Semester", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        semester_label.grid(row=2, column=3, padx=left_frame_width //
                            25, pady=left_frame_height//25, sticky=E)

        # semester entry
        semester_entry = Entry(left_frame, textvariable=self.var_semester, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        semester_entry.grid(row=2, column=4, padx=3, sticky=W)

        # date label
        date_label = Label(left_frame, text="Date", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        date_label.grid(row=3, column=0, padx=left_frame_width //
                        25, pady=left_frame_height//25, sticky=E)

        # date entry
        date_entry = Entry(left_frame, textvariable=self.var_date, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        date_entry.grid(row=3, column=1, padx=3, sticky=W)

        # time label
        time_label = Label(left_frame, text="Time", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        time_label.grid(row=3, column=3, padx=left_frame_width //
                        25, pady=left_frame_height//25, sticky=E)

        # time entry
        time_entry = Entry(left_frame, textvariable=self.var_time, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        time_entry.grid(row=3, column=4, padx=3, sticky=W)

        # status label
        status_label = Label(left_frame, text="Status", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        status_label.grid(row=4, column=0, padx=left_frame_width //
                          25, pady=left_frame_height//25, sticky=E)

        # status combo
        status_combo = ttk.Combobox(left_frame, textvariable=self.var_status, font=(
            "roboto", 11), width=left_frame_width//40, state="readonly")
        status_combo["values"] = (
            "--Select--", "Absent", "Present")
        status_combo.current(0)
        status_combo.grid(row=4, column=1, padx=3, sticky=W)

        # row_id label
        row_id_label = Label(left_frame, text="Row Id", font=(
            "roboto", 12, "bold"), fg="#004e64", bg="white")
        row_id_label.grid(row=4, column=3, padx=left_frame_width //
                          25, pady=left_frame_height//25, sticky=E)

        # row_id entry
        row_id_entry = Entry(left_frame, textvariable=self.var_rid, width=left_frame_width//35, font=(
            "roboto", 12), fg="#004e64", bg="white", bd=1, relief=SOLID, state="readonly")
        row_id_entry.grid(row=4, column=4, padx=3, sticky=W)

        # buttons frame
        btn_frame = Frame(left_frame, bd=0, relief=SOLID, bg="white")
        btn_frame.place(x=10, y=(left_frame_height//1.5), width=left_frame_width -
                        20, height=left_frame_height//6)

        btn_frame_width: int = left_frame_width-20
        btn_frame_height: int = left_frame_height//6

        # import button
        import_btn = Button(btn_frame, command=self.importCSV, text="Import CSV", font=("roboto", 14, "bold"), bg="#004e64", fg="white",
                            width=btn_frame_width//30, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        import_btn.grid(row=0, column=0, padx=btn_frame_width //
                        17, pady=btn_frame_height//10)

        # update button
        update_btn = Button(btn_frame, command=lambda: self.updateData(uID), text="Update", font=("roboto", 14, "bold"), bg="#004e64", fg="white",
                            width=btn_frame_width//30, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        update_btn.grid(row=0, column=1, padx=btn_frame_width //
                        17, pady=btn_frame_height//10)

        # export button
        export_btn = Button(btn_frame, command=self.exportCSV, text="Export CSV", font=("roboto", 14, "bold"), bg="#004e64", fg="white",
                            width=btn_frame_width//30, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        export_btn.grid(row=1, column=0, padx=btn_frame_width //
                        17, pady=btn_frame_height//10)

        # reset button
        reset_btn = Button(btn_frame, command=self.resetData, text="Reset", font=("roboto", 14, "bold"), bg="#004e64", fg="white",
                           width=btn_frame_width//30, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        reset_btn.grid(row=1, column=1, padx=btn_frame_width //
                       17, pady=btn_frame_height//10)

        # right frame
        right_frame = LabelFrame(main_frame, bd=2, relief=SOLID, bg="white",
                                 text="ATTENDANCE LIST", font=("roboto", 12, "bold"))
        right_frame.place(x=((main_frame_width)//2)+8, y=10, width=(
            main_frame_width//2)-20, height=main_frame_height-100)

        right_frame_width: int = (main_frame_width//2)-20
        right_frame_height: int = main_frame_height-100

        # clear button
        clear_btn = Button(main_frame, command=lambda: self.clearData(uID), text="Clear List", font=("roboto", 14, "bold"), bg="#004e64", fg="white",
                           width=right_frame_width//30, relief=FLAT, bd=0, activebackground="#004e64", activeforeground="white", cursor="hand2")
        clear_btn.place(
            x=(left_frame_width+(right_frame_width//2.5)), y=right_frame_height+20)

        # scroll bars & headings
        scrollX = ttk.Scrollbar(right_frame, orient=HORIZONTAL)
        scrollY = ttk.Scrollbar(right_frame, orient=VERTICAL)

        self.attendance_list = ttk.Treeview(right_frame, columns=("name", "rollNo", "date", "time", "dep", "course", "year", "sem",
                                                                  "status", "rid"), xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
        scrollX.pack(side=BOTTOM, fill=X)
        scrollY.pack(side=RIGHT, fill=Y)
        scrollX.config(command=self.attendance_list.xview)
        scrollY.config(command=self.attendance_list.yview)

        self.attendance_list.heading("name", text="Name")
        self.attendance_list.heading("rollNo", text="Roll No.")
        self.attendance_list.heading("date", text="Date")
        self.attendance_list.heading("time", text="Time")
        self.attendance_list.heading("dep", text="Department")
        self.attendance_list.heading("course", text="Course")
        self.attendance_list.heading("year", text="Year")
        self.attendance_list.heading("sem", text="Semester")
        self.attendance_list.heading("status", text="Status")
        self.attendance_list.heading("rid", text="Row ID")

        self.attendance_list["show"] = "headings"

        self.attendance_list.column("name", width=120)
        self.attendance_list.column("rollNo", width=90)
        self.attendance_list.column("date", width=80)
        self.attendance_list.column("time", width=80)
        self.attendance_list.column("dep", width=120)
        self.attendance_list.column("course", width=80)
        self.attendance_list.column("year", width=70)
        self.attendance_list.column("sem", width=70)
        self.attendance_list.column("status", width=80)
        self.attendance_list.column("rid", width=80)

        self.attendance_list.pack(fill=BOTH, expand=1)

        self.attendance_list.bind("<ButtonRelease>", self.getData)
        global myData
        myData.clear()
        self.fetchData(uID)

    # function to import csv data into table
    def importData(self, rows):
        self.attendance_list.delete(*self.attendance_list.get_children())
        for i in rows:
            self.attendance_list.insert("", END, values=i)
        self.resetData()

    # function to import csv
    def importCSV(self):
        global myData
        global filename
        myData.clear()
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select CSV file", filetypes=(
            ("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
        with open(filename) as myFile:
            csvRead = csv.reader(myFile, delimiter=",")
            for index, row in enumerate(csvRead):
                row.append(index+1)
                myData.append(row)
            self.importData(myData)

    # function to export csv:
    def exportCSV(self):
        try:
            if (len(myData) < 1):
                messagebox.showerror(
                    "Error", "No Data Found!", parent=self.root)
                return False
            filename1 = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Select Location & File Name", filetypes=(
                ("CSV File", "*csv"), ("All File", "*.*")), parent=self.root)
            filename1 = filename1 + ".csv"
            with open(filename1, mode="w", newline="") as myFile:
                csvWrite = csv.writer(myFile, delimiter=",")
                for i in myData:
                    csvWrite.writerow(i[:-1])
                messagebox.showinfo(
                    "Success", "Data Exported Successfully!", parent=self.root)
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to:{str(es)}", parent=self.root)

    # function to fetch data from default csv and show in list
    def fetchData(self, uID):
        global myData
        myData.clear()
        global filename
        if filename == "":
            default = 'files'
            filename = os.path.join(default, uID+'.csv')
        with open(filename) as myFile:
            csvRead = csv.reader(myFile, delimiter=",")
            for index, row in enumerate(csvRead):
                row.append(index+1)
                myData.append(row)
            self.importData(myData)

    # function to add data into field by clicking on list row
    def getData(self, event=""):
        cursor_focus = self.attendance_list.focus()
        content = self.attendance_list.item(cursor_focus)
        data = content["values"]

        self.var_name.set(data[0])
        self.var_rollNo.set(data[1])
        self.var_date.set(data[2])
        self.var_time.set(data[3])
        self.var_department.set(data[4])
        self.var_course.set(data[5])
        self.var_year.set(data[6])
        self.var_semester.set(data[7])
        self.var_status.set(data[8])
        self.var_rid.set(data[9])

    # function to reset data
    def resetData(self):
        self.var_name.set("")
        self.var_rollNo.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_department.set("")
        self.var_course.set("")
        self.var_year.set("")
        self.var_semester.set("")
        self.var_status.set("--Select--")
        self.var_rid.set("-")

    # function to update data
    def updateData(self, uID):
        if self.var_status.get() == "--Select--" or self.var_name.get() == "":
            messagebox.showerror(
                "Error", "Mark Absent/Present First!", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update Student Details?", parent=self.root)
                if Update > 0:
                    list = []
                    with open(filename, 'r') as b:
                        reader = csv.reader(b)
                        list.extend(reader)

                    lines = {self.var_rid.get()-1: [self.var_name.get(), self.var_rollNo.get(), self.var_date.get(), self.var_time.get(
                    ), self.var_department.get(), self.var_course.get(), self.var_year.get(), self.var_semester.get(), self.var_status.get()]}

                    with open(filename, 'w', newline='') as b:
                        writer = csv.writer(b)
                        for line, row in enumerate(list):
                            data = lines.get(line, row)
                            writer.writerow(data)

                    messagebox.showinfo(
                        "Updated", "Student Details updated successfully!", parent=self.root)
                    self.fetchData(uID)
                    self.resetData()
                else:
                    if not Update:
                        return

            except Exception as es:
                messagebox.showerror(
                    "Error", f"Error due to:{str(es)}", parent=self.root)

    def clearData(self, uID):
        try:
            delete = messagebox.askyesno(
                "Clear?", "Do you want to clear the Attendance Record List?", parent=self.root)
            if delete > 0:
                global filename
                # if filename == "":
                # default = 'files'
                # file = os.path.join(default, uID+'.csv')
                f = open(filename, "w+")
                # f.truncate(0)
                f.close()
                self.fetchData(uID)
                messagebox.showinfo(
                    "Success", "Attendance Record List has been Cleared!", parent=self.root)
            else:
                if not delete:
                    return
        except Exception as es:
            messagebox.showerror(
                "Error", f"Error due to:{str(es)}", parent=self.root)

    def backbutton(self):
        global filename
        filename = ""
        global myData
        myData = []
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    app = attend(root)
    root.mainloop()
