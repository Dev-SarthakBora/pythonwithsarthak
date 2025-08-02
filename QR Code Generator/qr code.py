import pyqrcode
import png
from PIL import ImageTk, Image
from pyqrcode import QRCode
import tkinter as tk 
from tkinter import *
import PIL.Image

Rootwindow = Tk()  
Rootwindow.geometry('500x550')
Rootwindow.title('QR generator0')

Label(Rootwindow,text='Lets Create QR Code',font='arial 15').pack()
name = tk.StringVar()
  
# Generate QR code
def create_qrcode():
    s1=name.get()
    qr = pyqrcode.create(s1)
    qr.png('myqr.png', scale = 6)
    Label(Rootwindow,text='QR Code is created and saved successfully').pack()

Entry(Rootwindow,textvariable=name,font='arial 15').pack()
Button(Rootwindow,text='create',bg='blue',command=create_qrcode).pack()
Rootwindow.mainloop()


# made by Sarthak Bora
# Date 15/10/24