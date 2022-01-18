from tkinter import *
from PIL import Image, ImageTk
#import tkinter as Tk
#from tkinter import ttk
from tkinter import filedialog as fd



class fenetre(Tk):
    def __init__(self):
        Tk.__init__(self)
        # création des widgets "esclaves" :
        self.height = 400
        self.width = 600
        # decalage lors de la calibration
        self.offsetX = 0
        self.offsetY = 0
        self.calibration = True
        # canvas
        self.can1 = Canvas(self, bg='dark grey', height=self.height, width=self.width)
        self.can1.pack(side=LEFT, padx=5, pady=5)
        self.image = "images/Motion_Shot.jpg"
        # nom des images traitees
        self.im = None
        # dimension des images traitees
        self.im_X = 0
        self.im_Y = 0 
        self.coef_X = 1
        self.coef_Y = 1
        # liste de valeurs saisies lors du pointage
        self.listeX = []
        self.listeY = []
        self.listeT = [0]
        self.valeurs = 'X,Y,T\n'
        # affichage dynamique du Label
        self.text_affichage = StringVar()
        #self.text_affichage.set("listes")
        self.create()
        #self.replay()


    def replay(self):
        #self.txt1.destroy()
        #self.txt1 = Label(self, text='vous avez deja \n une image')
        self.listeX = []
        self.listeY = []
        self.listeT = [0]
        self.valeurs = 'X,Y,T\n'
        self.text_affichage.set("Cliquer au centre\n du cercle rouge \n pour CALIBRER")
        self.im_origin = self.can1.create_image(0, 0, anchor="nw", image=self.photo_origin)
        self.calibrer()


    def select_file(self,event=None):
        filetypes = (
            # ('text files', '*.txt'),
            ('img files', '*.jpg'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)

        self.image = filename
        print(self.image)

        self.can1.delete("all")
        # image d'origine
        self.im = Image.open(self.image)
        self.im_X = self.im.size[0]
        self.im_Y = self.im.size[1]
        self.redimensionne()
        self.im = self.im.resize((int(self.im_X / self.coef_X), int(self.im_Y / self.coef_Y)), Image.ANTIALIAS)
        self.photo_origin = ImageTk.PhotoImage(self.im)

        self.im_origin = self.can1.create_image(0, 0, anchor="nw", image=self.photo_origin)
        #self.can1.tag_bind(self.im_origin, "<ButtonRelease>", self.select_file)
        self.replay()


    def redimensionne(self):
        self.im_X = self.im.size[0]
        self.im_Y = self.im.size[1]

        self.coef_X = self.im_X / 600
        self.coef_Y = self.im_Y / 400
        self.im = self.im.resize((int(self.im_X // self.coef_X), int(self.im_Y // self.coef_Y)), Image.ANTIALIAS)

    def calibrer(self):
        centreX = 100
        centreY = 100
        R = 50
        self.can1.create_oval((centreX-R//2, centreY-R//2), (centreX+R//2, centreY+R//2), outline = 'black',fill = 'red')
        self.can1.create_line((centreX-R//5, centreY-R//5), (centreX+R//5, centreY+R//5), width=2, fill = 'black')
        self.can1.create_line((centreX-R//5, centreY+R//5), (centreX+R//5, centreY-R//5), width=2, fill = 'black')
        self.calibration = True

    def clic(self,event):
        """ Gestion de l'événement clic gauche sur la zone graphique """

    
        if not(self.calibration):
            # position du pointeur de la souris (avec correction offset)
            X = event.x_root - self.offsetX
            Y = event.y_root - self.offsetY
            print(X,Y)
            # on dessine un carré
            r = 4
            self.can1.create_rectangle(X-r, Y-r, X+r, Y+r, outline = 'black',fill = 'green')
            self.listeX.append(X)
            self.listeY.append(Y)
            self.listeT.append(self.listeT[-1]+1)
            self.valeurs += '{},{},{}\n'.format(
                    str(X), 
                    str(Y), 
                    str(self.listeT[-1]))
            self.text_affichage.set(self.valeurs)
        else:
            self.offsetX = event.x_root - 100
            self.offsetY = event.y_root - 100
            self.calibration = False
            self.im_origin = self.can1.create_image(0, 0, anchor="nw", image=self.photo_origin)
            self.text_affichage.set("commencer le \n pointage")            
 

    def valider(self):
        fichier = open('coordonnees.txt', 'w')
        fichier.write(self.valeurs)
        fichier.close()
        self.text_affichage.set("coordonnées enregistrées \n dans \n coordonnees.txt")
        
    
    def create(self):
            self.bou1 = Button(self, text='Quitter', command=self.quit)
            self.bou1.pack(side=BOTTOM)
            #self.txt1 = Label(self, text='Choisir une image')
            self.bou2 = Button(self, text='select image', command=self.select_file)
            self.bou2.pack()
            
            self.label = Label(self, textvariable=self.text_affichage)
            self.label.pack()

            self.bou3 = Button(self, text='Recommencer', command=self.replay)
            self.bou3.pack(side=BOTTOM)
            
            self.bou4 = Button(self, text='Valider', command=self.valider)
            self.bou4.pack(side=BOTTOM)

            """
            self.bou5 = Button(self, text='entrelacer', command=self.superpose)
            self.bou5.pack()
            """
            # image d'origine
            self.im = Image.open(self.image)
            """
            self.im_X = self.im.size[0]
            self.im_Y = self.im.size[1]
            #self.redimensionne()
            self.coef_X = self.im_X / 600
            self.coef_Y = self.im_Y / 400
            self.im = self.im.resize((int(self.im_X // self.coef_X), int(self.im_Y // self.coef_Y)), Image.ANTIALIAS)
            #print('image redimensionné self.coef_X vaut {}, self.coef_Y vaut {}'.format(self.coef_X, self.coef_Y))
            """
            self.redimensionne()
            self.photo_origin = ImageTk.PhotoImage(self.im)

            #self.im_origin = self.can1.create_image(0, 0, anchor="nw", image=self.photo_origin)
            self.replay()
            self.can1.bind('<Button-1>', self.clic)








# run the application
if __name__ == '__main__':
    fen0 = fenetre()
    fen0.mainloop()
