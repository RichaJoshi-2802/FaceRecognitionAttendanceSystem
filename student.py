import tkinter.filedialog
from tkinter import *
from tkinter import ttk
import pyodbc
from PIL import Image, ImageTk
from tkinter import messagebox


conn = pyodbc.connect('Driver={SQL Server};'
                                      'Server=DESKTOP-0R0Q8IQ;'
                                      'Database=attendance;'
                                      'Trusted_Connection=yes;')

my_cursor = conn.cursor()
class student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x650+80+50")
        self.root.title("Student Management SYSTEM")

        # ========variables======

        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_stdId = StringVar()
        self.var_stdName = StringVar()

        img1 = Image.open("Images/uiImages/background.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label = Label(self.root, image=self.photoimg1)
        label.pack()
        label.place()

        title_lbl = Label(label, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1000, height=45)

        # main frame
        mainFrame = Frame(label, bd=2)
        mainFrame.place(x=5, y=50, width=990, height=570)

        # left frame
        leftFrame = LabelFrame(mainFrame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"), bg="white", fg="blue")
        leftFrame.place(x=10, y=10, width=970, height=530)


        # current course
        curr = LabelFrame(leftFrame, bd=2, relief=RIDGE, text="Student Information", font=("times new roman", 12, "bold"), bg="white", fg="blue")
        curr.place(x=150, y=10, width=670, height=530)

        # department
        depLbl = ttk.Label(curr, text="Department", font=("times new roman", 12, "bold"))
        depLbl.grid(row=0, column=3,  padx=10, pady=20)

        depCombo = ttk.Combobox(curr,  textvariable=self.var_dep, font=("times new roman", 12, "bold"), state="readonly")
        depCombo['values'] = ("Select Department", "CSE", "EE", "ME", "ECE", "CE")
        depCombo.current(0)
        depCombo.grid(row=0, column=4, padx=10, pady=20)

        # Year
        yearLbl = ttk.Label(curr, text="Select Year", font=("times new roman", 12, "bold"))
        yearLbl.grid(row=1, column=3, padx=10, pady=20)

        yearCombo = ttk.Combobox(curr, textvariable=self.var_year, font=("times new roman", 12, "bold"), state="readonly")
        yearCombo['values'] = ("Select Year", "First", "Second", "Third", "Fourth")
        yearCombo.current(0)
        yearCombo.grid(row=1, column=4, padx=10, pady=20)


        # University I'd

        idLbl = ttk.Label(curr,  text="University Id :", font=("times new roman", 12, "bold"))
        idLbl.grid(row=2, column=3, padx=10, pady=20)

        idEntry = ttk.Entry(curr, textvariable=self.var_stdId,  width=20, font=("times new roman", 12, "bold"))
        idEntry.grid(row=2, column=4, padx=10, pady=20)

        # name

        nameLbl = ttk.Label(curr,  text="Student Name :", font=("times new roman", 12, "bold"))
        nameLbl.grid(row=3, column=3, padx=10, pady=20)

        nameEntry = ttk.Entry(curr, textvariable=self.var_stdName, width=20, font=("times new roman", 12, "bold"))
        nameEntry.grid(row=3, column=4, padx=10, pady=20)

        # image label

        imgLbl = ttk.Label(curr, text="Upload Image", font=("times new roman", 12, "bold"))
        imgLbl.grid(row=4, column=3, padx=10, pady=20)

        button = ttk.Button(curr, text="Upload", width=20, command=lambda: upload_file())
        button.grid(row=4, column=4, padx=10, pady=10)



        # button

        b1 = Button(curr, text="  Save  ", command=self.addData, cursor="hand2", font=("times new roman", 15, "bold"), bg="black",
                    fg="green")
        b1.place(x=170, y=350, width=100, height=50)


        def upload_file():
            f_type = [('Jpg files', '*.jpg'), ('Jpeg files', '*.jpeg'), ('png files', '*.png')]
            filename = tkinter.filedialog.askopenfilename(filetypes=f_type)
            # with open(filename, 'rb') as file:
            #     binaryData = file.read()
            # return binaryData


    def addData(self):
        if self.var_dep.get() == "Select Department" or self.var_year.get() == "Select Year" or self.var_stdId.get() == "" or self.var_stdName.get() == "":
            messagebox.showerror("Error", "!!All Fields are Required!!", parent=self.root)
        else:
            try:
                val = (self.var_dep.get(), self.var_year.get(), self.var_stdId.get(), self.var_stdName.get())

                query = '''insert into attendance.dbo.stu_detail (department, year, rollno, name) values(?, ?, ?, ?)'''
                my_cursor.execute(query, val)
                conn.commit()
                conn.close()

                messagebox.showinfo("success", "Student details has been added successfully", parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error", "Due to :{str(es)}", parent=self.root)




if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()
