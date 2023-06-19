from pygame import mixer
from tkinter import *
import os

def playsong():
    currentsong=playlist.get(ACTIVE)
    print(currentsong)
    mixer.music.load(currentsong)
    songstatus.set("playing")
    mixer.music.play()

def pausesong():
    songstatus.set("paused")
    mixer.music.pause()

def stopsong():
    songstatus.set("stopped")
    mixer.music.stop()

def resumesong():
    songstatus.set("resuming")
    mixer.music.unpause()

root= Tk()
root.title("music player")

mixer.init()
songstatus= StringVar()
songstatus.set("choosing")

playlist=Listbox(root,selectmode=SINGLE,bg= "DodgerBlue2",fg="white",font=("arial",15),width=40)
playlist.grid(columnspan=5)

a = 'songs'
if os.path.exists(a):
    os.chdir(r'songs')
else:
    os.mkdir('songs')
    os.chdir(r'songs')
songs= os.listdir()
for s in songs:
    playlist.insert(END,s)

playbtn1= Button(root,text="play",command= playsong)
playbtn1.config(font=("arial",20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn1.grid(row=1,column=0)

playbtn2= Button(root,text="pause",command= pausesong)
playbtn2.config(font=("arial",20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn2.grid(row=1,column=1)

playbtn3= Button(root,text="stop",command= stopsong)
playbtn3.config(font=("arial",20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn3.grid(row=1,column=2)

playbtn4= Button(root,text="resume",command= resumesong)
playbtn4.config(font=("arial",20),bg="DodgerBlue2",fg="white",padx=7,pady=7)
playbtn4.grid(row=1,column=3)

root.mainloop()