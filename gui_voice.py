from tkinter import font
from ttkbootstrap import*
import ttkbootstrap as tb
from bot import asd




def liyr():
    asd()
    
"""*************************************"""
    
root=tb.Window(themename="cyborg")
root.title('voice_ai')
root.geometry('400x400')
root.minsize(400,400)
root.maxsize(400,400)
my_label=tb.Label(text="voice_ai",font=("Jokerman",40))
my_label.pack(pady=20)
my_button=tb.Button(text="start",bootstyle="danger,outline",command=liyr)
my_button.pack(pady=(10,1))
my_button=tb.Button(text="exit",bootstyle="danger,outline",command=root.quit)
my_button.pack(pady=(10,2))
lbl = tk.Label(text = "",font=("Comic Sans MS",40)) 
lbl.pack(pady=90)

root.mainloop()



