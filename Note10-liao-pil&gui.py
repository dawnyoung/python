# -*- coding: utf-8 -*-

#----------------------------------------------------------------------------------------
#         pil: python imaging library
#----------------------------------------------------------------------------------------

#  play with pictures

from PIL import Image

# open a jpg
im = Image.open('D:\python\Capture.jpg')

# get the size of this jpg
w, h = im.size
print('original size %s X %s' %(w, h))

# shrink to 50%
im.thumbnail((w//2, h//2))
print('new size %s X %s' %(w//2, h//2))

# save the shrinked image as jpeg
im.save('d:\python\shrinked.jpeg', 'jpeg')
#%%

# add filter
from PIL import Image, ImageFilter
im = Image.open('d:\python\Capture.jpg')
im2 = im.filter(ImageFilter.BLUR) # blur
im2.save('d:\python\im2.jpeg', 'jpeg')
#%%

im3 = im.filter(ImageFilter.EMBOSS)
im3.save('d:\python\im3.jpeg', 'jpeg')

#   Filters
# CONTOUR
# DETAIL
# EDGE_ENHANCE
# EDGE_ENHANCE_MORE
# EMBOSS
# FIND_EDGES
# SMOOTH
# SMOOTH_MORE
# SHARPEN
#%%

# make a security code
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import random

# random character
def ranChar():
    return chr(random.randint(65, 90))
    
# random color 1: background color
def ranCol():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

# random color 2: character color
def ranCol2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))
    
# width, height, rgb-coded color
w = 240
h = 60
im = Image.new('RGB', (w, h), (255, 255, 255))

# font
font = ImageFont.truetype('arial.ttf', 36)

# draw
draw = ImageDraw.Draw(im)

# background
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill = ranCol())

# characters
for t in range(4):
    draw.text((60 * t + 10, 10), ranChar(), font = font, fill = ranCol2())

# blur
im = im.filter(ImageFilter.BLUR)
im.save('d:\python\im4.jpeg', 'jpeg')
#%%

#-------------------------------------------------------------------------------------------
#     GUI
#-------------------------------------------------------------------------------------------

# Tkinter
# wxWidgets
# Qt
# GTK

from tkinter import *  # import everything

class Application(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
    def createWidgets(self):
        self.helloLable = Label(self, text = 'hello world')
        self.helloLable.pack()
        self.quitButton = Button(self, text = 'quit', command = self.quit)
        self.quitButton.pack()
    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'hello %s' % name)
        
app = Application()
app.master.title('hello world')
app.mainloop()
#%%)