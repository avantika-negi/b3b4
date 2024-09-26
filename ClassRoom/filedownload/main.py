from file_downloader import download_file as dwld
import tkinter as tk

root =tk.Tk()
root.title("File Downloader")
root.geometry("500x200")

def buttonCall():
    url= urlinput.get()
    fname=filenameInput.get()
    print(f"Url:{url}\nFilename:{fname}")
    dwld(url,fname)
    pass

# label enter url
urlLabel = tk.Label(root,text ="URL")

#urlLabel.pack(padx=10,pady=10)
urlLabel.grid(row=0,column=0)

#  URL entry
urlinput = tk.Entry(root)

#urlinput.pack(padx=10,pady=10)
urlinput.grid(row=0,column=1)

# label enter filename
filenameLabel=tk.Label(root,text="Filename")
filenameLabel.grid(row=1,column=0)

# file name entry
filenameInput=tk.Entry(root)
filenameInput.grid(row=1,column=1)

# button
downloadButton = tk.Button(root, text="Download",command = buttonCall)
downloadButton.grid(row=2,column=1)


root.mainloop()
