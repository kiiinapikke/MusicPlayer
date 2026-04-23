import os
import tkinter as tk
from tkinter import filedialog
import vlc

class Player:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("500x500")

        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        self.folder = ""
        self.songs = []

        self.listbox = tk.Listbox(root)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        controls = tk.Frame(root)
        controls.pack()

        tk.Button(controls, text="Load", bg="yellow", command=self.load).grid(row=0, column=0)

        tk.Button(controls, text="Play", bg="green", command=self.play).grid(row=0, column=1)

        tk.Button(controls, text="Pause", bg="orange", command=self.pause).grid(row=0, column=2)

        tk.Button(controls, text="Stop", bg="red", command=self.stop).grid(row=0, column=3)

    def load(self):
        self.folder = filedialog.askdirectory()
        self.songs = [f for f in os.listdir(self.folder) if f.endswith(".mp3")]
        self.listbox.delete(0, tk.END)
        for s in self.songs:
            self.listbox.insert(tk.END, s)

    def play(self):
        sel = self.listbox.curselection()
        if not sel:
            return
        path = os.path.join(self.folder, self.songs[sel[0]])
        media = self.instance.media_new(path)
        self.player.set_media(media)
        self.player.play()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()

root = tk.Tk()
app = Player(root)
root.mainloop()
