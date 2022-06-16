# NEED TO ADD SAVE BUTTON STILL

from tkinter import *
from tkinter import ttk, filedialog

from PIL import ImageTk, Image, ImageDraw, ImageFont

global filename


def loading_image():
    loading_image.filename = filedialog.askopenfile().__getattribute__("name")
    with Image.open(loading_image.filename) as im:
        resized_img = im.resize((600, 600))
        picture = ImageTk.PhotoImage(resized_img)
        canvas.create_image(20, 20, image=picture, anchor=NW)
        root.mainloop()


def add_watermark():
    with Image.open(loading_image.filename) as im:
        resized_img = im.resize((600, 600))
        draw = ImageDraw.Draw(resized_img)
        font = ImageFont.truetype(font="arial.ttf", size=30)
        draw.text((300, 150), text="Hello World", fill=(100, 100, 100), font=font)
        add_watermark.final_img = ImageTk.PhotoImage(resized_img)
        canvas.create_image(20, 20, image=add_watermark.final_img, anchor=NW)
        root.mainloop()

def save_img():
    pass
    # add_watermark.final_img.save("hello.jpg")

    # files = [('All Files', '*.*'),
    #          ('Python Files', '*.py'),
    #          ('Text Document', '*.txt')]
    # file = filedialog.asksaveasfile(filetypes=files, defaultextension=files)
    # if file:
    #     saving =open(add_watermark.final_img, "rb").read()
    #     file.write(saving)
    #     file.close()


root = Tk()
canvas = Canvas(root, width=600, height=600)
canvas.pack()

root.title("Image Watermarking")
root.state('zoomed')

frame = ttk.Frame(root)
load_image = ttk.Button(root, text="Load Image", command=loading_image)
load_image.pack()
add_watermark = ttk.Button(root, text="Add Bookmark", command=add_watermark)
add_watermark.pack()
save_watermarked_img = ttk.Button(root, text="Save Image")
save_watermarked_img.pack()
root.mainloop()
