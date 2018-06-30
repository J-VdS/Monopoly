from tkinter import *
import time

#from veld_v1.1 import veld


def main():
    tk = Tk()
    tk.geometry('700x700+5+5')
    tk.title('Monopoly')
    tk.resizable(0,0)    

    tk.update()

    while True:
        try:
            tk.update()
            tk.update_idletasks()
            time.sleep(0.2)
        except:
            break

if __name__ == '__main__':
    main()
        
    
