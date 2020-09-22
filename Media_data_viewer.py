import ffmpeg
import pprint
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog

class Visualizer:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("MEDIA DATA VIEWER")
        self.ventana.configure(bg="gray68")
        self.ventana.geometry("600x420")
        self.file_label = Label(self.ventana,text="NO FILE SELECTED",bg="gray50",fg="white")
        self.file_label.pack(side=TOP)
        self.display = scrolledtext.ScrolledText(self.ventana,bg="blue",fg="white",width=67,height=23)
        self.display.pack(side=TOP)
        self.btn_search = Button(self.ventana,text="SEARCH FILE",bg="light blue",width=30)
        self.btn_search.pack(side=TOP)       

        self.ventana.mainloop()

if __name__=="__main__":
    Visualizer()
