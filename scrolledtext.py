from tkinter import *


class ScrolledText(Frame):

    def __init__(self, parent=None):# if needed text='',file=None):
        Frame.__init__(self, parent)
        #self.pack(expand=YES, fill=BOTH)
        self.setup()


    def setup(self):
        scrollbarconfig ={'relief':FLAT}

        sbarV = Scrollbar(self,**scrollbarconfig)
        sbarH = Scrollbar(self, orient=HORIZONTAL,**scrollbarconfig)

        #sbarh.pack(side=bottom, fill=Y)
        sbarH.pack(side=BOTTOM, expand=YES,fill=X)
        #sbarV.pack(side=RIGHT, fill=Y)
        sbarV.pack(side=RIGHT, expand=YES, fill=Y)

        text = Text(self, relief=FLAT, wrap=NONE)
        
        text.config(xscrollcommand=sbarH.set)
        text.config(yscrollcommand=sbarV.set)

        sbarV.config(command=text.yview)
        sbarH.config(command=text.xview)
        
        
        text.pack(side=LEFT, expand=YES,fill=BOTH)
        self.makeaccessible(text)
    
    def makeaccessible(self, objects):
        """useful for overriding global object with the help of 
            different names e.g. self.textwindow, self.scriptwindow"""
        self.text = objects


     

if __name__ == '__main__':
    
    root = Tk()

    somekind = ScrolledText(root)
    somekind.pack()
    somekind.mainloop()
    #do nothing


"""#Import Tkinter
from tkinter import *
#define master
master = Tk()

#Horizontal (x) Scroll bar
xscrollbar = Scrollbar(master, orient=HORIZONTAL)
xscrollbar.pack(side=BOTTOM, fill=X)
#Vertical (y) Scroll Bar
yscrollbar = Scrollbar(master)
yscrollbar.pack(side=RIGHT, fill=Y)

#Text Widget
text = Text(master, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.pack()

#Configure the scrollbars
xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)
#Run tkinter main loop
mainloop()"""