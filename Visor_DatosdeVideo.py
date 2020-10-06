import ffmpeg
from tkinter import *
from tkinter import filedialog

class Visor:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.configure(bg="gray68")
        self.ventana.geometry("800x540")
        self.ventana.title("VISOR DATOS DE VIDEO")
        self.nomArch = StringVar()
        self.videoNameEntry = Entry(self.ventana,width=45,font=('Arial',15),textvariable=self.nomArch)
        self.videoNameEntry.place(x=10,y=10)
        self.btnBuscar = Button(self.ventana,text='BUSCAR',width=34,command=self.abrir_archivo)
        self.btnBuscar.place(x=540,y=12)
        self.labelRate = Label(self.ventana,text="avg frame rate:",bg="gray68",font=("Arial",15,"bold"))
        self.labelRate.place(x=10,y=100)

        self.ventana.mainloop()

    def abrir_archivo(self):
        self.archivo = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                        filetypes=(("mp4 files","*.mp4"),("all files","*.*")))
        if self.archivo != "":
            self.nombreArchivo = (self.archivo).split("/")[-1]
            self.nomArch.set(self.nombreArchivo) 
        

if __name__=="__main__":
    Visor()
