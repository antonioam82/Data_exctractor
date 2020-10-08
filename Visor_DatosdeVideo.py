import ffmpeg
from tkinter import *
from tkinter import filedialog, messagebox

class Visor:
    def __init__(self):

        
        self.ventana = Tk()
        
        self.rateValue = StringVar()
        self.rateBit = StringVar()
        self.chromaValue = StringVar()
        self.codecValue = StringVar()
        self.codecTag = StringVar()
        self.codecTstr = StringVar()
        self.codecTbase = StringVar()
        self.codecType = StringVar()
        self.codedHeight = StringVar()
        self.codecWidth = StringVar()
        #codec_width
        #display_aspect_ratio
        #divx_packed
        #duration
        #duration_ts
        
        

        color_ventana = "khaki"
        self.ventana.configure(bg=color_ventana)
        self.ventana.geometry("800x540")
        self.ventana.title("VISOR DATOS DE VIDEO")
        self.nomArch = StringVar()
        self.videoNameEntry = Entry(self.ventana,width=45,font=('Arial',15),textvariable=self.nomArch)
        self.videoNameEntry.place(x=10,y=10)
        self.btnBuscar = Button(self.ventana,text='BUSCAR',width=34,command=self.abrir_archivo)
        self.btnBuscar.place(x=540,y=12)
        
        self.labelRate = Label(self.ventana,text="avg frame rate:",bg=color_ventana,font=("Arial",15))
        self.labelRate.place(x=10,y=100)
        self.entryRate = Entry(self.ventana,textvariable=self.rateValue)
        self.entryRate.place(x=166,y=106)
        self.labelBitr = Label(self.ventana,text="bit rate:",bg=color_ventana,font=("Arial",15))
        self.labelBitr.place(x=79,y=130)
        self.entryBitr = Entry(self.ventana,textvariable=self.rateBit)
        self.entryBitr.place(x=166,y=135)
        self.labelChroma = Label(self.ventana,text="chroma location:",bg=color_ventana,font=("Arial",15))
        self.labelChroma.place(x=3,y=160)
        self.entryChroma = Entry(self.ventana,textvariable=self.chromaValue)
        self.entryChroma.place(x=166,y=165)
        self.labelCodec = Label(self.ventana,text="codec name:",bg=color_ventana,font=("Arial",15))
        self.labelCodec.place(x=34,y=190)
        self.entryCodec = Entry(self.ventana,textvariable=self.codecValue)
        self.entryCodec.place(x=166,y=195)
        self.labelCtag = Label(self.ventana,text="codec tag:",bg=color_ventana,font=("Arial",15))
        self.labelCtag.place(x=54,y=220)
        self.entryCtag = Entry(self.ventana,textvariable=self.codecTag)
        self.entryCtag.place(x=166,y=225)
        self.labelcodecTstr = Label(self.ventana,text="codec tag string:",bg=color_ventana,font=("Arial",15))
        self.labelcodecTstr.place(x=0,y=250)
        self.entrycodecTstr = Entry(self.ventana,textvariable=self.codecTstr)
        self.entrycodecTstr.place(x=166,y=255)
        self.labelcodecTbase = Label(self.ventana,text="codec time base:",bg=color_ventana,font=("Arial",15))
        self.labelcodecTbase.place(x=0,y=280)
        self.entrycodecTbase = Entry(self.ventana,textvariable=self.codecTbase)
        self.entrycodecTbase.place(x=166,y=285)
        self.labelcodecType = Label(self.ventana,text="codec type:",bg=color_ventana,font=("Arial",15))
        self.labelcodecType.place(x=48,y=310)
        self.entrycodecType = Entry(self.ventana,textvariable=self.codecType)
        self.entrycodecType.place(x=166,y=315)
        self.labelcodedHeight = Label(self.ventana,text="coded height:",bg=color_ventana,font=("Arial",15))
        self.labelcodedHeight.place(x=34,y=340)
        self.entrycodedHeight = Entry(self.ventana,textvariable=self.codedHeight)
        self.entrycodedHeight.place(x=166,y=345)
        
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
            self.chromaValue.set(video_streams[0]['chroma_location'])
            self.codecValue.set(video_streams[0]['codec_name'])
            self.codecTag.set(video_streams[0]['codec_tag'])
            self.codecTstr.set(video_streams[0]['codec_tag_string'])
            self.codecTbase.set(video_streams[0]['codec_time_base'])
            self.codecType.set(video_streams[0]['codec_type'])
            self.codedHeight.set(video_streams[0]['coded_height'])
        except:
            messagebox.showwarning("ERROR","No se pudo extraer la información.")

    
        

if __name__=="__main__":
    Visor()
