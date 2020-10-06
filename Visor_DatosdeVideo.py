import ffmpeg
from tkinter import *
from tkinter import filedialog, messagebox

class Visor:
    def __init__(self):

        
        self.ventana = Tk()
        
        self.rateValue = StringVar()
        self.rateBit = StringVar()
        
        self.ventana.configure(bg="gray68")
        self.ventana.geometry("800x540")
        self.ventana.title("VISOR DATOS DE VIDEO")
        self.nomArch = StringVar()
        self.videoNameEntry = Entry(self.ventana,width=45,font=('Arial',15),textvariable=self.nomArch)
        self.videoNameEntry.place(x=10,y=10)
        self.btnBuscar = Button(self.ventana,text='BUSCAR',width=34,command=self.abrir_archivo)
        self.btnBuscar.place(x=540,y=12)
        
        self.labelRate = Label(self.ventana,text="avg frame rate:",bg="gray68",font=("Arial",15))
        self.labelRate.place(x=10,y=100)
        self.entryRate = Entry(self.ventana,textvariable=self.rateValue)
        self.entryRate.place(x=166,y=106)
        self.labelBitr = Label(self.ventana,text="bit rate:",bg="gray68",font=("Arial",15))
        self.labelBitr.place(x=79,y=130)
        self.entryBitr = Entry(self.ventana,textvariable=self.rateBit)
        self.entryBitr.place(x=166,y=135)
        

        self.ventana.mainloop()

    def abrir_archivo(self):
        self.archivo = filedialog.askopenfilename(initialdir="/",title="SELECT FILE",
                        filetypes=(("mp4 files","*.mp4"),("all files","*.*")))
        if self.archivo != "":
            self.nombreArchivo = (self.archivo).split("/")[-1]
            self.nomArch.set(self.nombreArchivo)
            self.videoInfo()

    def videoInfo(self):
        try:
            probe = ffmpeg.probe(self.archivo)
            video_streams = [stream for stream in
            probe["streams"] if stream["codec_type"] == "video"]
            video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
        
            self.rateValue.set(video_streams[0]['avg_frame_rate'])
            self.rateBit.set(video_streams[0]['bit_rate'])
        except:
            messagebox.showwarning("ERROR","No se pudo extraer la información.")
        

if __name__=="__main__":
    Visor()
