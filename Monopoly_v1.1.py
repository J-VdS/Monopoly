from tkinter import *
from veld_v1 import veld
import time

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


if __name__ == '__main__':
    main()
        
    
