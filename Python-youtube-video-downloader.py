import tkinter as tk
from tkinter import scrolledtext as sct
from tkinter import messagebox
from tkinter import ttk

from pytube import Stream
from pytube import YouTube

import os
from pathlib import Path

variabl1=tk.DoubleVar
variabl2=tk.DoubleVar
variabl3=tk.DoubleVar

filesize=0
stream1=list()
sct_diplay=list()

def list_streams():
    global Entry,sct1,Button1,Button
    
    s=""
    link=""
    link=str(Entry.get())
    if link=="":
        tk.messagebox.showwarning(message="Please give a url to download!")
        return
        
    try: 
        yt = YouTube(str(link)) 
    except: 
       tk.messagebox.showwarning(message="Check your internet connection!")
       return

    try: 
        stream = yt.streams.all()

        for i in stream:
                s1=str(i)
                s1=s1.strip("<>")
                stream1.append(s1.split(" "))
        k=1
        for j in stream1:
                s+=str(k)+"."+j[1]+" "+j[2]+" "+j[3]+" "+j[len(j)-1]+"\n"
                s+="\n"
                sct_diplay.append(str(j[1]))
                k+=1
        sct1.delete(1.0,"end")
        sct1.update()
        sct1.insert(tk.INSERT,s)
        tk.messagebox.showinfo(message="Successfully listed streams!") 
        Button['state']=tk.DISABLED
        Button1['state']=tk.NORMAL
          
    except: 
        tk.messagebox.showwarning(message="Unable to list streams!")
        return 
    

def download():

    global Entry1,Entry,Button1,Button,filesize

    link=str(Entry.get())
    itag=int(Entry1.get())
    try:
        path_to_download_folder = str(os.path.join(Path.home(), "Downloads"))

    except:
        tk.messagebox.showwarning(message="Unable to find downloads folder")
        return

   
    try:    
        yt = YouTube(str(link)) # yt = YouTube(str(link),on_progress_callback=progress)  to implement on_progress_callback
        yt1=yt.streams.get_by_itag(int(itag))
        filesize=yt1.filesize
        yt1.download(path_to_download_folder)
        tk.messagebox.showinfo(message="Download complete")
        Button['state']=tk.NORMAL

    except:
        tk.messagebox.showwarning(message="Unable to download! please selected another video")

#you can implement the progress bar here to show the progress
''''   
def progress( chunk, file_handle, bytes_remaining):
    global filesize,Label2,window,variabl3
    remaining=(100*(bytes_remaining))/filesize
    step=100-int(remaining)
    print("Comppleted:",step)#show the percentage of completed download
''' 

window=tk.Tk()
window.title("Youtube video downloader")
Label=tk.Label(window,text="Youtube video Url:")
Label.grid(row=0,padx=4)
Entry=tk.Entry(window,textvariable=variabl1,width=50)
Entry.grid(row=0,column=1,padx=4,pady=4)

sct1=sct.ScrolledText(window)
sct1.grid(row=1,columnspan=2,rowspan=6,padx=4,pady=4)

Button=tk.Button(window,text="List streams",command=list_streams)
Button.grid(row=7,columnspan=2,padx=4,pady=4)

Label1=tk.Label(window,text="itag of video you want to download:")
Label1.grid(row=8,padx=4)
Entry1=tk.Entry(window,textvariable=variabl2,width=50)
Entry1.grid(row=8,column=1,padx=4,pady=4)



Button1=tk.Button(window,text="Download",command=download,width=20,bg="Red")
Button1.grid(row=9,columnspan=2,padx=4,pady=4)
Button1['state']=tk.DISABLED
window.mainloop()