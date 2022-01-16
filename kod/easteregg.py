#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import turtle
import time

def pos(trtl, x, y):
    trtl.pu()
    trtl.setpos(x, y)
    trtl.pd
    return

def easteregg(scores):
    window = turtle.Screen()
    window.colormode(255)
    window.bgcolor(231, 228, 237)
    window.setup(width = 1.0, height = 1.0, startx=None, starty=None)
    trtl = turtle.Turtle()

    trtl.ht()

    pos(trtl, -10, -10) 
    trtl.pd()
    trtl.shape("turtle")
    trtl.showturtle()
    trtl.rt(1000) 
    trtl.ht()
    trtl.clear()
    return scores