from turtle import *

def sierpinski(length,depth):
    if depth>1: dot()
    if depth==0:
        stamp()
    else:
        forward(length)
        sierpinski(length/2,depth-1)
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2,depth-1)
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2,depth-1)
        backward(length)
        left(120)

sierpinski(200,6)            
        