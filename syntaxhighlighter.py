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
        #self.delimiters = [' ', '.', '\n',',', '!', ':']#used to tokenize text lines
        self.tokenstart = self.tokenstop= '0.0'
        self.highlight =False
        self.syntaxhighlighter()            
    
    
    def syntaxhighlighter(self, calledby=1):   
        """used for highlighting,
        calledby flag used to denote the block of code
        that called for the syntax highlighter:
        0 to denote the syntax highlighting is off
        and 
        1 to denote the syntax highlighting is on
        ::: default is on
        """
        #print("The value of called by is: ", calledby)
        

        if not self.highlight:                        
            startline = self.Scriptwindow.index('insert linestart')
            endline = self.Scriptwindow.index('insert lineend')
            

            curindex = startline
            
            self.tokenstart = startline
            
                
            while(startline != endline):                
                while (self.Scriptwindow.get(curindex).isalpha()):
                    curindex = self.Scriptwindow.index(curindex+'+1c')#increment
                    
                self.tokenstop = curindex    #tokenstop tokenizes word

                if calledby ==1:                    
                    self.wordhighlight(self.tokenstart, self.tokenstop, endline)
                self.tokenstart=self.Scriptwindow.index(curindex+'+1c') if \
                                curindex != endline else endline
                
                startline = self.tokenstart                
                curindex = startline
           
        
        self.Scriptwindow.after(100, lambda: self.syntaxhighlighter(1))


    def wordhighlight(self, tokenstart, tokenstop, endline):
        """check the tokenized word and see if it is the keyword
        """
        
        word = self.Scriptwindow.get(tokenstart, tokenstop)
        
        print("The word is: ", word)
        print("The tokenstart is: ", tokenstart)
        print("The tokenstop is:  ", tokenstop)
        print("The endline is:    ", endline)
        import time
        time.sleep(3)
        
        for key in keywords.keys():
            if word in keywords[key]:
                self.Scriptwindow.tag_add(key, tokenstart, tokenstop)
                self.Scriptwindow.tag_config(key, foreground=tagcolors[key])
            else:
                self.Scriptwindow.tag_remove(key, tokenstart, tokenstop)
        
        #the following code actually highlights
        #everything following the def keyword
        #but upon extracting the word following def
        #it de-highlights all after the word
        #effectively highlighting only the function name
        if word in keywords['pythonfunctions']:
                self.Scriptwindow.tag_add('arbitrary',tokenstop,endline)                                
                self.Scriptwindow.tag_config('arbitrary', foreground="#74cb6b")
        else:
            self.Scriptwindow.tag_remove('arbitrary', tokenstop, endline)
            

    
                    

            

    def makeaccessible(self,objects):                
        self.Scriptwindow = objects


if __name__  == '__main__':
    parent = Tk()

    h  = syntaxhighlight(parent)
    h.grid(row=0, column=0)
    h.mainloop()