from tkinter import *
from PIL import Image, ImageTk

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

root = Tk()
root.title("Анимированный GIF")

animated_label = AnimatedGIFLabel(root, "gif/micro_active.gif")
animated_label.pack()

root.mainloop()