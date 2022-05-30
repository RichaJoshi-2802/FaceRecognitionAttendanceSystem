from tkinter import *
from PIL import Image, ImageTk
from student import student
from attend import attendance
from showDetail import showDetail
from showAttendance import showAttend


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x650+80+50")
        self.root.title("FACE RECOGNITION ATTENDANCE SYSTEM")



        img1 = Image.open("Images/uiImages/background.png")
        self.photoimg1 = ImageTk.PhotoImage(img1)
        label = Label(self.root, image=self.photoimg1)
        label.pack()
        label.place()
    #
    #
        title_lbl = Label(label, text="FACE RECOGNITION ATTENDANCE MANAGEMENT SYSTEM", font=("times new roman", 25, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1000, height=45)
    #
    #
        # btn 1
        img2 = Image.open("Images/uiImages/detail.png")
        img2.resize((180,180))
        self.photoimg2 = ImageTk.PhotoImage(img2)
        b1 = Button(label, image=self.photoimg2, command=self.stuDetail, cursor="hand2")
        b1.place(x=100, y=100, width=200, height=200)

        b2 = Button(label, text="Add Student", command=self.stuDetail, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red")
        b2.place(x=100, y=300, width=200, height=40)

        # btn 2
        img3 = Image.open("Images/uiImages/attendanceT.png")
        self.photoimg3 = ImageTk.PhotoImage(img3)

        b3 = Button(label, image=self.photoimg3, command=self.attendancet, cursor="hand2")
        b3.place(x=100, y=360, width=200, height=200)

        b4 = Button(label, text="Take Attendance", command=self.attendancet, cursor="hand2", font=("times new roman", 15, "bold"), bg="white", fg="red")
        b4.place(x=100, y=560, width=200, height=40)

        # btn 3

        img4 = Image.open("Images/uiImages/attendShow.png")
        img4.resize((200, 200))
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b5 = Button(label, image=self.photoimg4, command=self.attendS, cursor="hand2")
        b5.place(x=350, y=100, width=200, height=200)

        b6 = Button(label, text="Attendance Details", command=self.attendS, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="white", fg="red")
        b6.place(x=350, y=300, width=200, height=40)

        # button 4
        img5 = Image.open("Images/uiImages/stdetail.png")
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b7 = Button(label, image=self.photoimg5, command=self.show, cursor="hand2")
        b7.place(x=350, y=360, width=200, height=200)

        b8 = Button(label, text="Student Details", command=self.show, cursor="hand2",
                    font=("times new roman", 15, "bold"), bg="white", fg="red")
        b8.place(x=350, y=560, width=200, height=40)


    def stuDetail(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def attendancet(self):
        self.new_window = Toplevel(self.root)
        self.app = attendance(self.new_window)

    def show(self):
        self.new_window = Toplevel(self.root)
        self.app = showDetail(self.new_window)


    def attendS(self):
        self.new_window = Toplevel(self.root)
        self.app = showAttend(self.new_window)






if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
