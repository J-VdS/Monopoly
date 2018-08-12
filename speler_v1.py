# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 14:52:05 2018

@author: Jeroen VdS
"""

from tkinter import *
import time, random

class speler:
    straten = {'#663300':2, '#00008b':2 } #enige twee met andere
    '''
    zorgt voor alle standaard functies en constantes die een speler nodig heeft
    
    '''
    def __init__(self, tk, canvas, num, naam='speler'):
        #standaard locaties
        
        loc = [(593,613), (618, 613),(593, 638), (618, 638) ][num]
        self.kleur = ['#0015ab', '#12ab12', 'yellow', '#ab0000'][num]
        self.tk, self.canvas = tk, canvas
        self.vakje = 0
        self.vindex = 0
        self.vx = -55
        self.vy = 0

        r = 10
        self.id = self.canvas.create_oval(loc[0], loc[1], loc[0]+2*r, loc[1]+2*r, \
                                          fill=self.kleur)
        self.tk.update()
        #------------------
        self.naam = naam #max 10 tekens
        self.cash = 1500
        self.eigendommen = {} #or a list
        
        
        
        
    def worp(self):
        print('gegooid')
        (a, b) = (random.randint(1,6), random.randint(1,6))
        print(a, b)
        if a == b:
            return a+b, True
        return a+b, False
    
    def move(self, n):
        print('start moving')
        direc = [(-55, 0), (0, -55), (55, 0), (0, 55)]
        for i in range(n):
            self.vakje = (self.vakje+1)%40
            if self.vakje % 10 == 0:
                direc_10 = [(-75, -20), (20,-75), (75,20), (-20,75)]
                
                self.canvas.move(self.id, direc_10[self.vindex][0], direc_10[self.vindex][1])
                self.vindex = (self.vindex+1)%4
                (self.vx, self.vy) = direc[self.vindex]
                
            elif self.vakje % 5 == 0:
                self.canvas.move(self.id, (self.vx//55)*56, (self.vy//55)*56)
            else:
                self.canvas.move(self.id, self.vx, self.vy)
            time.sleep(0.3)
            self.tk.update()
                
        return self.vakje
    
    def __str__(self):
        return  str(self.naam)+' '*(10-len(self.naam))+str(self.cash)
    
    def __iadd__(self, other):
        #other moet een int zijn
        self.cash += other
        return self
    def __isub__(self, other):
        self.cash -= other
        return self
    

    #nodig voor ruilen    
    def __lshift__(self, other):
        # <<
        if other['kleur'] in self.eigendommen:
            self.eigendommen[other['kleur']].append(other)
        else:
            
            self.eigendommen[other['kleur']] = [other]
        return self
    
    def __rshift__(self, other):
        # >>
        return self
    
        
    
    
''' Standaard locaties 1: [(618, 618)]  '''  