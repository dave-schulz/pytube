import tkinter
import customtkinter
from pytube import YouTube


def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!", text_color="green")
    except:
        finishLabel.configure(text="Download Error...", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_downloaded = bytes_downloaded / total_size * 100
    per = str(int(percentage_downloaded))
    progress_bar_label.configure(text=per + '%')
    progress_bar_label.update()
    progress_bar.set(float(percentage_downloaded / 100))

    # Setup
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Downloader")

# Title
title = customtkinter.CTkLabel(app, text="Insert a YouTube link")
title.pack(padx=10, pady=10)

# Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Progress Bar
progress_bar_label = customtkinter.CTkLabel(app, text="0%")
progress_bar_label.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=400)
progress_bar.set(0.5)
progress_bar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)
download.pack(padx=10, pady=10)

app.mainloop()
