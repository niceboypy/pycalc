from tkinter import *
from pycalmod import keywords, tagcolors
from scrolledtext import ScrolledText as scrpwin
import threading
import random
import time

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
        self.delimiters = [' ', '.', '\n',',', '!', ':']#used to tokenize text lines
        self.tokenstart = self.tokenstop= '0.0'
        self.highlight =False
        self.syntaxhighlighter()            
    
    
    def syntaxhighlighter(self):        
        if not self.highlight:                        
            startline = self.Scriptwindow.index('insert linestart')
            endline = self.Scriptwindow.index('insert lineend')
            curindex = startline
            #print("The startline is: ", startline)
            #print("The endline is: ", endline)
            self.tokenstart = startline

            while(startline != endline):                
                while not(self.Scriptwindow.get(curindex) in self.delimiters):
                    curindex = self.Scriptwindow.index(curindex+'+1c')#increment
                    #print("The current index is: ", curindex)
                    #time.sleep(2)
                    #print("in the second loop",random.randrange(1, 50))

                #startline = curindex                  #update startline for check
                self.tokenstop = curindex    #tokenstop tokenizes word
                self.wordhighlight()
                self.tokenstart=self.Scriptwindow.index(curindex+'+1c') if \
                                curindex != endline else endline
                #print("Tokenstart here is: ", self.tokenstart)
                startline = self.tokenstart                
                curindex = startline
            #print("loops ended")
        self.after(100, self.syntaxhighlighter)


    def wordhighlight(self):
        """check the tokenized word and see if it is the keyword
        """
        word = self.Scriptwindow.get(self.tokenstart, self.tokenstop)
        for key in keywords.keys():
            if word in keywords[key]:
                self.Scriptwindow.tag_add(key, self.tokenstart, self.tokenstop)
                self.Scriptwindow.tag_config(key, foreground=tagcolors[key])
            else:
                self.Scriptwindow.tag_remove(key, self.tokenstart, self.tokenstop)



    def makeaccessible(self,objects):                
        self.Scriptwindow = objects




if __name__  == '__main__':
    parent = Tk()

    h  = syntaxhighlight(parent)
    h.grid(row=0, column=0)
    h.mainloop()