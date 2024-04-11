from tkinter import *
from pathlib import Path
from tkinter.messagebox import showinfo, askyesnocancel
from alerts_in_ua import Client as AlertsClient
from PIL import Image, ImageTk
from tkextrafont import Font
import threading
import datetime
import timermod
import soundmod

alerts_client = AlertsClient(token="adb83999749af2d97631f4d8da3fc882237afe2dab2203")

def while_alert():
    global alert_status
    while True:
        alert_status = alerts_client.get_air_raid_alert_status('Харківська область')
        if str(alert_status) == "active:Харківська область":
            print("ТРЕВОГА ТВОЮ МАТЬ!")
        elif str(alert_status) == "no_alert:Харківська область":
            print("а нету тревоги")
        timermod.sleeptime(15)

def main():
    timermod.sleeptime(2)
    app = Tk() 
    app.title("Yuki Assistant")
    app.iconbitmap("voice.ico")
    app.geometry("560x480")
    app.overrideredirect(False)
    app.resizable(False, False)
    app["bg"] = "#2e3642"
    
    class AnimatedGIFLabel(Label):
        def __init__(self, master, path_to_gif):
            Label.__init__(self, master)
            self.path_to_gif = path_to_gif
            self.frames = []
            self.load_frames(0)
            self.idx = 0
            self.delay = 100  # задержка между кадрами (в миллисекундах)
            self.next_frame()

        def load_frames(self, idx):
            self.frames = []
            gif = Image.open(self.path_to_gif)
            while True:
                try:
                    gif.seek(idx)
                    self.frames.append(ImageTk.PhotoImage(gif.copy()))
                    idx += 1
                except EOFError:
                    break

        def next_frame(self):
            self.config(image=self.frames[self.idx])
            self.idx += 1
            if self.idx == len(self.frames):
                self.idx = 0
            self.after(self.delay, self.next_frame)
    
    font_path = "fonts/Play-Bold.ttf"
    play_bold = Font(file=font_path, family="Play")
    
    x = app.winfo_screenwidth()
    y = app.winfo_screenheight()
    app.wm_geometry(f"560x480+{x//2-560//2}+{y//2-480//2}")

    app.background = PhotoImage(file="psd/background_main.png")
    bg = Label(app , image=app.background)
    bg.place(x=-2 , y=-2)

    current_label = Label(app, text="Поточний урок: Історія України", anchor="w", font=("Play Bold", 15), bg="white", fg="black")
    current_label.place(x=120, y=120, height=50, width=320)
    
    next_label = Label(app, text="Наступний урок: ", anchor="w", font=("Play Bold", 15), bg="white", fg="black")
    next_label.place(x=120, y=180, height=50, width=320)

    micro_animated = AnimatedGIFLabel(app, "gif/micro_active.gif")
    #micro_animated.place(x=120, y=240, height=48, width=48)
    
    micro_static_img = PhotoImage(file="psd/micro_static.png")
    micro_static = Label(app, image=micro_static_img)
    micro_static.place(x=120, y=300, height=48, width=48)
    
    thread_alert = threading.Thread(target=while_alert)
    thread_alert.start()
    
    app.mainloop()

def auth_window():
    timermod.sleeptime(3)
    def close(event):
        auth.destroy()
    
    def event_enter(event):
        link_input = str(link_entry.get())
        link_format = link_input.replace("/h", "/")
        link = open("link.yuki", "w")
        link.write(str(link_format))
        link.close()
        if link_input == "":
            pass
        else:
            result =  askyesnocancel(title="Подтвержение операции", message="Подтвердить операцию?")
            if result==None: 
                showinfo("Результат", "Операция приостановлена")
            elif result: 
                showinfo("Результат", "Операция подтверждена")
                timermod.sleeptime(1.2)
                auth.destroy()
                main()
            else: 
                showinfo("Результат", "Операция отменена")
    
    def enter():
        link_input = str(link_entry.get())
        link_format = link_input.replace("/h", "/")
        link = open("link.yuki", "w")
        link.write(str(link_format))
        link.close()
        if link_input == "":
            pass
        else:
            result =  askyesnocancel(title="Подтвержение операции", message="Подтвердить операцию?")
            if result==None: 
                showinfo("Результат", "Операция приостановлена")
            elif result: 
                showinfo("Результат", "Операция подтверждена")
                timermod.sleeptime(1.2)
                auth.destroy()
                main()
            else: 
                showinfo("Результат", "Операция отменена")
    
    auth = Tk() 
    auth.title("Yuki Assistant")
    auth.iconbitmap("lock.ico")
    auth.geometry("560x420")
    auth.overrideredirect(True)
    auth.resizable(False, False)
    auth["bg"] = "#2e3642"

    x = auth.winfo_screenwidth()
    y = auth.winfo_screenheight()
    auth.wm_geometry(f"560x420+{x//2-560//2}+{y//2-420//2}")

    auth.background = PhotoImage(file="psd/background_auth.png")
    bg = Label(auth , image=auth.background)
    bg.place(x=-2 , y=-2)

    link_entry = Entry(auth, justify=LEFT, borderwidth=1, font="Calibri 12", relief=SUNKEN)
    link_entry.place(x=130, y=120, height=35, width=300)
    
    link_button = Button(auth, text="Надіслати посилання", font="Calibri 12", borderwidth=0, bg="#3c99a1", fg="white", activebackground="#45b1ba", activeforeground="white",  relief=FLAT, command=enter)
    link_button.place(x=130, y=160, height=35, width=300)
    
    link_entry.bind("<Return>", event_enter)
    auth.bind("<Escape>", close)
    
    auth.mainloop()

def voice(number, lesson):
    if number == 1:
        if str(lesson) == "algebra":
            soundmod.sound("tts/number/first.mp3")
            soundmod.sound("tts/lesson/algebra.mp3")
        elif str(lesson) == "geometry":
            soundmod.sound("tts/number/first.mp3")
            soundmod.sound("tts/lesson/geometry.mp3")

def first_start():
    check_file = open("check.yuki", "w")
    check_file.write("Checked!")
    check_file.close()
    auth_window()

check_file = Path("check.yuki")
check_file.touch()

link_file = Path("link.yuki")
link_file.touch()

check_file = open("check.yuki", "r")
user_check = check_file.read()
check_file.close()

link_file = open("link.yuki", "r")
link = link_file.read()
link_file.close()

if user_check == "":
    first_start()
elif link == "":
    first_start() 
else:
    main()
