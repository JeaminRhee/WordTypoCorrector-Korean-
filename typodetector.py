from tkinter import *
from tkinter import messagebox
import main_

# Make sure to have only one docx extension in your current directory
# We are automatically find one docx file and correct it.
prohibited_ = ["\\", '/', '|', '*', '<', '>', '?', ':', '"']


def clicked(args, args2): #args = radiobutton(docx or txt) / args2 = save file name
    if len(args2)==0:
        messagebox.showerror("Error", "Save File Name is Empty")

    elif any(pro_character in args2 for pro_character in prohibited_):
        messagebox.showerror("Error", "File Name Can't Contain Special Characters"
                                      "\nex) /, |, *, ?, \", :, <, >, \\, ")

    elif args==1: # radiobutton docx is clicked
        MsgBox = messagebox.askquestion("Information", "Are you sure you want to correct docx file?")
        if MsgBox == 'yes':
            typo_dict = main_.typolistread()
            misspelled_dict = main_.docx_process(args2, typo_dict)
            messagebox.showinfo('Information', 'Corrected Docx File created!')
            MsgBox = messagebox.askquestion("Information", "Want to check what you misspelled?")
            if MsgBox=='yes':
                main_.show_typos(misspelled_dict)
            else:
                root.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')

    elif args==2: # radiobutton txt is clicked
        MsgBox = messagebox.askquestion("Information", "Are you sure you want to correct txt file?")
        if MsgBox == 'yes':
            typo_dict = main_.typolistread()
            misspelled_dict = main_.txt_process(args2,typo_dict)
            messagebox.showinfo('Information', 'Corrected TXT File created!')
            MsgBox = messagebox.askquestion("Information", "Want to check what you misspelled?")
            if MsgBox == 'yes':
                main_.show_typos(misspelled_dict)
            else:
                root.destroy()
        else:
            messagebox.showinfo('Return', 'You will now return to the application screen')


root = Tk()
root.geometry('270x210')
root.title("Typo Detector")
theLabel = Label(root, text="What file\nyou wanna check?", font=("Arial Bold", 12)).place(x=50, y=5)
lil_explain = Label(root, text="Make sure to have only one file per extension\nin the directory.\nAnd it corrects only text typos.", font = ("Times 32", 9)).place(x=5, y=50)
selected = IntVar()
selected.set(1)
rad1 = Radiobutton(root, text="docx",value = 1, variable = selected)
rad2 = Radiobutton(root, text="txt", value = 2, variable = selected)
rad1.place(x= 25, y= 110)
rad2.place(x= 150, y= 110)

content = StringVar()
Label(root, text="Save File Name: ",font=("Arial Bold", 9)).place(x=2,y=138)
e1 = Entry(root, text="ex)output", textvariable = content)
e1.insert(END, 'ex)output')
e1.place(x=101, y=138)

frame = Frame(root)
frame.place(x=100, y=168)
button1 = Button(frame, text="OK", width=6, command=lambda:clicked(selected.get(), content.get()))
button1.grid()

root.mainloop()
