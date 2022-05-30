from tkinter import *
from tkinter import ttk
import pyodbc
from PIL import Image, ImageTk



class showDetail:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x650+80+50")
        self.root.title("Student Management SYSTEM")

        # ========variables======

        self.var_dep = StringVar()
        self.var_year = StringVar()
        self.var_stdId = StringVar()
        self.var_stdName = StringVar()
        self.var_img = StringVar()

        img1 = Image.open("Images/uiImages/background.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label = Label(self.root, image=self.photoimg1)
        label.pack()
        label.place()

        title_lbl = Label(label, text="STUDENT DETAILS",
                          font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=800, height=45)

        # main frame
        mainFrame = Frame(label, bd=2)
        mainFrame.place(x=10, y=50, width=700, height=550)


        rightFrame = LabelFrame(mainFrame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"), bg="white", fg="red")
        rightFrame.place(x=100, y=10, width=500, height=500)

        depLbl = ttk.Label(rightFrame, text="Department", font=("times new roman", 12, "bold"))
        depLbl.grid(row=0, column=0, padx=10, pady=20)
        depLbl = ttk.Label(rightFrame, text="Year", font=("times new roman", 12, "bold"))
        depLbl.grid(row=0, column=1, padx=10, pady=20)
        depLbl = ttk.Label(rightFrame, text="University Roll No.", font=("times new roman", 12, "bold"))
        depLbl.grid(row=0, column=2, padx=10, pady=20)
        depLbl = ttk.Label(rightFrame, text="Name", font=("times new roman", 12, "bold"))
        depLbl.grid(row=0, column=3, padx=10, pady=20)
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-0R0Q8IQ;'
                              'Database=attendance;'
                              'Trusted_Connection=yes;')

        my_cursor = conn.cursor()

        my_cursor.execute('select * from attendance.dbo.stu_detail')
        a = my_cursor.fetchall()
        length = len(a)
        i = 1
        for data in a:
            for j in range(4):
                depLbl = ttk.Label(rightFrame, text=data[j], font=("times new roman", 12, "bold"))
                depLbl.grid(row=i, column=j, padx=5, pady=5)

            i += 1
        conn.commit()


if __name__ == "__main__":
    root = Tk()
    obj = showDetail(root)
    root.mainloop()
