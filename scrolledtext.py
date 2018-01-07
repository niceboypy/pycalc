from tkinter import *


class ScrolledText(Frame):

    def __init__(self, parent=None):# if needed text='',file=None):
        Frame.__init__(self, parent)                
        #self.pack(expand=YES, fill=BOTH)
        self.setup()

    def setup(self):
        sbarV = Scrollbar(self)
        sbarH = Scrollbar(self)
        text = Text(self, relief=FLAT)
        sbarV.config(command=text.yview)
        sbarH.config(command=text.xview, orient=HORIZONTAL)
        text.config(yscrollcommand=sbarV.set, xscrollcommand=sbarH.set)
        sbarV.pack(side=RIGHT, fill=Y)
        sbarH.pack(side=BOTTOM, fill=X)
        text.pack(side=LEFT, expand=YES, fill=BOTH)
        self.makeaccessible(text)
       
    
    def makeaccessible(self, objects):
        """useful for overriding global object with the help of 
            different names e.g. self.textwindow, self.scriptwindow"""
        self.text = objects


     

if __name__ == '__main__':
    
    root = Tk()
    somekind = ScrolledText(root)
    somekind.grid(row=0, column=0, sticky='nsew')
    Grid.columnconfigure(somekind.master, 0, weight=1)
    Grid.rowconfigure(somekind.master, 0, weight=1)
    #somekind.config(bg='green')
    somekind.mainloop()

