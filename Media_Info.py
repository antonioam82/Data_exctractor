import ffmpeg
from tkinter import *
from tkinter import filedialog, messagebox

class Visor:
    def __init__(self):

        
        self.ventana = Tk()
        self.codecLong = StringVar()
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
        self.height = StringVar()
        self.index = StringVar()
        self.isAvc = StringVar()
        self.level = StringVar()
        self.nalLensiz = StringVar()
        self.nbFrames = StringVar()
        self.pixFmt = StringVar()
        self.rframeRate = StringVar()
        self.refs = StringVar()
        self.startPts = StringVar()
        self.startTime = StringVar()
        self.timeBase = StringVar()
        self.width = StringVar()
        #self.tags = StringVar()
        self.profile = StringVar()

        #profile
        #tags
        #disposition
        #codec_long_name
        
        

        color_ventana = "gray80"
        self.ventana.configure(bg=color_ventana)
        self.ventana.geometry("920x540")
        self.ventana.title("MEDIA FILE INFO")
        self.nomArch = StringVar()
        Entry(self.ventana,width=55,font=('Arial',15),textvariable=self.nomArch).place(x=10,y=10)
        Button(self.ventana,text='BUSCAR',width=34,command=self.abrir_archivo).place(x=653,y=12)

        Label(self.ventana,text="codec long name:",bg=color_ventana,font=("Arial",13)).place(x=21,y=60)
        Entry(self.ventana,textvariable=self.codecLong,width=48).place(x=166,y=63)
        Label(self.ventana,text="avg frame rate:",bg=color_ventana,font=("Arial",13)).place(x=43,y=103)
        Entry(self.ventana,textvariable=self.rateValue).place(x=166,y=106)
        Label(self.ventana,text="bit rate:",bg=color_ventana,font=("Arial",13)).place(x=97,y=133)
        Entry(self.ventana,textvariable=self.rateBit).place(x=166,y=135)
        Label(self.ventana,text="chroma location:",bg=color_ventana,font=("Arial",13)).place(x=30,y=163)
        Entry(self.ventana,textvariable=self.chromaValue).place(x=166,y=165)
        Label(self.ventana,text="codec name:",bg=color_ventana,font=("Arial",13)).place(x=55,y=193)
        Entry(self.ventana,textvariable=self.codecValue).place(x=166,y=195)
        Label(self.ventana,text="codec tag:",bg=color_ventana,font=("Arial",13)).place(x=73,y=223)
        Entry(self.ventana,textvariable=self.codecTag).place(x=166,y=225)
        Label(self.ventana,text="codec tag string:",bg=color_ventana,font=("Arial",13)).place(x=28,y=253)
        Entry(self.ventana,textvariable=self.codecTstr).place(x=166,y=255)
        Label(self.ventana,text="codec time base:",bg=color_ventana,font=("Arial",13)).place(x=25,y=283)
        Entry(self.ventana,textvariable=self.codecTbase).place(x=166,y=285)
        Label(self.ventana,text="codec type:",bg=color_ventana,font=("Arial",13)).place(x=64,y=313)
        Entry(self.ventana,textvariable=self.codecType).place(x=166,y=315)
        Label(self.ventana,text="coded height:",bg=color_ventana,font=("Arial",13)).place(x=52,y=343)
        Entry(self.ventana,textvariable=self.codedHeight).place(x=166,y=345)
        Label(self.ventana,text="display aspect ratio:",bg=color_ventana,font=("Arial",13)).place(x=5,y=373)
        Entry(self.ventana,textvariable=self.disaspRatio).place(x=166,y=375)
        Label(self.ventana,text="divx packed:",bg=color_ventana,font=("Arial",13)).place(x=62,y=403)#88
        Entry(self.ventana,textvariable=self.divxPacked).place(x=166,y=405)
        Label(self.ventana,text="duration:",bg=color_ventana,font=("Arial",13)).place(x=88,y=433)
        Entry(self.ventana,textvariable=self.duration).place(x=166,y=435)
        Label(self.ventana,text="duration ts:",bg=color_ventana,font=("Arial",13)).place(x=70,y=463)
        Entry(self.ventana,textvariable=self.durationTs).place(x=166,y=465)
        Label(self.ventana,text="profile:",bg=color_ventana,font=("Arial",13)).place(x=65,y=493)
        Entry(self.ventana,textvariable=self.profile,width=27).place(x=125,y=495)
        Label(self.ventana,text="has b frames:",bg=color_ventana,font=("Arial",13)).place(x=360,y=103)
        Entry(self.ventana,textvariable=self.hasbFrames).place(x=473,y=106)
        Label(self.ventana,text="height:",bg=color_ventana,font=("Arial",13)).place(x=412,y=133)
        Entry(self.ventana,textvariable=self.height).place(x=473,y=136)
        Label(self.ventana,text="index:",bg=color_ventana,font=("Arial",13)).place(x=418,y=163)
        Entry(self.ventana,textvariable=self.index).place(x=473,y=166)
        Label(self.ventana,text="is avc:",bg=color_ventana,font=("Arial",13)).place(x=414,y=193)
        Entry(self.ventana,textvariable=self.isAvc).place(x=473,y=196)
        Label(self.ventana,text="level:",bg=color_ventana,font=("Arial",13)).place(x=425,y=223)
        Entry(self.ventana,textvariable=self.level).place(x=473,y=226)
        Label(self.ventana,text="nal length size:",bg=color_ventana,font=("Arial",13)).place(x=353,y=253)
        Entry(self.ventana,textvariable=self.nalLensiz).place(x=473,y=256)
        Label(self.ventana,text="nb frames:",bg=color_ventana,font=("Arial",13)).place(x=383,y=283)
        Entry(self.ventana,textvariable=self.nbFrames).place(x=473,y=286)
        Label(self.ventana,text="pix fmt:",bg=color_ventana,font=("Arial",13)).place(x=409,y=313)
        Entry(self.ventana,textvariable=self.pixFmt).place(x=473,y=316)
        Label(self.ventana,text="r frame rate:",bg=color_ventana,font=("Arial",13)).place(x=370,y=343)
        Entry(self.ventana,textvariable=self.rframeRate).place(x=473,y=346)
        Label(self.ventana,text="refs:",bg=color_ventana,font=("Arial",13)).place(x=428,y=373)
        Entry(self.ventana,textvariable=self.refs).place(x=473,y=376)
        Label(self.ventana,text="start pts:",bg=color_ventana,font=("Arial",13)).place(x=399,y=403)
        Entry(self.ventana,textvariable=self.startPts).place(x=473,y=406)
        Label(self.ventana,text="start time:",bg=color_ventana,font=("Arial",13)).place(x=390,y=433)
        Entry(self.ventana,textvariable=self.startTime).place(x=473,y=436)
        Label(self.ventana,text="time base:",bg=color_ventana,font=("Arial",13)).place(x=387,y=463)
        Entry(self.ventana,textvariable=self.timeBase).place(x=473,y=466)
        Label(self.ventana,text="width:",bg=color_ventana,font=("Arial",13)).place(x=420,y=493)
        Entry(self.ventana,textvariable=self.width).place(x=473,y=496)
        #Label(self.ventana,text="tags:",bg=color_ventana,font=("Arial",13)).place(x=732,y=103)
        #Entry(self.ventana,textvariable=self.tags).place(x=780,y=106)
        
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
            self.rateValue.set(self.null_finder('avg_frame_rate'))
            self.rateBit.set(self.null_finder('bit_rate'))
            self.chromaValue.set(self.null_finder('chroma_location'))
            self.codecValue.set(self.null_finder('codec_name'))
            self.codecLong.set(self.null_finder('codec_long_name'))
            self.codecTag.set(self.null_finder('codec_tag'))
            self.codecTstr.set(self.null_finder('codec_tag_string'))
            self.codecTbase.set(self.null_finder('codec_time_base'))
            self.codecType.set(self.null_finder('codec_type'))
            self.codedHeight.set(self.null_finder('coded_height'))
            self.disaspRatio.set(self.null_finder('display_aspect_ratio'))
            self.divxPacked.set(self.null_finder('divx_packed'))
            self.duration.set(self.null_finder('duration'))
            self.durationTs.set(self.null_finder('duration_ts'))
            self.profile.set(self.null_finder('profile'))
            self.hasbFrames.set(self.null_finder('has_b_frames'))
            self.height.set(self.null_finder('height'))
            self.index.set(self.null_finder('index'))
            self.isAvc.set(self.null_finder('is_avc'))
            self.level.set(self.null_finder('level'))
            self.nalLensiz.set(self.null_finder('nal_length_size'))
            self.nbFrames.set(self.null_finder('nb_frames'))
            self.pixFmt.set(self.null_finder('pix_fmt'))
            self.rframeRate.set(self.null_finder('r_frame_rate'))
            self.refs.set(self.null_finder('refs'))
            self.startPts.set(self.null_finder('start_pts'))
            self.startTime.set(self.null_finder('start_time'))
            self.timeBase.set(self.null_finder('time_base'))
            self.width.set(self.null_finder('width'))
            #self.tags.set(self.null_finder('tags'))

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


