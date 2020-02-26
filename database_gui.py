#!/usr/bin/python3
# Matthew Buckmaster
# 2/10/2020

"""GUI version of game_database.py"""

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText

TITLE_FONT = ("Times New Roman", 24)

BOTTOM_FONT = ("Arial", 15)

class Screen(tk.Frame):
    
    current = 0
    
    def __init__(self):
        tk.Frame.__init__(self)    
        
    def switch_frame():
        screens[Screen.current].tkraise()    

class MainMenu(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.lbl_title = tk.Label(self, text = "Game Library", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0)
        self.btn_add = tk.Button(self, text = "Add", font = BOTTOM_FONT,command=self.go_add)
        self.btn_add.grid(row = 1, column = 0)
        self.btn_edit = tk.Button(self, text = "Edit", font = BOTTOM_FONT,command=self.go_edit)
        self.btn_edit.grid(row = 2, column = 0)
        self.btn_search = tk.Button(self, text = "Serach", font = BOTTOM_FONT,command=self.go_search)
        self.btn_search.grid(row = 3, column = 0)
        self.btn_remove = tk.Button(self, text = "Remove", font = BOTTOM_FONT,command=self.go_remove)
        self.btn_remove.grid(row = 4, column = 0)
        self.btn_save = tk.Button(self, text = "Save", font = BOTTOM_FONT,command=self.go_save)
        self.btn_save.grid(row = 5, column = 0)   
        
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1)
        
    def go_add(self):
        Screen.current = 1
        Screen.switch_frame()
        
    def go_edit(self):

        pop_up = tk.Tk()
        pop_up.title("Edit Selection")
        frm_edit_select = EditSelect(pop_up)
        frm_edit_select.grid(row = 0, column = 0)
        
    def go_search(self):
        Screen.current = 2
        Screen.switch_frame()        
        
    def go_remove(self):
        Screen.current = 5
        Screen.switch_frame()    
        
    def go_save(self):
        Screen.current = 7
        Screen.switch_frame()  

class AddScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        #Configure
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1) 
        self.grid_columnconfigure(3, weight = 1)  
        self.grid_columnconfigure(4, weight = 1) 
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)  
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1) 
        self.grid_rowconfigure(4, weight = 1)  
        self.grid_rowconfigure(5, weight = 1)
        self.grid_rowconfigure(6, weight = 1)   
        
        #Title
        self.lbl_screen_title = tk.Label(self, text = "Add Screen", font = TITLE_FONT)
        self.lbl_screen_title.grid(row = 0, column = 0, columnspan=3, sticky = "new")
        
        #Input
        self.lbl_title = tk.Label(self,text = "Title: ")
        self.lbl_title.grid(row = 1, column = 0)
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 1, column = 1)
       
        self.lbl_genre = tk.Label(self,text = "Genre: ")
        self.lbl_genre.grid(row = 2, column = 0)  
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 2, column = 1)     
        
        self.lbl_dev = tk.Label(self,text = "Developer: ")
        self.lbl_dev.grid(row = 3, column = 0)  
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 3, column = 1)  
        
        self.lbl_pub = tk.Label(self, text = "Publisher: ")
        self.lbl_pub.grid(row = 4, column = 0)  
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 4, column = 1)           
        
        self.lbl_platform = tk.Label(self,text = "Platform: ")
        self.lbl_platform.grid(row = 5, column = 0)  
        self.ent_platform = tk.Entry(self)
        self.ent_platform.grid(row = 5, column = 1)          
        
        self.lbl_release = tk.Label(self,text = "  Release Date: ")
        self.lbl_release.grid(row = 1, column = 2)  
        self.ent_release = tk.Entry(self)
        self.ent_release.grid(row = 1, column = 3)               
        
        self.lbl_rate = tk.Label(self,text = "Rating: ")
        self.lbl_rate.grid(row = 2, column = 2)  
        self.ent_rate = tk.Entry(self)
        self.ent_rate.grid(row = 2, column = 3) 
        
        self.lbl_price = tk.Label(self,text = "Price: ")
        self.lbl_price.grid(row = 3, column = 2)  
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row = 3, column = 3)
        
        self.lbl_purchase = tk.Label(self,text ="  Purchase Date: ")
        self.lbl_purchase.grid(row = 4, column = 2)  
        self.ent_purchase = tk.Entry(self)
        self.ent_purchase.grid(row = 4, column = 3)
        
        #Drop Down
        self.lbl_mode = tk.Label(self,text = "Mode: ")
        self.lbl_mode.grid(row = 5, column = 2)          
        self.options = ["Singleplayer", "Multiplayer"] 
        self.dbx_mode = tk.StringVar(self)
        self.dbx_mode.set(self.options[0])
        self.menu = tk.OptionMenu(self, self.dbx_mode,*self.options)
        self.menu.grid(row=5,column=3,sticky="wns")
        
        self.cbx_beat = tk.Checkbutton(self, text = "Beaten?")
        self.cbx_beat.grid(row = 6, column = 2, sticky = "ws")
        
        #Notes
        self.lbl_notes = tk.Label(self,text = "Notes: ")
        self.lbl_notes.grid(row = 6, column = 1,sticky="ws")                
        self.scr_notes = ScrolledText(self,width=59,height=12)
        self.scr_notes.grid(row = 7, column = 0, columnspan = 4,sticky="news")    
        
        #Buttons
        self.btn_back = tk.Button(self,text = "Back", font = BOTTOM_FONT,command=self.go_back)
        self.btn_back.grid(row = 8, column = 0, sticky = "news")
        self.btn_clear = tk.Button(self,text = "Reset", font = BOTTOM_FONT,command=self.reset)
        self.btn_clear.grid(row = 8, column = 1, sticky = "news")
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT,command=self.go_confirm)
        self.btn_submit.grid(row = 8, column = 3, sticky = "news")     
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame() 
        
    def reset(self):
        print("Reset")    
        
    def go_confirm(self):
        Screen.current = 0
        Screen.switch_frame()        

class EditSelect(tk.Frame):
    def __init__(self,parent):
        tk.Frame.__init__(self, master = parent)
        self.parent = parent

        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)  
        self.grid_rowconfigure(2, weight = 1)        
        
        self.lbl_edit_question = tk.Label(self,text = "Which Game Would You Like To Edit? ", font = BOTTOM_FONT)
        self.lbl_edit_question.grid(row = 0, column = 0, columnspan = 3) 
        
        self.lbl_mode = tk.Label(self,text = "Game List: ")
        self.lbl_mode.grid(row = 1, column = 0, sticky = "news") 
        self.options = ["Select a Title"]
        for key in games.keys():
            self.options.append(games[key][0])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])        
        self.menu = tk.OptionMenu(self, self.tkvar,*self.options)
        self.menu.grid(row=1,column=1, sticky = "wesn")        
        
        self.btn_edit_cancel = tk.Button(self, text = "Cancel", command = self.cancel)
        self.btn_edit_cancel.grid(row = 2, column = 0) 
        self.btn_edit_ok = tk.Button(self, text = "Ok", command = self.go_edit)
        self.btn_edit_ok.grid(row = 2, column = 1) 
                
    def cancel(self):
        self.parent.destroy()
        
    def go_edit(self): 
        Screen.current = 3
        
        if self.tkvar.get() == self.options[0]:
            pass
        else:
            for i in range(len(self.options)):
                if self.tkvar.get() == self.options[i]:
                    screens[Screen.current].edit_key = i
                    screens[Screen.current].update()
                    break
            Screen.switch_frame()
            self.parent.destroy()    
        
        
class EditScreen(tk.Frame):
    def __init__(self):
        Screen.__init__(self)
        self.edit_key = 0
        
        #Configure
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1) 
        self.grid_columnconfigure(3, weight = 1)  
        self.grid_columnconfigure(4, weight = 1) 
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 1)  
        self.grid_rowconfigure(2, weight = 1)
        self.grid_rowconfigure(3, weight = 1) 
        self.grid_rowconfigure(4, weight = 1)  
        self.grid_rowconfigure(5, weight = 1)
        self.grid_rowconfigure(6, weight = 1)   
        
        #Title
        self.lbl_screen_title = tk.Label(self, text = "Edit Screen", font = TITLE_FONT)
        self.lbl_screen_title.grid(row = 0, column = 0, columnspan=3, sticky = "new")
        
        #Input
        self.lbl_title = tk.Label(self,text = "Title: ")
        self.lbl_title.grid(row = 1, column = 0)
        self.ent_title = tk.Entry(self)
        self.ent_title.grid(row = 1, column = 1)
       
        self.lbl_genre = tk.Label(self,text = "Genre: ")
        self.lbl_genre.grid(row = 2, column = 0)  
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 2, column = 1)     
        
        self.lbl_dev = tk.Label(self,text = "Developer: ")
        self.lbl_dev.grid(row = 3, column = 0)  
        self.ent_dev = tk.Entry(self)
        self.ent_dev.grid(row = 3, column = 1)  
        
        self.lbl_pub = tk.Label(self, text = "Publisher: ")
        self.lbl_pub.grid(row = 4, column = 0)  
        self.ent_pub = tk.Entry(self)
        self.ent_pub.grid(row = 4, column = 1)           
        
        self.lbl_platform = tk.Label(self,text = "Platform: ")
        self.lbl_platform.grid(row = 5, column = 0)  
        self.ent_platform = tk.Entry(self)
        self.ent_platform.grid(row = 5, column = 1)          
        
        self.lbl_release = tk.Label(self,text = "  Release Date: ")
        self.lbl_release.grid(row = 1, column = 2)  
        self.ent_release = tk.Entry(self)
        self.ent_release.grid(row = 1, column = 3)               
        
        self.lbl_rate = tk.Label(self,text = "Rating: ")
        self.lbl_rate.grid(row = 2, column = 2)  
        self.ent_rate = tk.Entry(self)
        self.ent_rate.grid(row = 2, column = 3) 
        
        self.lbl_price = tk.Label(self,text = "Price: ")
        self.lbl_price.grid(row = 3, column = 2)  
        self.ent_price = tk.Entry(self)
        self.ent_price.grid(row = 3, column = 3)
        
        self.lbl_purchase = tk.Label(self,text ="  Purchase Date: ")
        self.lbl_purchase.grid(row = 4, column = 2)  
        self.ent_purchase = tk.Entry(self)
        self.ent_purchase.grid(row = 4, column = 3)
        
        #Drop Down
        self.lbl_mode = tk.Label(self,text = "Mode: ")
        self.lbl_mode.grid(row = 5, column = 2)          
        self.options = ["Singleplayer", "Multiplayer"] 
        self.dbx_mode = tk.StringVar(self)
        self.dbx_mode.set(self.options[0])
        self.menu = tk.OptionMenu(self, self.dbx_mode,*self.options)
        self.menu.grid(row=5,column=3,sticky="wns")
        
        self.cbx_beat = tk.Checkbutton(self, text = "Beaten?")
        self.cbx_beat.grid(row = 6, column = 2, sticky = "ws")
        
        #Notes
        self.lbl_notes = tk.Label(self,text = "Notes: ")
        self.lbl_notes.grid(row = 6, column = 1,sticky="ws")                
        self.scr_notes = ScrolledText(self,width=59,height=12)
        self.scr_notes.grid(row = 7, column = 0, columnspan = 4,sticky="news")    
        
        #Buttons
        self.btn_back = tk.Button(self,text = "Back", font = BOTTOM_FONT,command=self.go_back)
        self.btn_back.grid(row = 8, column = 0, sticky = "news")
        self.btn_clear = tk.Button(self,text = "Reset", font = BOTTOM_FONT,command=self.reset)
        self.btn_clear.grid(row = 8, column = 1, sticky = "news")
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT,command=self.go_confirm)
        self.btn_submit.grid(row = 8, column = 3, sticky = "news")     
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame() 
        
    def reset(self):
        print("Reset")    
        
    def go_confirm(self):
        Screen.current = 0
        Screen.switch_frame()      
        
    
        #Updateent_title
    def update(self):
        entry = games[self.edit_key]
        self.ent_title.delete(0, "end")
        self.ent_title.insert(0, entry[0])
        self.ent_genre.delete(0, "end")
        self.ent_genre.insert(0, entry[1])
        self.ent_dev.delete(0, "end")
        self.ent_dev.insert(0, entry[2])
        self.ent_pub.delete(0, "end")
        self.ent_pub.insert(0, entry[3])     
        self.ent_platform.delete(0, "end")
        self.ent_platform.insert(0, entry[4])
        self.ent_release.delete(0, "end")
        self.ent_release.insert(0, entry[5])
        self.ent_rate.delete(0, "end")
        self.ent_rate.insert(0, entry[6])        
        self.ent_price.delete(0, "end")
        self.ent_price.insert(0, entry[8])
        self.ent_purchase.delete(0, "end")
        self.ent_purchase.insert(0, entry[10])             
        
class SearchScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
        
        #Configure
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  
        self.grid_columnconfigure(2, weight = 1) 
        self.grid_columnconfigure(3, weight = 1)
        self.grid_rowconfigure(5,weight=1)

        #Title
        self.lbl_title = tk.Label(self,text = "Search", font = TITLE_FONT)
        self.lbl_title.grid(row = 0, column = 0, columnspan=3, sticky = "news") 
        
        #Print Filter
        self.lbl_filter = tk.Label(self,text = "Print Filter: ", font = BOTTOM_FONT)
        self.lbl_filter.grid(row = 1, column = 2, sticky = "nws")  

        
        #Search By
        self.lbl_srch_by = tk.Label(self,text = "Search By: ", font = BOTTOM_FONT)
        self.lbl_srch_by.grid(row = 1, column = 0, sticky = "nws")  
        self.ent_srch_by = tk.Entry(self)
        self.ent_srch_by.grid(row = 2, column = 0, sticky = "ws")
        
        #Search For
        self.lbl_srch_for = tk.Label(self,text = "Search For: ", font = BOTTOM_FONT)
        self.lbl_srch_for.grid(row = 3, column = 0, sticky = "nws")
        self.ent_srch_for = tk.Entry(self)
        self.ent_srch_for.grid(row = 4, column = 0, sticky = "nw") 
        
        #Scroll
        self.scr_print = ScrolledText(self,width=59,height=19)
        self.scr_print.grid(row = 5, column = 0, columnspan = 3,sticky="news")
        
        #Check Boxes
        checkbox_filter = CheckboxFilter(self)
        checkbox_filter.grid(row = 2, column = 1, rowspan = 3, columnspan = 2, sticky = "news")        
        
        #Buttons
        self.btn_back = tk.Button(self,text = "Back", font = BOTTOM_FONT,command=self.go_back)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")
        self.btn_clear = tk.Button(self,text = "Clear", font = BOTTOM_FONT,command=self.clear)
        self.btn_clear.grid(row = 6, column = 1, sticky = "news")
        self.btn_submit = tk.Button(self,text = "Submit", font = BOTTOM_FONT,command=self.submit)
        self.btn_submit.grid(row = 6, column = 2, sticky = "news")        
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame() 

    def clear(self):
        print("Cleared")    

    def submit(self):
        print("Submited")        
        
class CheckboxFilter(tk.Frame):
    def __init__(self, parent ):
        tk.Frame.__init__(self, master= parent)
        
        
        self.cbx_title = tk.Checkbutton(self, text = "Title")
        self.cbx_title.grid(row = 0, column = 0, sticky = "nws")
        
        self.cbx_genre = tk.Checkbutton(self, text = "Genre")
        self.cbx_genre.grid(row = 1, column = 0, sticky = "nws") 
        
        self.cbx_dev = tk.Checkbutton(self, text = "Developer")
        self.cbx_dev.grid(row = 2, column = 0, sticky = "nws") 
        
        self.cbx_pub = tk.Checkbutton(self, text = "Publisher")
        self.cbx_pub.grid(row = 3, column = 0, sticky = "nws") 
        
        self.cbx_platform = tk.Checkbutton(self,text = "Platform")
        self.cbx_platform.grid(row = 0, column = 1, sticky = "nws") 
        
        self.cbx_date = tk.Checkbutton(self, text = "Release Date")
        self.cbx_date.grid(row = 1, column = 1, sticky = "nws")
        
        self.cbx_rate = tk.Checkbutton(self, text = "Rating")
        self.cbx_rate.grid(row = 2, column = 1, sticky = "nws" )
        
        self.cbx_multi = tk.Checkbutton(self, text = "Single/Multi")
        self.cbx_multi.grid(row = 3, column = 1, sticky = "nws") 
        
        self.cbx_price = tk.Checkbutton(self, text = "Price")
        self.cbx_price.grid(row = 0, column = 2, sticky = "nws") 
        
        self.cbx_beat = tk.Checkbutton(self, text = "Beaten")
        self.cbx_beat.grid(row = 1, column = 2, sticky = "nws")         
        
        self.cbx_beat = tk.Checkbutton(self, text = "Purchase Date")
        self.cbx_beat.grid(row = 2, column = 2, sticky = "nws")            
        
        self.cbx_note = tk.Checkbutton(self, text = "Notes")
        self.cbx_note.grid(row = 3, column = 2, sticky = "nws")        
        
class RemoveScreen(Screen):
    def __init__(self):
        Screen.__init__(self) 
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  

        
        self.lbl_genre = tk.Label(self,text = "Which Game Would You Like To Remove? ", font = BOTTOM_FONT)
        self.lbl_genre.grid(row = 0, column = 0)  
        self.ent_genre = tk.Entry(self)
        self.ent_genre.grid(row = 1, column = 0)   
        
        #Buttons
        self.btn_clear = tk.Button(self,text = "Cancel", font = BOTTOM_FONT)
        self.btn_clear.grid(row = 3, column = 0)
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT)
        self.btn_submit.grid(row = 2, column = 0)            
        
class SaveScreen(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        self.lbl_save = tk.Label(self,text = "Library Saved ", font = BOTTOM_FONT)
        self.lbl_save.grid(row = 0, column = 0)
        self.btn_save = tk.Button(self,text = "Ok", font = BOTTOM_FONT)
        self.btn_save.grid(row = 2, column = 0)          
       
#Main
if __name__ == "__main__":

    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
    data_file.close()
    root = tk.Tk()
    root.title("Game Lib")_date
    root.geometry("500x500")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    screens = [MainMenu(),AddScreen(),SearchScreen(),EditScreen()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[0].tkraise()

    root.mainloop()

