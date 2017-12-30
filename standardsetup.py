#!/usr/bin/python3

from tkinter import *

from scrolledtext import ScrolledText


class  standard_display_set(Frame):
    def __init__(self, parent=None):


        self.additionals = []#just one button for now
        self.configurations = {'config':{
                      'button1':{
                          'text':'script','relief':FLAT,
                          'bg':'#989898','width':1,
                          'font':(' ', 9, '')                         
                                }
                        },
                      'grid':{
                          'button1':{
                          'row':0, 'column':1, 'rowspan':3, 'sticky':N+S
                                    },
                          'button2':{
                          'row':0, 'column':2, 'rowspan':3, 'sticky':N+S
                                    }
                      }                     
                    }


        self.parent = parent
        #Frame.__init__(self)
        self.setstandard()
        
        #optional
        self.makewidgets(self.parent)
        

    
    def setstandard(self):
        """set standard block, just define, not configure"""
      
      
        #set the standard input, display and output panels
        #output panel topmost
        self.output = Message(self.parent)
        #display panel
        #records history
        #until evaluated
        
         
        self.display = ScrolledText(self.parent)
        #entry widget
        self.entry = Entry(self.parent)        
        
        #set configuration for the standard panel
        self.standard_UIconfigure()
        self.entry.focus()
        self.standard_CommandConfigure()


    def standard_UIconfigure(self):
        """configurations of all the standard block properties"""
        #configure subparent
        self.parent.grid(row=0, column=0, sticky=E+W+N+S)
        
        #########################################################
        #output panel properties
        #config options
        #########################################################
        output_configs ={
            'bg':'#ced4c6', 'fg':'#000000', 'relief':FLAT,
            'font':(' ',25, 'bold')
        }#configurations defined as a single peice        
        self.output.grid(row=0, column=0, sticky=EW)
        self.output.config(**output_configs)
        

        #########################################################
        #display properties
        #config options
        #########################################################
        display_text_configs={
            'height':10,'font':(' ', 15, 'normal'), 'bg':'#f8f8f8',
            'relief':FLAT
        }
        self.display.text.config(**display_text_configs)       
        self.display.grid(row=1, column=0,sticky=N+S+E+W)
        #display friendly status
        self.display.text.insert(INSERT, "YOUR STATUS:"+'\n'+'________________\n'+' '+'')
        self.display.text.config(state='disabled')

        #setting scrollbar
        scrollbar = Scrollbar(self.parent)
        
        
        
        #########################################################
        #input properties
        #config options
        #########################################################
        entry_configs ={
            'font':('',15, ''), 'bg':'#45b4c8', 'relief':FLAT

        }
        self.entry.config(**entry_configs)
        self.entry.grid(row=2, column=0, sticky=EW)

        Grid.columnconfigure(self.parent, 0, weight=1)
        Grid.rowconfigure(self.parent,1,weight=1)
        Grid.columnconfigure(self.parent.master, 0, weight=1)
        Grid.rowconfigure(self.parent.master,0,weight=1)

        
    def standard_CommandConfigure(self):
        """configure standard panel's command and basic behaviour"""
        self.configureoutputpanel()
        self.display.text.bind('<KeyPress>', self.onKeyPress)
        self.entry.bind('<Return>', self.OnEntryReturn)       

    def configureoutputpanel(self):
        """override in class or todo later"""
        pass
        

    def makewidgets(self, parent):
        #make the message dialog
        if  self.additionals: #raise ValueError('No items defined')

            self.addition_items = [self.identify(parent, *items) for items in self.additionals]
            for item in self.addition_items:
                #TODECIDE
                #self.addition_items.append(item(parent)) #save if neccessary
                item.config(**(self.configurations['config'][item.NAME]))
                item.grid(**(self.configurations['grid'][item.NAME]))#see respective configuration
                
            self.addition_items[0].config(command=self.onScriptButton)

    def identify(self,parent, Object, name):
        obj = Object(parent)
        setattr(obj, 'NAME', name)
        #return object with additional property with instance set
        return obj

    def onKeyPress(self, event):
        """callback on keypress"""
        self.display.config(state='disabled')

    def OnEntryReturn(self,event):
        """on entry return"""
        information = self.entry.get() #get all the contents
        self.display.text.config(state='normal')
        self.display.text.mark_set(INSERT, END)
        self.display.text.insert(INSERT, '\n'+information)
        self.display.text.config(state='disabled')
        self.display.text.see(END)
        self.entry.delete(0,END)
    
    def onScriptButton(self):
        #override in subclass
        pass





if __name__ == '__main__':
                 

    class prototype( standard_display_set):
        def __init__(self, Parent):
             standard_display_set.__init__(self, parent=Parent)

        

    root = Tk()
    parent = Frame(root)

    parent.pack(expand=YES, fill=BOTH)
    parent.config(bg='green')
    parent.config()
    x = prototype(parent)
    mainloop()