from tkinter import * 
win = Tk() 
win.geometry("787x600")
playername = StringVar()
def SubmitName():
    
    playername.get
    #messagebox.showinfo("Success", playername)
    print(playername)
    
frame3 = Frame(win) 
frame3.pack()
label1 = Label(frame3, text="You awaken in a room, with no memories of yourself or your past. ")
label2 = Label(frame3, text="First, how about you give yourself a name:")
label1.config(font=("Courier", 11)) 
label2.config(font=("Courier", 11))
entry1 = Entry(frame3, textvariable=playername) 
entry1.config(font=("Courier", 11))
label1.grid(row=0, column=0, columnspan=3) 
label2.grid(row=1, column=0)
entry1.grid(row=1, column=1)
bnamesub= Button(frame3, text="Submit", command=lambda: SubmitName()) 
bnamesub.grid()
win.mainloop()
