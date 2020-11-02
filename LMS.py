from tkinter import *
import tkinter.messagebox
import LibBksDatabase
import os


#FRONTEND
#============================================LOGIN and REGISTER========================================================#


def delete2():
    screen3.destroy()


def delete3():
    screen4.destroy()


def delete4():
    screen5.destroy()


def login_sucess():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("Success")
    screen3.geometry("150x100")
    Label(screen3, text="Login Sucess").pack()
    Button(screen3, text="OK", command=screen.quit).pack()


def password_not_recognised():
    global screen4
    screen4 = Toplevel(screen)
    screen4.title("Success")
    screen4.geometry("150x100")
    Label(screen4, text="Password Error").pack()
    Button(screen4, text="OK", command=delete3).pack()


def user_not_found():
    global screen5
    screen5 = Toplevel(screen)
    screen5.title("Success")
    screen5.geometry("150x100")
    Label(screen5, text="User Not Found").pack()
    Button(screen5, text="OK", command=delete4).pack()


def register_user():
    print("working")

    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(screen1, text="Registration Success", fg="green", font=("calibri", 11)).pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
        else:
            password_not_recognised()

    else:
        user_not_found()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title("Register")
    screen1.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(screen1, text="Please enter details below").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username * ").pack()

    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password * ").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", width=10, height=1, command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("300x250")
    Label(screen2, text="Please enter details below to login").pack()
    Label(screen2, text="").pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    Label(screen2, text="Username * ").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Password * ").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", width=10, height=1, command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.iconbitmap("logo.ico")
    screen.geometry("300x250")
    screen.title("Library Management System")
    Label(text="Library Management System", bg="orange", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    screen.mainloop()


main_screen()


#======================================================================================================================#


class Library:

    def __init__(self, root):
        self.root = root
        self.root.title(" Library Management System ")
        self.root.geometry("1350x750+0+0")
        self.root.iconbitmap("logo.ico")

        MTy = StringVar()
        Ref = StringVar()
        Title = StringVar()
        Fna = StringVar()
        Sna = StringVar()
        Adr1 = StringVar()
        Adr2 = StringVar()
        Pcd = StringVar()
        MNo = StringVar()
        BkID = StringVar()
        BkT = StringVar()
        Atr = StringVar()
        DBo = StringVar()
        Ddu = StringVar()
        sPr = StringVar()
        Lrf = StringVar()
        Dod = StringVar()
        DonL = StringVar()

        #============================================FUNCTION DECLARATIONS============================================#
        def iExit():
            iExit = tkinter.messagebox.askyesno(" LMS ", "Are you sure you want to Exit ?")
            if iExit > 0:
                root.destroy()
                return

        def ClearData():
            self.txtMType.delete(0, END)
            self.txtBkID.delete(0, END)
            self.txtRef.delete(0, END)
            self.txtBkT.delete(0, END)
            self.txtTitle.delete(0, END)
            self.txtAtr.delete(0, END)
            self.txtFna.delete(0, END)
            self.txtSna.delete(0, END)
            self.txtDdu.delete(0, END)
            self.txtAdr1.delete(0, END)
            self.txtAdr2.delete(0, END)
            self.txtDonL.delete(0, END)
            self.txtLrf.delete(0, END)
            self.txtPcd.delete(0, END)
            self.txtDod.delete(0, END)
            self.txtMNo.delete(0, END)
            self.txtsPr.delete(0, END)
            self.txtDbo.delete(0, END)

        def addData():
            if(len(MTy.get())!=0):
                LibBksDatabase.addDataRec(MTy.get(), Ref.get(), Title.get(), Fna.get(), Sna.get(),Adr1.get(), Adr2.get(),
                                          Pcd.get(), MNo.get(), BkID.get(), BkT.get(), Atr.get(), DBo.get(), Ddu.get(),
                                          sPr.get(), Lrf.get(), Dod.get(), DonL.get())

                Booklist.delete(0, END)
                Booklist.insert(END, (MTy.get(), Ref.get(), Title.get(), Fna.get(), Sna.get(),Adr1.get(), Adr2.get(),
                                          Pcd.get(), MNo.get(), BkID.get(), BkT.get(), Atr.get(), DBo.get(), Ddu.get(),
                                          sPr.get(), Lrf.get(), Dod.get(), DonL.get()))

        def DisplayData():
            Booklist.delete(0, END)
            for row in LibBksDatabase.viewData():
                Booklist.insert(END, row)

        def SelectedBook(event):
            global sb
            searchBk = Booklist.curselection()[0]
            sb = Booklist.get(searchBk)

            self.txtMType.delete(0, END)
            self.txtMType.insert(END, sb[1])

            self.txtRef.delete(0, END)
            self.txtRef.insert(END, sb[2])

            self.txtTitle.delete(0, END)
            self.txtTitle.insert(END, sb[3])

            self.txtFna.delete(0, END)
            self.txtFna.insert(END, sb[4])

            self.txtSna.delete(0, END)
            self.txtSna.insert(END, sb[5])

            self.txtAdr1.delete(0, END)
            self.txtAdr1.insert(END, sb[6])

            self.txtAdr2.delete(0, END)
            self.txtAdr2.insert(END, sb[7])

            self.txtPcd.delete(0, END)
            self.txtPcd.insert(END, sb[8])

            self.txtMNo.delete(0, END)
            self.txtMNo.insert(END, sb[9])

            self.txtBkID.delete(0, END)
            self.txtBkID.insert(END, sb[10])

            self.txtBkT.delete(0, END)
            self.txtBkT.insert(END, sb[11])

            self.txtAtr.delete(0, END)
            self.txtAtr.insert(END, sb[12])

            self.txtDbo.delete(0, END)
            self.txtDbo.insert(END, sb[13])

            self.txtDdu.delete(0, END)
            self.txtDdu.insert(END, sb[14])

            self.txtsPr.delete(0, END)
            self.txtsPr.insert(END, sb[15])

            self.txtLrf.delete(0, END)
            self.txtLrf.insert(END, sb[16])

            self.txtDod.delete(0, END)
            self.txtDod.insert(END, sb[17])

            self.txtDonL.delete(0, END)
            self.txtDonL.insert(END, sb[18])


        def deleteData():
            if(len(MTy.get())!=0):
                LibBksDatabase.deleteRec(sb[0])
                ClearData()
                DisplayData()


        def searchDatabase():
            Booklist.delete(0, END)
            for row in LibBksDatabase.searchData(MTy.get(), Ref.get(), Title.get(), Fna.get(), Sna.get(),Adr1.get(),
                                                 Adr2.get(), Pcd.get(), MNo.get(), BkID.get(), BkT.get(), Atr.get(),
                                                 DBo.get(), Ddu.get(),sPr.get(), Lrf.get(), Dod.get(), DonL.get()):
                Booklist.insert(END, row)

        def update():
            if (len(MTy.get()) != 0):
                LibBksDatabase.dataUpdate(sb[0], MTy.get(), Ref.get(), Title.get(), Fna.get(), Sna.get(),Adr1.get(),
                                                 Adr2.get(), Pcd.get(), MNo.get(), BkID.get(), BkT.get(), Atr.get(),
                                                 DBo.get(), Ddu.get(),sPr.get(), Lrf.get(), Dod.get(), DonL.get())










        #==================================================FRAMES======================================================#

        MainFrame = Frame(self.root)
        MainFrame.grid()

        Title_Frame = Frame(MainFrame, bd=2, padx=40, pady=8, bg='orange', relief=RIDGE)
        Title_Frame.pack(side=TOP)

        self.lblTitle = Label(Title_Frame, font=('arial', 46, 'bold'), text=" Library Management System ")
        self.lblTitle.grid(sticky=W)

        ButtonFrame = Frame(MainFrame, bd=2, width=1350, height=100, padx=20, pady=20, bg='orange', relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        FrameDetail = Frame(MainFrame, bd=0, width=1350, height=50, padx=20, relief=RIDGE)
        FrameDetail.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=800, height=300, padx=20, relief=RIDGE,
                                   font=('arial', 12, 'bold'), text=' Library Member Info ', bg='orange')
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=20, pady=3, relief=RIDGE,
                                    font=('arial', 12, 'bold'), text=' Book Details ', bg='orange')
        DataFrameRIGHT.pack(side=RIGHT)

        # ============================================LABEL and ENTRY==================================================#
#
        self.lblMemberType = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Member Type', padx=2, pady=2,
                                   bg='orange')
        self.lblMemberType.grid(row=0, column=0, sticky=W)

        self.txtMType = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MTy,width=25)
        self.txtMType.grid(row=0, column=1)
#
        self.lblBkID = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Book ID', padx=2, pady=2,
                             bg='orange')
        self.lblBkID.grid(row=0, column=2, sticky=W)

        self.txtBkID = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=BkID, width=25)
        self.txtBkID.grid(row=0, column=3)
#
        self.lblRef = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Reference No.', padx=2, pady=2,
                            bg='orange')
        self.lblRef.grid(row=1, column=0, sticky=W)

        self.txtRef = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ref, width=25)
        self.txtRef.grid(row=1, column=1)
#
        self.lblBkT = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Book Title', padx=2, pady=2,
                            bg='orange')
        self.lblBkT.grid(row=1, column=2, sticky=W)

        self.txtBkT = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=BkT, width=25)
        self.txtBkT.grid(row=1, column=3)
#
        self.lblTitle = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Title', padx=2, pady=2,
                              bg='Orange')
        self.lblTitle.grid(row=2, column=0, sticky=W)

        self.txtTitle = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Title, width=25)
        self.txtTitle.grid(row=2, column=1)
#
        self.lblAtr = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Author', padx=2, pady=2,
                            bg='Orange')
        self.lblAtr.grid(row=2, column=2, sticky=W)

        self.txtAtr = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Atr, width=25)
        self.txtAtr.grid(row=2, column=3)
#
        self.lblFna = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='FirstName', padx=2, pady=2,
                            bg='Orange')
        self.lblFna.grid(row=3, column=0, sticky=W)

        self.txtFna = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Fna, width=25)
        self.txtFna.grid(row=3, column=1)
#
        self.lblDBo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Date Borrowed', padx=2, pady=2,
                            bg='Orange')
        self.lblDBo.grid(row=3, column=2, sticky=W)

        self.txtDbo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DBo, width=25)
        self.txtDbo.grid(row=3, column=3)
#
        self.lblSna = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='SurName', padx=2, pady=2,
                            bg='Orange')
        self.lblSna.grid(row=4, column=0, sticky=W)

        self.txtSna = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Sna, width=25)
        self.txtSna.grid(row=4, column=1)
#
        self.lblDdu = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Due Date', padx=2, pady=2,
                            bg='Orange')
        self.lblDdu.grid(row=4, column=2, sticky=W)

        self.txtDdu = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Ddu, width=25)
        self.txtDdu.grid(row=4, column=3)
#
        self.lblAdr1 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address 1', padx=2, pady=2,
                             bg='Orange')
        self.lblAdr1.grid(row=5, column=0, sticky=W)

        self.txtAdr1 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr1, width=25)
        self.txtAdr1.grid(row=5, column=1)
#
        self.lblDonL = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Days On Loan', padx=2, pady=2,
                             bg='Orange')
        self.lblDonL.grid(row=5, column=2, sticky=W)

        self.txtDonL = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=DonL, width=25)
        self.txtDonL.grid(row=5, column=3)
#
        self.lblAdr2 = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Address 2', padx=2, pady=2,
                             bg='Orange')
        self.lblAdr2.grid(row=6, column=0, sticky=W)

        self.txtAdr2 = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Adr2, width=25)
        self.txtAdr2.grid(row=6, column=1)
#
        self.lblLrf = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Late Return Fine', padx=2, pady=2,
                            bg='Orange')
        self.lblLrf.grid(row=6, column=2, sticky=W)

        self.txtLrf = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Lrf, width=25)
        self.txtLrf.grid(row=6, column=3)
#
        self.lblPcd = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Post Code', padx=2, pady=2,
                            bg='Orange')
        self.lblPcd.grid(row=7, column=0, sticky=W)

        self.txtPcd = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Pcd, width=25)
        self.txtPcd.grid(row=7, column=1)
#
        self.lblDod = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Date Over Due', padx=2, pady=2,
                            bg='Orange')
        self.lblDod.grid(row=7, column=2, sticky=W)

        self.txtDod = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=Dod, width=25)
        self.txtDod.grid(row=7, column=3)
#
        self.lblMNo = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Mobile Number', padx=2, pady=2,
                            bg='Orange')
        self.lblMNo.grid(row=8, column=0, sticky=W)

        self.txtMNo = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=MNo, width=25)
        self.txtMNo.grid(row=8, column=1)
#
        self.lblsPr = Label(DataFrameLEFT, font=('arial', 12, 'bold'), text='Selling Price', padx=2, pady=2,
                            bg='Orange')
        self.lblsPr.grid(row=8, column=2, sticky=W)

        self.txtsPr = Entry(DataFrameLEFT, font=('arial', 12, 'bold'), textvariable=sPr, width=25)
        self.txtsPr.grid(row=8, column=3)

        # ============================================LISTBOX and SCROLLBAR============================================#

        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky=NS)

        Booklist = Listbox(DataFrameRIGHT, width=45, height=12, font=('arial', 12, 'bold'), yscrollcommand=scrollbar.set)
        Booklist.bind('<<ListboxSelect>>', SelectedBook)
        Booklist.grid(row=0, column=0, padx=8)

        scrollbar.configure(command=Booklist.yview)

        # ============================================BUTTONS WIDGETS==================================================#

        self.btnAddData = Button(ButtonFrame, text='Add Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=addData)
        self.btnAddData.grid(row=0,column=0)

        self.btnDisData = Button(ButtonFrame, text='Display Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=DisplayData)
        self.btnDisData.grid(row=0, column=1)

        self.btnClrData = Button(ButtonFrame, text='Clear Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=ClearData)
        self.btnClrData.grid(row=0, column=2)

        self.btnDelData = Button(ButtonFrame, text='Delete Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=deleteData)
        self.btnDelData.grid(row=0, column=3)

        self.btnUpdData = Button(ButtonFrame, text='Update Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=update)
        self.btnUpdData.grid(row=0, column=4)

        self.btnSrhData = Button(ButtonFrame, text='Search Data', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                                 command=searchDatabase)
        self.btnSrhData.grid(row=0, column=5)

        self.btnExit = Button(ButtonFrame, text='Exit', font=('arial', 14, 'bold'), height=2, width=13, bd=4,
                              command=iExit)
        self.btnExit.grid(row=0, column=6)


if __name__ == '__main__':
    root = Tk()
    application = Library(root)
    root.mainloop()
