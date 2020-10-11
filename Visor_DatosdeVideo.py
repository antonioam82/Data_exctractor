  
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
        self.disaspRatio = StringVar()
        self.divxPacked = StringVar()
        self.duration =StringVar()
        self.durationTs = StringVar()
        self.hasbFrames = StringVar()

                #'has_b_frames': 0,
       # 'height': 360,
         #'index': 0,
         #'is_avc': 'true',
          #'level': 30,
          #'nal_length_size': '4',
          #'nb_frames': '61',
          #'pix_fmt': 'yuv420p',
        
        

        color_ventana = "khaki"
        self.ventana.configure(bg=color_ventana)
        self.ventana.geometry("800x540")
        self.ventana.title("VISOR DATOS DE VIDEO")
        self.nomArch = StringVar()
        self.videoNameEntry = Entry(self.ventana,width=45,font=('Arial',15),textvariable=self.nomArch)
        self.videoNameEntry.place(x=10,y=10)
        self.btnBuscar = Button(self.ventana,text='BUSCAR',width=34,command=self.abrir_archivo)
        self.btnBuscar.place(x=540,y=12)
        
        self.labelRate = Label(self.ventana,text="avg frame rate:",bg=color_ventana,font=("Arial",13))
        self.labelRate.place(x=43,y=103)
        self.entryRate = Entry(self.ventana,textvariable=self.rateValue)
        self.entryRate.place(x=166,y=106)
        self.labelBitr = Label(self.ventana,text="bit rate:",bg=color_ventana,font=("Arial",13))
        self.labelBitr.place(x=97,y=133)
        self.entryBitr = Entry(self.ventana,textvariable=self.rateBit)
        self.entryBitr.place(x=166,y=135)
        self.labelChroma = Label(self.ventana,text="chroma location:",bg=color_ventana,font=("Arial",13))
        self.labelChroma.place(x=30,y=163)
        self.entryChroma = Entry(self.ventana,textvariable=self.chromaValue)
        self.entryChroma.place(x=166,y=165)
        self.labelCodec = Label(self.ventana,text="codec name:",bg=color_ventana,font=("Arial",13))
        self.labelCodec.place(x=55,y=193)
        self.entryCodec = Entry(self.ventana,textvariable=self.codecValue)
        self.entryCodec.place(x=166,y=195)
        self.labelCtag = Label(self.ventana,text="codec tag:",bg=color_ventana,font=("Arial",13))
        self.labelCtag.place(x=73,y=223)
        self.entryCtag = Entry(self.ventana,textvariable=self.codecTag)
        self.entryCtag.place(x=166,y=225)
        self.labelcodecTstr = Label(self.ventana,text="codec tag string:",bg=color_ventana,font=("Arial",13))
        self.labelcodecTstr.place(x=28,y=253)
        self.entrycodecTstr = Entry(self.ventana,textvariable=self.codecTstr)
        self.entrycodecTstr.place(x=166,y=255)
        self.labelcodecTbase = Label(self.ventana,text="codec time base:",bg=color_ventana,font=("Arial",13))
        self.labelcodecTbase.place(x=25,y=283)
        self.entrycodecTbase = Entry(self.ventana,textvariable=self.codecTbase)
        self.entrycodecTbase.place(x=166,y=285)
        self.labelcodecType = Label(self.ventana,text="codec type:",bg=color_ventana,font=("Arial",13))
        self.labelcodecType.place(x=64,y=313)
        self.entrycodecType = Entry(self.ventana,textvariable=self.codecType)
        self.entrycodecType.place(x=166,y=315)
        self.labelcodedHeight = Label(self.ventana,text="coded height:",bg=color_ventana,font=("Arial",13))
        self.labelcodedHeight.place(x=52,y=343)
        self.entrycodedHeight = Entry(self.ventana,textvariable=self.codedHeight)
        self.entrycodedHeight.place(x=166,y=345)
        self.labeldisaspRatio = Label(self.ventana,text="display aspect ratio:",bg=color_ventana,font=("Arial",13))
        self.labeldisaspRatio.place(x=5,y=373)
        self.entrydisaspRatio = Entry(self.ventana,textvariable=self.disaspRatio)
        self.entrydisaspRatio.place(x=166,y=375)
        self.labeldivxPacked = Label(self.ventana,text="divx packed:",bg=color_ventana,font=("Arial",13))
        self.labeldivxPacked.place(x=62,y=403)#88
        self.entrydivxPacked = Entry(self.ventana,textvariable=self.divxPacked)
        self.entrydivxPacked.place(x=166,y=405)
        self.labelDuration = Label(self.ventana,text="duration:",bg=color_ventana,font=("Arial",13))
        self.labelDuration.place(x=88,y=433)
        self.entryDuration = Entry(self.ventana,textvariable=self.duration)
        self.entryDuration.place(x=166,y=435)
        self.labeldurationTs = Label(self.ventana,text="duration ts:",bg=color_ventana,font=("Arial",13))
        self.labeldurationTs.place(x=70,y=463)
        self.entrydurationTs = Entry(self.ventana,textvariable=self.durationTs)
        self.entrydurationTs.place(x=166,y=465)
        self.labelhasbFrames = Label(self.ventana,text="has b frames:",bg=color_ventana,font=("Arial",13))
        self.labelhasbFrames.place(x=360,y=103)
        self.entryhasbFrames = Entry(self.ventana,textvariable=self.hasbFrames)
        self.entryhasbFrames.place(x=473,y=106)
        
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
            self.video_streams = [stream for stream in
            probe["streams"] if stream["codec_type"] == "video"]
            self.video_streams = [stream for stream in probe["streams"] if stream["codec_type"] == "video"]
            #self.rateValue.set(video_streams[0]['avg_frame_rate'])
            self.rateValue.set(self.null_finder('avg_frame_rate'))
            self.rateBit.set(self.null_finder('bit_rate'))
            self.chromaValue.set(self.null_finder('chroma_location'))
            self.codecValue.set(self.null_finder('codec_name'))
            self.codecTag.set(self.null_finder('codec_tag'))
            self.codecTstr.set(self.null_finder('codec_tag_string'))
            self.codecTbase.set(self.null_finder('codec_time_base'))
            self.codecType.set(self.null_finder('codec_type'))
            self.codedHeight.set(self.null_finder('coded_height'))
            self.disaspRatio.set(self.null_finder('display_aspect_ratio'))
            self.divxPacked.set(self.null_finder('divx_packed'))
            self.duration.set(self.null_finder('duration'))
            self.durationTs.set(self.null_finder('duration_ts'))
            self.hasbFrames.set(self.null_finder('has_b_frames'))

            #self.divxPacked.set(video_streams[0]['divx_packed'])
        except Exception as e:
            print(str(e))
            messagebox.showwarning("ERROR","No se pudo extraer la información.")

    def null_finder(self,campo):
        try:
            value = self.video_streams[0][campo]
            return value
        except:
            return "No info available"
            
            

if __name__=="__main__":
    Visor()
