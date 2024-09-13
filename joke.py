from PIL import Image, ImageDraw, ImageFont, ImageFilter
import textwrap
import random
# from tkinter import *

with open("Jokes.txt") as f:
    content = f.read().splitlines()

astr = content[random.randrange(len(content))]
MAX_W, MAX_H = 1280, 400
size = (1280,400)
background = Image.new('RGB', (MAX_W, MAX_H), 'black')
draw = ImageDraw.Draw(background)
if len(astr) > 120:
    font=ImageFont.truetype('Arial Black.ttf', 40)
else:
    font=ImageFont.truetype('Arial Black.ttf', 60)

o_left, o_top, o_right, o_bottom = font.getbbox(astr)
o_width = o_right - o_left
o_height = o_bottom - o_top
y_text = MAX_H - (MAX_H - o_height)
wrapper = textwrap.TextWrapper(width=30)
words = wrapper.wrap(text=astr)
for line in words:
    left, top, right, bottom = font.getbbox(line)
    width = right - left
    height = bottom-top
    draw.text(((MAX_W - width) / 2, y_text), 
                  line, font=font, fill="blue")
    y_text += height

background.save("page.png")

root = Tk()
canvas = canvas(root, width=1280, height=400)
logo = PhotoImage(file="page.png")
canvas.create_image(0,0,image=logo)
root.mainloop()
