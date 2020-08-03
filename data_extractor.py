#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.scrolledtext as scrolledtext
from tkinter import filedialog
from PIL import Image
from PIL.ExifTags import TAGS

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("DATA EXTRACTOR")
        #self.ventana.geometry("630x200")

        self.display = scrolledtext.ScrolledText(self.ventana,bg="black",fg="green",width=65,height=20)
        self.display.pack(side=TOP)
        self.btn_search = Button(self.ventana,text="SEARCH FILE",bg="orange",width=30,command=self.open_file)
        self.btn_search.pack(side=TOP)
        
        self.ventana.mainloop()

    def open_file(self):
        file = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                                        filetypes=(("jpg files","*.jpg"),("png files","*.jpg")))
        if file is not None:
            self.extract_data(file)

    def extract_data(self,f):
        self.display.delete('1.0',END)
        image = Image.open(f)
        exifdata = image._getexif()

        if exifdata is not None:
            for tag_id in exifdata:
                tag = TAGS.get(tag_id, tag_id)
                data = exifdata.get(tag_id)
                if isinstance(data, bytes):
                    data = data.decode('UTF8','replace')
                self.display.insert(END,'{} {}'.format(tag,data)+"\n")
        else:
            self.display.insert(END,'NO DATA')

    
if __name__=="__main__":
    App()

