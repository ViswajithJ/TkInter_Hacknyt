from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def search_video():
    print('hi')


# main program
window = Tk()
window.title("Youtube Video Downloader")

canvas = Canvas(window, height=640, width=1024)
canvas.pack()

# images
bg_img = PhotoImage(file='./images/bg_image1.png')
yt_image1 = PhotoImage(file="./images/youtube-icon72.png")
search_img = PhotoImage(file="./images/search.png")

# background-img
bg_label = Label(window, image=bg_img)
bg_label.place(relheight=1, relwidth=1)

# frame for Search-bar
frame1 = Frame(window, bg='white', bd=5, borderwidth=0)
frame1.place(relx=0.5, rely=0.05, relheight=0.12, relwidth=0.75, anchor='n')

# frame for displaying Video-Data
frame2 = Frame(window, bg='white', bd=5, borderwidth=0)
frame2.place(relx=0.5, rely=0.3, relheight=0.40, relwidth=0.75, anchor='n')


# placing ytb icon in frame1
yt_label = Label(frame1, image=yt_image1, borderwidth=0)
yt_label.place(relx=0, rely=0, relheight=1, relwidth=0.1)

# placing Entry box in frame1
search_entry = Entry(frame1, borderwidth=5, fg='black', font=('calibri', 17))
search_entry.place(relx=0.1, rely=0, relheight=1, relwidth=0.8)
search_entry.insert(END, "Replace with a valid youtube url")

# placing Search button in frame1
search_btn = Button(frame1, image=search_img,
                    command=search_video, borderwidth=0)
search_btn.place(relx=0.9, rely=0, relheight=1, relwidth=0.1)


window.mainloop()
