import tkinter as tk
from compressmodule import compress,decompress
from tkinter  import filedialog


def open_file():
    filename=filedialog.askopenfilename(initiadir='/',title="Select a file to compress")
    return filename

def compression(i,o):
    compress(i,o)

def decompression(ip,op):
    decompress(ip,op)

window=tk.Tk()
window.title("Compression engine")
window.geometry("300x200")

input_entry=tk.Entry(window)
output_entry=tk.Entry(window)

compress_button=tk.Button(window,text="COMPRESS",command=lambda:compression(input_entry.get(),output_entry.get()))


input_label=tk.Label(window,text="File to be compressed")
output_label=tk.Label(window,text="Name of compressed file")

input_label.grid(row=0,column=0)
input_entry.grid(row=0,column=1)
output_label.grid(row=1,column=0)
output_entry.grid(row=1,column=1)
compress_button.grid(row=2,column=1)

input_entry=tk.Entry(window)
output_entry=tk.Entry(window)

decompress_button=tk.Button(window,text="DECOMPRESS",command=lambda:decompression(input_entry.get(),output_entry.get()))


input_label=tk.Label(window,text="File to be decompressed")
output_label=tk.Label(window,text="Name of decompressed file")

input_label.grid(row=4,column=0)
input_entry.grid(row=4,column=1)
output_label.grid(row=5,column=0)
output_entry.grid(row=5,column=1)
decompress_button.grid(row=6,column=1)

window.mainloop()