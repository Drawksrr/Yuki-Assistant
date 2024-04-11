from tkinter import *
import timermod
from tkinter.messagebox import showinfo, askyesnocancel
import threading

link = ""

def auth_window():
    stop_flag = True
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
                stop_flag = False
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
                stop_flag = False
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
    
auth_window()