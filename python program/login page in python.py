from tkinter import *
root = Tk()
root.geometry("500*300")

lebel (root,text="my ragistration form",font="ar15bold").grid(row=0,column=3)


name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency")


name.grid(row=1, column=2)
phone. grid(row=2, column=2)
gender. grid(row=3, column=2)
emergency. grid(row=4, column=2)


namevalue = StringVar
phonevalue = StringVar
gendervalue = StringVar
emergencyvalue = StringVar
chekvalue = IntVar

nameentry = Entry(root, textvariable =namevalue)
phoneentry = Entry(root, textvariable =phonevalue)
genderentry = Entry(root, textvariable =gendervalue)
emergencyentry = Entry(root, textvariable =emergencyvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
root.mainloop()

