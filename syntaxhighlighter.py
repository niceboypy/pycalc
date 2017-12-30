from tkinter import *
from pycalmod import keywords, tagcolors
from scrolledtext import ScrolledText as scrpwin
import threading
import random

class syntaxhighlight(scrpwin):
    
    def __init__(self,parent=None):
        scrpwin.__init__(self,parent=parent)
        self.setupscrpwin()
        self.builtkeys = {} #dictionary to cache keywords
        self.tokenstart = '1.0'
        self.tokenstop = self.Scriptwindow.index(END)

    def setupscrpwin(self):
        """setup the configurations for scrpwin widget"""
        #setup widget .after method
        #for syntax highlighting
        self.Scriptwindow.bind('<Key>', self.setflag)
        self.delimiters = [' ', '.', '\n',',', '!', ':']#used to tokenize text lines
        self.tokenstart = self.tokenstop= '0.0'
        self.Scriptwindow.after(20000, self.syntaxhighlighter)
        self.highlight =False
    
    def setflag(self,event):
        self.highlight = False   
    
    
    def syntaxhighlighter(self):
        
        #get the linestart and lineend of the 
        #line in which the cursor is placed
        print("here we've come")        
        
        if not self.highlight:                        
            startline = self.Scriptwindow.index('insert linestart')
            endline = self.Scriptwindow.index('insert lineend')
            curindex = startline
            print("The startline is: ", startline)
            print("The endline is: ", endline)
            self.tokenstart = startline

            while(startline != endline):
                print("in the first loop", random.randrange(1, 50))
                import time
                time.sleep(3)
                    
                while not(self.Scriptwindow.get(curindex) in self.delimiters):
                    curindex = self.Scriptwindow.index(curindex+'+1c')#increment
                    print("The current index is: ", curindex)
                    time.sleep(2)
                    print("in the second loop",random.randrange(1, 50))

                #startline = curindex                  #update startline for check
                self.tokenstop = curindex    #tokenstop tokenizes word
                self.wordhighlight()
                self.tokenstart=self.Scriptwindow.index(curindex+'+1c') if \
                                curindex != endline else endline
                print("Tokenstart here is: ", self.tokenstart)
                startline = self.tokenstart                
                curindex = startline
            print("loops ended")


    def wordhighlight(self):
        """check the tokenized word and see if it is the keyword
        """
        word = self.Scriptwindow.get(self.tokenstart, self.tokenstop)
        print("The word is: ", word)


    def makeaccessible(self,objects):                
        self.Scriptwindow = objects




if __name__  == '__main__':
    parent = Tk()

    h  = syntaxhighlight(parent)
    h.grid(row=0, column=0)
    h.mainloop()