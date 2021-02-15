from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_Name = ""

def openLocation():
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name, fg="green")

    else:
        locationError.config(text="Please Choose A Folder", fg="black")

#donwload video
def DownloadVideo():
    choice = ytdchoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)

        if(choice == choices[0]):
            select = yt.streams.filter(progressive=True).first()

        elif(choice == choices[1]):
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]):
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(text="Paste Link again", fg="black")

    select.download(Folder_Name)
    ytdError.config(text="Download Completed!", fg="green", font=("jost",15,"bold"))



root = Tk()
root.title("YouTube Video Downloader")
root.geometry("330x255")
root.resizable(False, False)
root.columnconfigure(0, weight=1)

ytdLabel = Label(root, text="Enter the URL of the Video", font=("jost",15))
ytdLabel.grid()

ytdEntryVar = StringVar()
ytdEntry = Entry(root, width=50, textvariable=ytdEntryVar)
ytdEntry.grid(pady=5)

ytdError = Label(root, text="", fg="black", font=("jost",10))
ytdError.grid()

saveLabel = Label(root, text="Save the Video File", font=("jost",15))
saveLabel.grid()

saveEntry = Button(root, width=16, bg="red", fg="White", text="Choose Output Path", command=openLocation)
saveEntry.grid()

locationError = Label(root, text="", fg="black", font=("jost",10))
locationError.grid()

ytdQuality = Label(root, text="Select Quality", font=("jost",15))
ytdQuality.grid()

choices = ["1080p","720p","480p","360p","240p","144p","Audio"]
ytdchoices = ttk.Combobox(root, values=choices)
ytdchoices.grid(pady=5)

downloadbtn = Button(root, text="Download", width=10, bg="red", fg="White", command=DownloadVideo)
downloadbtn.grid()

developerlabel = Label(root, text="", font=("jost",15))
developerlabel.grid()

root.mainloop()