from tkinter import *
import glob, time

class veld:
    def __init__(self, tk):
        self.tk = tk
        self.canvas = Canvas(self.tk, width=700, height=700)
        self.canvas.pack()
        self.tk.update()
        

        self.images = self.load_img()
        self.vakjes()
        self.straten()
        

    def load_img(self):
        a = {}
        for file in glob.glob('*.gif'):
            a[file[1:-4]] = PhotoImage(file=file)
        #print(a)    
        return a

    def vakjes(self):
        self.canvas.create_rectangle(10,10,670,670)
        for i in range(11):
            for j in range(11):
                if 0<i<10 and 0<j<10:
                    continue
                
                elif i%5 == 0 and j%5 == 0:
                    self.special(i, j)
                #tekent het vakje van de straten (+algemeen fonds, kans en belast)
                elif i == 0 :
                    self.canvas.create_rectangle(37+j*55+(j//5), 10,\
                                                 92+j*55+(j//5), 92)
                elif i == 10:
                    self.canvas.create_rectangle(37+j*55+(j//5), 588,\
                                                 92+j*55+(j//5), 670)
                elif j == 0:
                    self.canvas.create_rectangle(10, 37+i*55+(i//5),\
                                                 92, 92+i*55+(i//5))                  
                else:
                    #j == 10
                    self.canvas.create_rectangle(588, 37+i*55+(i//5),\
                                                 670, 92+i*55+(i//5))
                    
                
                    
            
                
        self.tk.update()
    
    
    def special(self, i, j):
        #tekent de img's
        if (i,j) == (0,0):
            self.canvas.create_image(10, 10, image=self.images['pot'], \
                                     anchor=NW)
        elif (i, j) == (0,5):
            self.canvas.create_image(92+4*55, 10, image=self.images['station3'], \
                                     anchor=NW)
        elif (i, j) == (0,10):
            self.canvas.create_image(148+8*55, 10, image=self.images['gotojail'], \
                                     anchor=NW)
        elif (i, j) == (5,0):
            self.canvas.create_image(10, 92+4*55, image=self.images['station2'], \
                                     anchor=NW)
        elif (i, j) == (5,10):
            self.canvas.create_image(148+8*55, 92+4*55, image=self.images['station4'], \
                                     anchor=NW)
        elif (i, j) == (10,0): 
            self.canvas.create_image(10, 148+8*55, image=self.images['jail'], \
                                     anchor=NW)
        elif (i, j) == (10,5): 
            self.canvas.create_image(92+4*55, 148+8*55, image=self.images['station1'], \
                                     anchor=NW)
        elif (i, j) == (10,10):
            self.canvas.create_image(148+8*55, 148+8*55, image=self.images['start'], \
                                     anchor=NW)
        #tekent de vakjes rond de img's
        if i%10 == 0 and j%10 == 0:
            self.canvas.create_rectangle(10+(j//10)*(138+8*55), 10+(i//10)*(138+8*55),\
                                         92+(j//10)*(138+8*55), 92+(i//10)*(138+8*55))
        elif i==5:
            self.canvas.create_rectangle(10+(j//10)*(138+8*55), 10+(82+4*55),\
                                         92+(j//10)*(138+8*55), 66+(82+4*55))
        elif j==5:
            self.canvas.create_rectangle(10+(82+4*55), 10+(i//10)*(138+8*55), \
                                         66+(82+4*55), 92+(i//10)*(138+8*55))
        
    def straten(self):
        '''
        tekent de kleine balkjes door eerst een txt op te vragen en die data
        te verwerken'''
        #leest txt (dit is een lijst) en slaat hem op in een variabele
        straatinfo = ''
        with open('straten.txt', 'r') as infile:
            straatinfo = [eval(line) for line in [i.strip() for i in infile.readlines()]]
                       
        
        for straat in straatinfo:
            
            (i,j) = straat['loc']
            if straat['type'] == 'straat':
            
                #todo herleid de 4 if statements naar 2 
                if i == 0:
                    self.canvas.create_rectangle(37+j*55+(j//5), 72,\
                                                 92+j*55+(j//5), 92, \
                                                 fill=straat['kleur'])
                
                elif i == 10:
                    self.canvas.create_rectangle(37+j*55+(j//5), 588,\
                                                 92+j*55+(j//5), 608,\
                                                 fill=straat['kleur'])
                elif j == 0:
                    self.canvas.create_rectangle(72, 37+i*55+(i//5),\
                                                 92, 92+i*55+(i//5), 
                                                 fill=straat['kleur'])
                else:
                    #j == 10:
                    self.canvas.create_rectangle(588, 37+i*55+(i//5),\
                                                 608, 92+i*55+(i//5), 
                                                 fill=straat['kleur'])
            elif straat['type'] == 'kans' or straat['type'] == 'alg':
                #tekent kans afb
                #Todo in 1 lijn mogelijk
                if i == 0:
                    self.canvas.create_image(37+j*55+(j//5), 10, anchor=NW, \
                                        image=self.images[straat[type]+'3'])
                elif i == 10:
                    self.canvas.create_image(37+j*55+(j//5), 588, anchor=NW, \
                                        image=self.images[straat[type]+'1'])
                elif j == 0:
                    self.canvas.create_image(10, 37+i*55+(i//5), anchor=NW, \
                                        image=self.images[straat[type]+'2'])
                else:
                    #j == 10
                    self.canvas.create_image(588, 37+i*55+(i//5), anchor=NW, \
                                        image=self.images[straat[type]+'4']])
        
        self.tk.update()
        
        
        
            
        
        
                        
                    
        

if __name__ == '__main__':
    tk = Tk()
    tk.wm_attributes('-topmost', 1)
    tk.update()
    tk.geometry('700x700+0+0')
    
    veld(tk)
    
    
    time.sleep(5)
    tk.destroy()
