from tkinter import *

import time, veld_v1, speler_v1, actiescherm_v1

class monopoly:
    def __init__(self):
        self.commu = 'communicatie.txt'
        self.windows = []
        self.canvas = []
        
        #schermpjes
        self.veld = None #wordt gemaakt in speelveldfunctie
        self.speelveld()
        self.stand()
        self.acties()
        
        #communicatie document
        with open(self.commu, 'w') as outfile:
            outfile.write('initialisatie')
        
        self.get_info()
        
        #info spelers
        self.spelers = []
        
        
        #self.main()
    
    def speelveld(self):
        speelveld = Tk()
        speelveld.geometry('700x700+0+0')
        speelveld.title('Monopoly - veld')
        speelveld.resizable(0,0)
        speelveld.wm_attributes('-topmost', 1)
        canvas1 = Canvas(speelveld, width=700, height=700)
        canvas1.pack()
        
        self.veld = veld_v1.veld(speelveld, canvas1)
        
        self.windows.append(speelveld)
        self.canvas.append(canvas1)  
    
    def stand(self):
        stand = Tk()
        stand.geometry('200x200+700+0')
        stand.title('Monopoly - stand')
        stand.resizable(0,0)
        stand.wm_attributes('-topmost', 1)
        canvas2 = Canvas(stand, width=200, height=200)
        canvas2.pack()
        
        self.windows.append(stand)
        self.canvas.append(canvas2)
        
    def acties(self):
        actieveld = Tk()
        actieveld.resizable(0,0)
        actieveld.geometry('200x470+700+230')
        actieveld.title('Monopoly - actiescherm')
        actieveld.resizable(0,0)
        actieveld.wm_attributes('-topmost', 1)
        canvas3 = Canvas(actieveld, width=200, height=500)
        canvas3.pack()
        
        self.actiescherm = actiescherm_v1.acties(actieveld, canvas3, self.commu)
        
        self.windows.append(actieveld)
        self.canvas.append(canvas3)
        
    def get_info(self):
        
        while True:
            with open(self.commu, 'r') as infile:
                data = [i.strip() for i in infile.readlines()]
            if 'Done' in data:
                break
            if not self.standaard():
                return
        
        
        
        
            
            
                









    
    def standaard(self):
        try:
            for i in range(3):
                self.windows[i].update()
                self.windows[i].update_idletasks()
                time.sleep(0.3)
        except :
            self.windows[(i+1)%3].destroy()
            self.windows[(i+2)%3].destroy()
            return False
        return True
    
                
    
        
        
'''
def main():
    
    speelveld = Tk()
    speelveld.geometry('700x700+5+5')
    speelveld.title('Monopoly')
    #tk.resizable(0,0)    
    speelveld.wm_attributes('-topmost', 1)
    canvas1 = Canvas(speelveld, width=700, height=700)
    canvas1.pack()
    
    _ = veld(speelveld, canvas1)
        
    while True:
        try:
            speelveld.update()
            speelveld.update_idletasks()
            time.sleep(0.2)
        except:
            break

'''
if __name__ == '__main__':
    _ = monopoly()
    
        
    
