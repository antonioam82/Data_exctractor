from tkinter import *
import tkinter.scrolledtext as scrolledtext
from PIL import Image
from PIL.ExifTags import TAGS

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("DATA EXTRACTOR")
        #self.ventana.geometry("630x200")

        self.display = scrolledtext.ScrolledText(self.ventana,bg="black",width=65,height=20)
        self.display.pack(side=TOP)
        self.btn_search = Button(self.ventana,text="SEARCH FILE",bg="orange",width=30)
        self.btn_search.pack(side=TOP)
        
        self.ventana.mainloop()

if __name__=="__main__":
    App()

