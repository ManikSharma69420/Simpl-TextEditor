from tkinter import *
from tkinter import filedialog
from tkinter import messagebox 
import tkinter.font as tkFont

global isXclicked

isXclicked = False

global filename

global isfileopened

isfileopened = False

global isfilesaved

isfilesaved = False 

def quitusingcancelbutton():
    global isXclicked
    isXclicked=False

def checkforsave():
    global isXclicked, isfilesaved
    if maintextentry.get("1.0", "end-1c").strip() == "":
        gui.destroy()
    elif isfilesaved == False and isXclicked == False:
        isXclicked = True;value = "";saveui=Tk();saveui.title("Do you want to save?");label1 = Label(saveui,text="Do you want to save the file?");label1.pack();b1 = Button(saveui,text="Save",command=savefile);b1.pack();b2 = Button(saveui,text="Don't Save",command=lambda: [gui.destroy(), saveui.destroy()]);b2.pack();b3 = Button(saveui,text="Cancel",command=lambda: [quitusingcancelbutton(), saveui.destroy()]);b3.pack()

gui = Tk()

gui.title("Simpl TextEditor ⱽ¹.⁰")

gui.protocol('WM_DELETE_WINDOW', checkforsave)

gui.geometry("640x480")

gui.resizable(0,0)

txt_font = tkFont.Font(family="Cascadia Code", size=10)

def about():
    aboutui = Tk()
    aboutui.title("About Simple TextEditor ⱽ¹.⁰")
    l1 = Label(aboutui, text="Made by Manik Sharma (Github - ManikSharma69420) \n Enjoy the editor! \n New stuff like fonts coming soon!")
    l1.pack()

credit_button = Button(gui, text="Simpl TextEditor ⱽ¹.⁰", font=txt_font, bg="#f5f5f5", bd=0, highlightthickness=0, command=about)
credit_button.place(x=400, y=445)

#main text entry box
maintextentry = Text(gui, width=77, height=25, font=txt_font)
maintextentry.place(x=10,y=10)

#func to get the text
def gettext():
    maintext = maintextentry.get("1.0",'end-1c')
    
#filebrowser func 
def browsefiles():
    global isfilesaved
    global filename
    global isfileopened
    maintextentry.delete("1.0", 'end-1c')
    filename = filedialog.askopenfilename(initialdir="/", title="Select a File", filetypes=(("Text files", "*.txt*"), ("All files", "*.*")))

    # Check if a file was selected
    if filename:
        with open(filename, 'r') as txtfile:
            openedtxtfile = txtfile.read()
            maintextentry.insert('1.0', openedtxtfile)  # Insert text starting from the top
            isfilesaved = True
            isfileopened = True
    else:
        # Reset save and open status if no file is selected
        isfilesaved = False
        isfileopened = False


def isfile():
    isfileopened = False;

def checkfiles():
    if maintextentry.get("1.0", "end-1c").strip() == "" or isfilesaved:
        browsefiles()
    else:
        saveui = Tk()
        saveui.title("Remember to Save your files before opening a new one!")
        label1 = Label(saveui, text="Do you want to save the current file before opening a new one?")
        label1.pack()
        b1 = Button(saveui, text="Save", command=lambda: [savefile(), saveui.destroy(), browsefiles()])
        b1.pack()
        b2 = Button(saveui, text="Don't Save", command=lambda: [saveui.destroy(), browsefiles()])
        b2.pack()
        b3 = Button(saveui, text="Cancel", command=saveui.destroy)
        b3.pack()

def savefile():
    global isfilesaved
    global filename
    global isfileopened
    if isfileopened == False:
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if filename:
            with open(filename, 'w') as file:
                textcontent = maintextentry.get("1.0", "end-1c")
                file.write(textcontent)
                isfileopened = True
                isfilesaved = True
    elif isfileopened == True:
        with open(filename, 'w') as file:
                textcontent = maintextentry.get("1.0", "end-1c")
                file.write(textcontent)
    isfilesaved=True
#prints text to console
#printtexttoconsolebutton = Button(gui, text="Print text to console", command=gettext)
#printtexttoconsolebutton.place(x=0, y=420)
#commented our cause its useless lol ^^^

#button to open filebrowser
openfilebrowser = Button(gui, text="Open a text file", command=checkfiles, font=txt_font)
openfilebrowser.place(x=10, y=445)

#button to save txt file
savetextfile = Button(gui, text="Save your text file", command=savefile, font=txt_font)
savetextfile.place(x=150, y=445)

gui.mainloop()