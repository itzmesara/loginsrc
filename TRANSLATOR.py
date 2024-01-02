from tkinter import *
from googletrans import Translator
root=Tk()
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()

x = screenwidth
y = screenheight
root.geometry("640x720")

def trans(text,target_language="hi"):
    translator=Translator()
    translated_text=translator.translate(text,dest=target_language)
    return translated_text.text
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    tran = trans(inp, target_language='en')
    lbl.config(text=tran)

inputtxt = Text(root,height=5,width=20)
inputtxt.pack()
# Button Creation
printButton = Button(root,text="Print",command=printInput)
printButton.pack()
diut=Button(root, text="Quit", command=root.destroy)
diut.pack()
lbl = Label(root, text = "")
lbl.pack()
root.mainloop()