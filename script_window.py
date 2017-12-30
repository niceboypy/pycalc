

from tkinter import *
import threading
from scrolledtext import ScrolledText as scriptwin


class ScriptWindow(scriptwin):
    def __init__(self, parent=None):
        scriptwin.__init__(self,parent=parent)
        self.setconfigs()

    
    def setconfigs(self):
        """setup configurations for the texteditor"""
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        #access by self.scriptwindow the text widget        
        #test: self.scriptwindow.insert(INSERT, 'test sentence')
        self.scriptwindow.bind('<KeyPress>', self.startthreadcheck) #start thread on key press
                                                                    #TO-DO end thread?
        self.scriptwindow.bind('<KeyPress-space>', self.test)

        
    def test(self,event):
        print("Some test here")


    


    def startthreadcheck(self,event):
        """implementing syntax highlighting algorithm
            implemented in a thread to make GUI active"""

    
        


    def makeaccessible(self, objects):

        #overridden from ScrolledText
        self.scriptwindow = objects



if __name__ == '__main__':
    
    parent = Tk()
    instance = ScriptWindow(parent)
    instance.pack()
    mainloop()