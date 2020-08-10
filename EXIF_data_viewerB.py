#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import re
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS
import warnings
import piexif

warnings.filterwarnings("ignore", "(Possibly )?corrupt EXIF data", UserWarning)

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("EXIF DATA VIEWER")
        self.ventana.configure(bg="gray68")
        self.ventana.geometry("565x379")
        self.file = ""
        self.file_label = Label(self.ventana,text="NO FILE SELECTED",bg="gray70",fg="white")
        self.file_label.pack(side=TOP)
        self.display = scrolledtext.ScrolledText(self.ventana,bg="black",fg="light green",width=65,height=20)
        self.display.pack(side=TOP)
        self.btn_search = Button(self.ventana,text="SEARCH FILE",bg="light blue",width=30,command=self.open_file)
        self.btn_search.place(x=12,y=348)
        self.btn_delete = Button(self.ventana,text="DELETE EXIF DATA",bg="light blue",width=30,command=self.remove)
        self.btn_delete.place(x=335,y=348)
        
        self.ventana.mainloop()

    def open_file(self):
        self.file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                                        filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
        if self.file != "":
            self.file_label.configure(text=(self.file).split("/")[-1])
            self.extract_data(self.file)

    def extract_data(self,f):
        self.display.delete('1.0',END)
        try:
            image = Image.open(f)
            exifdata = image._getexif()
            if exifdata is not None:
                self.display.insert(END,"-"*26+"METADATA INFO"+"-"*26+"\n")
                for tag_id in exifdata:
                    tag = TAGS.get(tag_id, tag_id)
                    data = exifdata.get(tag_id)
                    if isinstance(data, bytes):
                        data = data.decode('UTF8','replace')
                    try:
                        self.display.insert(END,f"{tag:26}: {data}"+"\n")
                    except:
                        data = re.sub('[^a-zA-Z0-9 \n\.]', '', data)
                        self.display.insert(END,f"{tag:26}: {data}"+"\n")
                self.display.insert(END,"-"*65)
            else:
                self.display.insert(END,'NO DATA.')
        except:
            self.display.insert(END,'ERROR.')

    def remove(self):
        if self.file != "":
            piexif.remove(self.file)
            self.extract_data(self.file)

    
if __name__=="__main__":
    App()
