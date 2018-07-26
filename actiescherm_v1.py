# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 16:29:03 2018

@author: Jeroen VdS
"""

from tkinter import *
import speler_v1


class acties:
    def __init__(self, tk, canvas, commutxt):
        #uit argumenten
        self.tk, self.canvas = tk, canvas
        self.commutxt = commutxt
        
        self.knoppen = {0:[[],[],[]], 1:[[],[]], 2:[[],[]], 3:[[],[]], 4:[[],[]]}
        self.state = 0
        
        self.state_0()
        self.state_1()
        self.state_2()
        self.state_3()
        self.state_4()
        
        
        
        self.speler = None
        self.alle_spelers = [] 
        
        self.canvas.bind_all('<Button-1>', self.clicked)
        
               
    def knop(self, x1, y1, x2, y2, actie, text, fill='grey'):
        b = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill, state='hidden')
        t = self.canvas.create_text((x2-x1)//2+x1, (y2-y1)//2+y1, text=text, \
                anchor='center', state='normal', font=('Helvetica', 12))
        return (b, t, actie)
    
        
    
    def state_0(self):
        pre = self.knoppen[0][0]
        cor = self.knoppen[0][1]
        extr = self.knoppen[0][2] #bevat alle extra zaken die geen buttons zijn
        
        self.aantal = 1
        pre +=self.knop( 20, 20,180, 60, ' ', 'AANTAL SPELERS', fill='#00bb20')
        pre +=self.knop( 20, 70, 60, 90, 'self.change(1)', '1')
        pre +=self.knop( 60, 70,100, 90, 'self.change(2)', '2')
        pre +=self.knop(100, 70,140, 90, 'self.change(3)', '3')
        pre +=self.knop(140, 70,180, 90, 'self.change(4)', '4')
        pre +=self.knop( 20,420,180,460, 'self.start()', 'START', fill='#15aba2')
        
        '''
        font = ('Helvetica', 12)
        extr += (self.canvas.create_text(20, 110, text='Speler 1:', font=font, anchor='nw'))
        '''
        

        for i in range(0, len(pre), 3):
            cor.append((self.canvas.coords(pre[i])))
        
        self.show(0)
        
        
        
    def state_1(self):
        pre = self.knoppen[1][0]
        cor = self.knoppen[1][1]
        
        pre +=self.knop(20, 20,180, 60, 'self.volgende()', 'Gooi/Einde beurt')
        pre +=self.knop(20, 80,180,120, 'self.switch_state(2)', 'Ruilen' )
        pre +=self.knop(20,140,180,180, 'self.switch_state(3)', 'Huizen en Hotels')
        #pre +=(self.knop(20,200,180,240, ))
        pre +=self.knop(20,260,180,300, 'self.switch_state(4)', 'info kaarten')

        pre +=self.knop(20,420,180,460, 'self.switch_state(10)', 'Instellingen')
        
        for i in range(0, len(pre), 3):
            cor.append((self.canvas.coords(pre[i])))
        
        self.hide(1)
        self.tk.update()
    
    def state_2(self):
        pre = self.knoppen[2][0]
        cor = self.knoppen[2][1]
        
        pre += self.knop(110,420,190,460, 'self.switch_state(1)', 'Terug' )
        
        for i in range(0, len(pre), 3):
            cor.append((self.canvas.coords(pre[i])))
        
        self.hide(2)
        self.tk.update()
    
    def state_3(self):
        pre = self.knoppen[3][0]
        cor = self.knoppen[3][1]
        
        pre += self.knop(110,420,190,460, 'self.switch_state(1)', 'Terug' )
        
        for i in range(0, len(pre), 3):
            cor.append((self.canvas.coords(pre[i])))
            
        self.hide(3)
        self.tk.update()
        
    
    def state_4(self):
        pre = self.knoppen[4][0]
        cor = self.knoppen[4][1]
        
        pre += self.knop(110,420,190,460, 'self.switch_state(1)', 'Terug' )
        
        for i in range(0, len(pre), 3):
            cor.append((self.canvas.coords(pre[i])))
            
        self.hide(4)
        self.tk.update()
        
    def clicked(self, evt):
        x = self.tk.winfo_pointerx() - self.tk.winfo_rootx()
        y = self.tk.winfo_pointery() - self.tk.winfo_rooty()
        
        st = self.state
        
        for i in range(len(self.knoppen[st][1])):
            knop = self.knoppen[st][1][i]
            if knop[0] < x < knop[2] and knop[1] < y < knop[3]:
                exec(self.knoppen[st][0][i*3+2]) #of evalf
                break
    
    def switch_state(self, to):
        self.hide(self.state)
        self.show(to)
        
        self.state = to
    
    def hide(self, state):
        for i in range(0, len(self.knoppen[state][0]), 3):
            self.canvas.itemconfig(self.knoppen[state][0][i], state='hidden')
            self.canvas.itemconfig(self.knoppen[state][0][i+1], state='hidden')
        
        if len(self.knoppen[state]) == 3:
            for i in self.knoppen[state][2]:
                self.canvas.itemconfig(i, state='hidden')
        
        self.tk.update()
        
        
            
    def show(self, state):
        for i in range(0, len(self.knoppen[state][0]), 3) :
            self.canvas.itemconfig(self.knoppen[state][0][i], state='normal')
            self.canvas.itemconfig(self.knoppen[state][0][i+1], state='normal')
        
        if len(self.knoppen[state]) == 3 and state != 0:
            for i in self.knoppen[state][2]:
                self.canvas.itemconfig(i, state='normal')
        
        self.tk.update()
    
    def change(self, a):
        self.aantal = a   
        print(self.aantal)
    
    def start(self):
        
        #voorlopig hier moet nog een naam systeem komen en mooie UI
        with open(self.commutxt, 'w') as outfile:
            outfile.write('Done'+'\n')
            outfile.write(str(self.aantal))
        del self.aantal
        self.switch_state(1)
        
    
    def get_players(self):
        return self.alle_spelers
    
    def set_player(self, player):
        print(player)
        self.speler = player
        self.dubbel = True
        
        #commu.txt voorbereiden
        with open(self.commutxt, 'w') as outfile:
            outfile.write('player: %s' %(str(self.speler))+'\n')
    
    def volgende(self):
        print(self.speler)
        if self.speler == None:
            return
        elif self.dubbel:
            (aantal, self.dubbel) = self.speler.worp()
            self.speler.move(aantal)
        
        else:
            with open(self.commutxt, 'a') as outfile:
                outfile.write('Done'+'\n')
        return             
        

if __name__ == '__main__':
    import time
    tk = Tk()
    tk.geometry('200x470+700+230')
    tk.wm_attributes('-topmost', 1)
    tk.update()
    canvas = Canvas(tk, width=200, height=470)
    canvas.pack()
    tk.update()
    
    _ = acties(tk, canvas, 'test.txt')
    
    
    while True:
        try:
            tk.update()
            tk.update_idletasks()
            time.sleep(0.2)
        except:
            break    

'''
uitleg over self.state:
    0 = beginscherm voor het initialiseren van het spel (aantal spelers, naam, kleur)
    1 = actiescherm met de basisknoppen waarop knop volgende beurt er onderaan opkomt
        (deze knop enkel actief als alle schulden betaald zijn)
    2 = actiescherm ruilen
    3 = actiescherm huizen
    4 = info kaarten (sjabloom maken)
    
    
    9 = intellingen
    10 = wachtscherm
'''       
