# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 22:14:24 2019

@author: lenovo
"""
#import sleep
from PIL import Image,ImageDraw,ImageFont
img=Image.open("forsk.jpg.png")
font_type1=ImageFont.truetype('Montserrat-Regular.ttf',30)
font_type_1=ImageFont.truetype('Qwerty Ability - Personal Use.otf',45)
font_type2=ImageFont.truetype('Concetta Kalvani Signature.ttf',30)
draw=ImageDraw.Draw(img)
(x, y) = (200, 10)
draw.text((x,y),text="IDENTITY CARD",fill='Black',font=font_type_1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 70)
draw.text((x,y),text="Name=Kuldeep Singh Shekhawat",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 130)
draw.text((x,y),text="father's name= MR.Indra Singh Shekhawat",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 200)
draw.text((x,y),text="Semester=5th",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 270)
draw.text((x,y),text="Branch=computer SCience and Engg.",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 320)
draw.text((x,y),text="contact_no=7742775759",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (10, 380)
draw.text((x,y),text="Institute Name=Forsk Technologies pvt. ltd",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)

(x, y) = (20, 420)
draw.text((x,y),text="Sign of the manager",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (130, 470)
draw.text((x,y),text="Sylvester",fill='Black',font=font_type2)
draw=ImageDraw.Draw(img)
(x, y) = (570, 420)
draw.text((x,y),text="Sign of the student",fill='Black',font=font_type1)
draw=ImageDraw.Draw(img)
(x, y) = (600, 470)
draw.text((x,y),text="kuldeep",fill='Black',font=font_type2)
draw=ImageDraw.Draw(img)
img.show()

from Tkinter import *
from PIL import ImageTk,Image
backgroundImage = PhotoImage("IMG_20190304_093949")
... other stuffs

root=Tk()
canvasWidth=600
canvasHeight=400
self.canvas=Canvas(root,width=canvasWidth,height=canvasHeight)
backgroundImage=root.PhotoImage("D:\Documents\Background.png")
backgroundLabel=root.Label(parent,image=backgroundImage)
backgroundLabel.place(x=0,y=0,relWidth=1,relHeight=1)
self.canvas.pack()
root.mainloop()