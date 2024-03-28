import qrcode
import cv2
import tkinter as tk


def generate_code():
    string_code = generate.get()
    image = qrcode.make(string_code)
    image.save('code.gif')
    im = cv2.imread('code.gif')
    img = tk.PhotoImage(file=r'code.gif')
    new_width, new_height, c = im.shape
    root.img = img
    canvas.config(width=new_width, height=new_height)
    canvas.create_image(new_width/2, new_height/2, image=img, anchor='center')
    root.geometry(f'{new_width+200}x{new_height+200}')


imgage = qrcode.make('QR Code generator by Kamil Seternus')
imgage.save('code.gif')

root = tk.Tk()
root.title('QR Code generator')
root.geometry('580x520')
root.minsize(520, 420)

canvas = tk.Canvas(root, width=340, height=340, background='#ffffff', borderwidth=1)
canvas.pack(pady=20)
img = tk.PhotoImage(file=r'code.gif')
root.img = img
canvas.create_image(170, 170, image=img, anchor='center')

generate = tk.Entry(root, font='Calibri 22', width=33)
generate.pack()

generate_button = tk.Button(root, font='Calibri 22', text='Generate QR Code', command=generate_code)
generate_button.pack(pady=20)

root.mainloop()
