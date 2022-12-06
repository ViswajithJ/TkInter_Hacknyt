from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from pytube import YouTube
from pytube import exceptions

'''Function definitions'''


# to get vid stream of highest res, info about video, return in list
def get_vid_stream_data(link):
    yt_obj = YouTube(link)
    title = yt_obj.title
    channel = yt_obj.author
    length = round(yt_obj.length/60, 2)
    videos = yt_obj.streams
    vid_stream = videos.get_highest_resolution()
    size = round(vid_stream.filesize*0.000001, 2)
    res = vid_stream.__getattribute__("resolution")
    yt_video_info = [vid_stream, title, channel, length, size, res]
    return yt_video_info


def display_info(yt_video_info):
    i = 0
    rows = [
        "Title           :   " + yt_video_info[1],
        "Channel     :   " + yt_video_info[2],
        "Duration    :   " + str(yt_video_info[3]) + "min",
        "Size           :   " + str(yt_video_info[4]) + "MB",
        "Resolution :    " + yt_video_info[5]
    ]
    for row in rows:
        search_on_click = Label(
            frame2, text=row, bg='black', fg='green', font=('calibri', 14))
        search_on_click.place(relx=0, rely=i/8)
        i += 1


def download_video(vid_stream):
    path = tuple(filedialog.askdirectory())
    if (path != ()):
        path = "".join(path)
        try:
            vid_stream.download(path)
            messagebox.showinfo("Youtube Video Downloader",
                                "Downloaded successfully")
        except:
            messagebox.showerror(
                "Youtube Video Downloader", "An error occured.")
    else:
        messagebox.showinfo("Youtube Video Downloader", "Cancelled")


# on clicking search_btn
def search_video():
    link = search_entry.get()
    if (link != ''):
        try:
            yt_video_info = get_vid_stream_data(link)
            display_info(yt_video_info)

            download_btn = Button(
                window, image=download_img, borderwidth=0, command=lambda: download_video(yt_video_info[0]))
            download_btn.place(relx=0.35, rely=0.7,
                               relheight=0.17, relwidth=0.30)
        except exceptions.RegexMatchError:
            messagebox.showerror("Youtube Video Downloader",
                                 "Enter valid youtube video url")
        except exceptions.VideoUnavailable:
            messagebox.showerror("Youtube Video Downloader",
                                 "Video is unavailable")
        except Exception as err:
            messagebox.showerror(
                "Youtube Video Downloader", err)
    else:
        messagebox.showwarning("Youtube Video Downloader", "Enter a url")


''' Main Program '''


window = Tk()
window.title("Youtube Video Downloader")

canvas = Canvas(window, height=640, width=1024)
canvas.pack()

# images
bg_img = PhotoImage(file='./images/bg_image1.png')
yt_image1 = PhotoImage(file="./images/youtube-icon72.png")
search_img = PhotoImage(file="./images/search.png")
download_img = PhotoImage(file="./images/download_img1.png")

# background-img
bg_label = Label(window, image=bg_img)
bg_label.place(relheight=1, relwidth=1)

# frame for Search-bar
frame1 = Frame(window, bg='white', bd=5, borderwidth=0)
frame1.place(relx=0.5, rely=0.05, relheight=0.12, relwidth=0.75, anchor='n')

# frame for displaying Video-Data
frame2 = Frame(window, borderwidth=10, bg='black', bd=5, border=5)
frame2.place(relx=0.5, rely=0.3, relheight=0.40, relwidth=0.75, anchor='n')


# placing ytb icon in frame1
yt_label = Label(frame1, image=yt_image1, borderwidth=0)
yt_label.place(relx=0, rely=0, relheight=1, relwidth=0.1)

# placing Entry box in frame1
search_entry = Entry(frame1, borderwidth=5, fg='black', font=('calibri', 15))
search_entry.place(relx=0.1, rely=0, relheight=1, relwidth=0.8)
search_entry.insert(END, "Replace with a valid youtube url")

# placing Search button in frame1
search_btn = Button(frame1, image=search_img,
                    command=search_video, borderwidth=0)
search_btn.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)


window.mainloop()
