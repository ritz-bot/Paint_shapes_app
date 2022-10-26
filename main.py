import numpy as np
from PIL import Image
# data=np.zeros((5,4,3), dtype=np.uint8)
# data[:]=[255,198,0]
# print(data)
# data[0:3,0:2]=[255,145,0]
# data[1:4,1:3]=[255,200,231]
#
# img=Image.fromarray(data,'RGB')
# img.save("canvas.png")


class Square:
    def __init__(self,x,y,side,color):
        self.color = color
        self.x = x
        self.y = y
        self.side = side

    def make(self, canvas):
        canvas.data[self.x : self.x+ self.side , self.y : self.y+self.side] = self.color

class Rectangle:
    def __init__(self,len,bred,color,x,y):
        self.y = y
        self.x = x
        self.color = color
        self.bred = bred
        self.len = len
    def make(self,canvas):
        canvas.data[self.x : self.x + self.len, self.y: self.y + self.bred] = self.color
class Canvas:
    def __init__(self,width,height,color):
        self.color = color
        self.width= width
        self.height = height

        self.data = np.zeros((self.width, self.height, 3), dtype=np.uint8)
        self.data[:]=self.color


    def make(self,imagepath):

        img=Image.fromarray(self.data,'RGB')
        img.save(imagepath)
print("please mention the color scheme of the canvas:")
canvas_width=int(input("plaese mention the width of canvas:"))
canvas_length=int(input("plaese mention the length of canvas:"))
colors={'white':(255,255,255),'black': (0,0,0)}
canva_color=input("Enter the color of the canvas:")
canvas = Canvas(width=canvas_width,height=canvas_length,color=colors[canva_color])
while True:
    shape_type = input("please enter what you want to draw:")
    if shape_type.lower() == "Rectangle":
        rect_len = int(input("please enter the length of rectangle: "))
        rect_bre = int(input("please enter the breadth of rectangle: "))
        rect_x = int(input("please enter the x coordinate of rectangle: "))
        rect_y = int(input("please enter the x coordinate of rectangle: "))
        red = int(input("How much red you want to inculcate"))
        blue = int(input("How much blue you want to inculcate"))
        green = int(input("How much green you want to inculcate"))

        r1 = Rectangle(len=rect_len, bred=rect_bre, x=rect_x, y=rect_y, color=[red, green, blue])
        r1.make(canvas)

    if shape_type.lower() == "Square":

        sq_side = int(input("please enter the side of square: "))
        sq_x = int(input("please enter the x coordinate of square: "))
        sq_y = int(input("please enter the x coordinate of suare: "))
        red = int(input("How much red you want to inculcate"))
        blue = int(input("How much blue you want to inculcate"))
        green = int(input("How much green you want to inculcate"))

        s1 = Square(x=sq_x, y=sq_y, side=sq_side, color=[red, blue, green])
        s1.make(canvas)

    if shape_type == "quit":
        break




canvas.make('kali.png')

