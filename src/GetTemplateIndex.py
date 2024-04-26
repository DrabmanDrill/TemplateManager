import urllib.request, sys
import tkinter as tk
import tkinter.font as tkFont

files = "https://raw.githubusercontent.com/DrabmanDrill/TemplateIndex/main/TemplateIndex/test.txt"

window = tk.Tk()
Percentage = 0
font = tkFont.Font()

window.title = "TemplateIndexDownloader"
window.geometry("200x200")

l1 = tk.Label(window, text="Downloading Index", anchor="center").pack()
l2 = tk.Label(window, text=(Percentage, "%"), anchor="center").pack()

#url = sys.argv[1]
#file_name = url.split('/')[-1]

urllib.request.urlretrieve(files)

window.mainloop()
