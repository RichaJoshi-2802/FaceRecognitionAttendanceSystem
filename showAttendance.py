import csv
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk




class showAttend:
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

        title_lbl = Label(label, text="ATTENDANCE",
                          font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=800, height=45)

        # main frame
        mainFrame = Frame(label, bd=2)
        mainFrame.place(x=50, y=70, width=700, height=550)


        rightFrame = LabelFrame(mainFrame, bd=2, relief=RIDGE, text="Student Details", font=("times new roman", 15, "bold"), bg="white", fg="red")
        rightFrame.place(x=100, y=10, width=500, height=500)



        file = open("attendance.csv")
        csvreader = csv.reader(file)
        rows = []
        for row in csvreader:
            rows.append(row)
        print(rows)

        i = 1
        for data in rows:

            for j in range(4):
                depLbl = ttk.Label(rightFrame, text=data[j], font=("times new roman", 12, "bold"))
                depLbl.grid(row=i, column=j, padx=5, pady=5)

            i += 1


if __name__ == "__main__":
    root = Tk()
    obj = showAttend(root)
    root.mainloop()