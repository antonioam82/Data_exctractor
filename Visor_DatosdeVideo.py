import ffmpeg
from tkinter import *

class Visor:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.configure(bg="gray68")
        self.ventana.geometry("800x540")
        self.ventana.title("VISOR DATOS DE VIDEO")
        self.videoNameEntry = Entry(self.ventana,width=45,font=('Arial',15))
        self.videoNameEntry.place(x=10,y=10)
        self.btnBuscar = Button(self.ventana,text='BUSCAR',width=34)
        self.btnBuscar.place(x=540,y=12)

        self.ventana.mainloop()
        

if __name__=="__main__":
    Visor()
