from ttk import  Frame
import ttk as nttk
from tkinter import *

selected_item = []
listbox_hauptpflicht = []




class ChooserFrame(Frame):


    def populateFrame(self):
        global selected_item
        selected_item = StringVar()

        # Subframe for "Hauptwahlpflicht"
        txt = nttk.Label(text="Item")
        frame_hauptpflicht = nttk.Frame()
        global listbox_hauptpflicht
        listbox_hauptpflicht = Listbox(frame_hauptpflicht, activestyle = 'dotbox', listvariable = selected_item)
        listbox_hauptpflicht.insert(0,'Item1')
        listbox_hauptpflicht.insert(1, 'Item2')
        listbox_hauptpflicht.insert(2, 'Item3')
        listbox_hauptpflicht.pack(expand=TRUE, fill=BOTH)

        # Subframe for "Hauptwahl"
        frame_hauptwahl = nttk.Frame()
        txt = nttk.Label(frame_hauptwahl, text="Some text")
        txt.pack(side=LEFT, expand=TRUE, fill=BOTH)
        button_sample = nttk.Button(frame_hauptwahl, text="Click me!")
        button_sample.pack(side=LEFT, expand=TRUE, fill=BOTH)

         #Notebook construction (using frame objects)
        notebook = nttk.Notebook(self)
        notebook.add(frame_hauptpflicht, text="Hauptwahlpflicht")
        notebook.add(frame_hauptwahl, text="Hauptwahl")
        notebook.pack(side=LEFT, fill=BOTH, expand=TRUE)

        # Used as an interface for other widgets to get the content of the currently selected line
    def getSelectedItem(self):
        global listbox_hauptpflicht
        index = listbox_hauptpflicht.curselection()
        # Return 0 if no item is currently selected
        if (index):
            return listbox_hauptpflicht.get(index, last=index)[0]

        else:
            return 0