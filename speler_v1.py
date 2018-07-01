# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 14:52:05 2018

@author: Jeroen VdS
"""

from tkinter import *
import time, random

class speler:
    '''
    zorgt voor alle standaard functies en constantes die een speler nodig heeft
    
    '''
    def __init__(self, tk, canvas, num):
        #standaard locaties
        loc = [(618,618), (648, 618),(618, 648), (648, 648) ][num]
        self.tk, self.canvas = tk, canvas
        self.vakje = 0
        self.vindex = 0
        self.vx = -55
        self.vy = 0

        r = 5
        self.id = self.canvas.create_oval(loc[0], loc[1], loc[0]+2*r, loc[1]+2*r, \
                                          fill='#0000ab')
        #------------------
        self.cash = 1500
        self.eigendommen = {} #or a list
        
        
        
        
    def worp(self):
        (a, b) = (random.randint(1,6), random.randint(1,6))
        print(a, b)
        if a == b:
            return a+b, True
        return a+b, False
    
    def move(self, n):
        direc = [(-55, 0), (0, -55), (55, 0), (0, 55)]
        for i in range(n):
            self.vakje = (self.vakje+1)%40
            if self.vakje % 10 == 0:
                self.canvas.move(self.id, (self.vx//55)*82, (self.vy//55)*82)
                self.vindex = (self.vindex+1)%4
                (self.vx, self.vy) = direc[self.vindex]
                
            elif self.vakje % 5 == 0:
                self.canvas.move(self.id, (self.vx//55)*56, (self.vy//55)*56)
            else:
                self.canvas.move(self.id, self.vx, self.vy)
                
        return self.vakje
    
''' Standaard locaties 1: [(618, 618)]  '''  