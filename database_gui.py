#!/usr/bin/python3
# Matthew Buckmaster
# 2/10/2020

"""GUI version of game_database.py"""

import pickle

import tkinter as tk

from tkinter.scrolledtext import ScrolledText

from tkinter import messagebox as mb

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
        screens[Screen.current].clear()
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
        Screen.current = 4
        Screen.switch_frame()    
        
    def go_save(self):
        Screen.current = 5
        Screen.switch_frame()  
        
    def clear(self):
        self.ent_title.delete(0, "end")
        self.ent_genre.delete(0, "end")
        self.ent_dev.delete(0, "end")
        self.ent_pub.delete(0, "end")
        self.ent_platform.delete(0, "end")
        self.ent_release.delete(0, "end")
        self.ent_rate.delete(0, "end") 
        self.ent_price.delete(0, "end")
        self.ent_purchase.delete(0, "end")            


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
        self.btn_clear = tk.Button(self,text = "Clear", font = BOTTOM_FONT,command=self.clear)
        self.btn_clear.grid(row = 8, column = 1, sticky = "news")
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT,command=self.go_confirm)
        self.btn_submit.grid(row = 8, column = 3, sticky = "news")     
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()
        
        
    def clear(self):
        self.ent_title.delete(0, "end")
        self.ent_genre.delete(0, "end")
        self.ent_dev.delete(0, "end")
        self.ent_pub.delete(0, "end")
        self.ent_platform.delete(0, "end")
        self.ent_release.delete(0, "end")
        self.ent_rate.delete(0, "end") 
        self.ent_price.delete(0, "end")
        self.ent_purchase.delete(0, "end")            
            
        
    def go_confirm(self):
        Screen.current = 0
        Screen.switch_frame()  
        entry = []
        entry.append(self.ent_title.get())
        entry.append(self.ent_genre.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_platform.get())
        entry.append(self.ent_release.get())
        entry.append(self.ent_rate.get())
        entry.append(self.dbx_mode.get())
        entry.append(self.ent_price.get())
        entry.append("")
        entry.append(self.ent_purchase.get())
        entry.append(self.scr_notes.get(0.0, "end"))
        games[len(games)+1] = entry
        mb.showinfo(message = "Entry has been added")

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
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT,command=self.confirm)
        self.btn_submit.grid(row = 8, column = 3, sticky = "news")     
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame() 
        
    def reset(self):
        print("Reset")    
        
    def confirm(self):
        Screen.current = 0 
        Screen.switch_frame()
        entry = []
        entry.append(self.ent_title.get())
        entry.append(self.ent_genre.get())
        entry.append(self.ent_dev.get())
        entry.append(self.ent_pub.get())
        entry.append(self.ent_platform.get())
        entry.append(self.ent_release.get())
        entry.append(self.ent_rate.get())
        entry.append(self.dbx_mode.get())
        entry.append(self.ent_price.get())
        entry.append("")
        entry.append(self.ent_purchase.get())
        entry.append(self.scr_notes.get(0.0, "end"))
        games[self.edit_key] = entry
        
    
        
    
        #Update
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
        self.checkbox_filter = CheckboxFilter(self)
        self.checkbox_filter.grid(row = 2, column = 1, rowspan = 3, columnspan = 2, sticky = "news")        
        
        #Buttons
        self.btn_back = tk.Button(self,text = "Back", font = BOTTOM_FONT,command=self.go_back)
        self.btn_back.grid(row = 6, column = 0, sticky = "news")
        self.btn_clear = tk.Button(self,text = "Clear", font = BOTTOM_FONT,command=self.clear)
        self.btn_clear.grid(row = 6, column = 1, sticky = "news")
        self.btn_submit = tk.Button(self,text = "Submit", font = BOTTOM_FONT,command=self.submit_search)
        self.btn_submit.grid(row = 6, column = 2, sticky = "news") 
        
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame() 

    def clear(self):
        self.checkbox_filter.title_filter.set(False)  
        self.checkbox_filter.genre_filter.set(False) 
        self.checkbox_filter.dev_filter.set(False) 
        self.checkbox_filter.pub_filter.set(False) 
        self.checkbox_filter.platform_filter.set(False) 
        self.checkbox_filter.release_filter.set(False)
        self.checkbox_filter.rate_filter.set(False)
        self.checkbox_filter.multi_filter.set(False) 
        self.checkbox_filter.price_filter.set(False)  
        self.checkbox_filter.beat_filter.set(False) 
        self.checkbox_filter.purchase_filter.set(False) 
        self.checkbox_filter.note_filter.set(False) 
             
    def filter_print(self, entry):
        if self.checkbox_filter.title_filter.get() == True:
            msg = entry[0]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.genre_filter.get() == True:
            msg = entry[1]+"\n"
            self.scr_print.insert("insert", msg)   
        if self.checkbox_filter.dev_filter.get() == True:
            msg = entry[2]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.pub_filter.get() == True:
            msg = entry[3]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.platform_filter.get() == True:
            msg = entry[4]+"\n"
            self.scr_print.insert("insert", msg)   
        if self.checkbox_filter.release_filter.get() == True:
            msg = entry[5]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.rate_filter.get() == True:
            msg = entry[6]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.multi_filter.get() == True:
            msg = entry[7]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.price_filter.get() == True:
            msg = entry[8]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.beat_filter.get() == True:
            msg = entry[9]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.purchase_filter.get() == True:
            msg = entry[10]+"\n"
            self.scr_print.insert("insert", msg)
        if self.checkbox_filter.note_filter.get() == True:
            msg = entry[11]+"\n"
            self.scr_print.insert("insert", msg)
            
            
    def submit_search(self):
        self.scr_print.delete(0.0, "end")
        for key in games.keys():
            entry = games[key]
            self.filter_print(entry)
                
                
class CheckboxFilter(tk.Frame):
    def __init__(self, parent ):
        tk.Frame.__init__(self, master= parent)
        
        self.title_filter = tk.BooleanVar()
        self.title_filter.set(True)
        self.cbx_title = tk.Checkbutton(self, text = "Title", variable = self.title_filter )
        self.cbx_title.grid(row = 0, column = 0, sticky = "nws")
        
        self.genre_filter = tk.BooleanVar()
        self.genre_filter.set(True)        
        self.cbx_genre = tk.Checkbutton(self, text = "Genre", variable = self.genre_filter )
        self.cbx_genre.grid(row = 1, column = 0, sticky = "nws") 
        
        self.dev_filter = tk.BooleanVar()
        self.dev_filter.set(True)        
        self.cbx_dev = tk.Checkbutton(self, text = "Developer", variable = self.dev_filter )
        self.cbx_dev.grid(row = 2, column = 0, sticky = "nws") 
        
        self.pub_filter = tk.BooleanVar()
        self.pub_filter.set(True)        
        self.cbx_pub = tk.Checkbutton(self, text = "Publisher", variable = self.pub_filter )
        self.cbx_pub.grid(row = 3, column = 0, sticky = "nws") 
        
        self.platform_filter = tk.BooleanVar()
        self.platform_filter.set(True)        
        self.cbx_platform = tk.Checkbutton(self,text = "Platform", variable = self.platform_filter )
        self.cbx_platform.grid(row = 0, column = 1, sticky = "nws") 
        
        self.release_filter = tk.BooleanVar()
        self.release_filter.set(True)        
        self.cbx_date = tk.Checkbutton(self, text = "Release Date", variable = self.release_filter )
        self.cbx_date.grid(row = 1, column = 1, sticky = "nws")
        
        self.rate_filter = tk.BooleanVar()
        self.rate_filter.set(True)        
        self.cbx_rate = tk.Checkbutton(self, text = "Rating", variable = self.rate_filter )
        self.cbx_rate.grid(row = 2, column = 1, sticky = "nws" )
        
        self.multi_filter = tk.BooleanVar()
        self.multi_filter.set(True)        
        self.cbx_multi = tk.Checkbutton(self, text = "Single/Multi", variable = self.multi_filter )
        self.cbx_multi.grid(row = 3, column = 1, sticky = "nws") 
        
        self.price_filter = tk.BooleanVar()
        self.price_filter.set(True)        
        self.cbx_price = tk.Checkbutton(self, text = "Price", variable = self.price_filter )
        self.cbx_price.grid(row = 0, column = 2, sticky = "nws") 
        
        self.beat_filter = tk.BooleanVar()
        self.beat_filter.set(True)        
        self.cbx_beat = tk.Checkbutton(self, text = "Beaten", variable = self.beat_filter )
        self.cbx_beat.grid(row = 1, column = 2, sticky = "nws")         
        
        self.purchase_filter = tk.BooleanVar()
        self.purchase_filter.set(True)        
        self.cbx_purchase = tk.Checkbutton(self, text = "Purchase Date", variable = self.purchase_filter )
        self.cbx_purchase.grid(row = 2, column = 2, sticky = "nws")            
        
        self.note_filter = tk.BooleanVar()
        self.note_filter.set(True)        
        self.cbx_note = tk.Checkbutton(self, text = "Notes", variable = self.note_filter )
        self.cbx_note.grid(row = 3, column = 2, sticky = "nws")        
        
class RemoveScreen(Screen):
    def __init__(self):
        Screen.__init__(self) 
        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 1)  

        
        self.lbl_genre = tk.Label(self,text = "Which Game Would You Like To Remove? ", font = BOTTOM_FONT)
        self.lbl_genre.grid(row = 0, column = 0,columnspan=2)  

        self.lbl_mode = tk.Label(self,text = "Game List: ")
        self.lbl_mode.grid(row = 1, column = 0, sticky = "news") 
        self.options = ["Select a Title"]
        for key in games.keys():
            self.options.append(games[key][0])
        self.tkvar = tk.StringVar(self)
        self.tkvar.set(self.options[0])        
        self.menu = tk.OptionMenu(self, self.tkvar,*self.options)
        self.menu.grid(row=1,column=1, sticky = "wesn")         
        
        #Buttons
        self.btn_clear = tk.Button(self,text = "Cancel", font = BOTTOM_FONT, command = self.go_back)
        self.btn_clear.grid(row = 2, column = 0)
        self.btn_submit = tk.Button(self,text = "Confirm", font = BOTTOM_FONT)
        self.btn_submit.grid(row = 2, column = 1)    
        
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()         
        
class SaveScreen(Screen):
    def __init__(self):
        Screen.__init__(self)    
        
        self.lbl_save = tk.Label(self,text = "Library Saved ", font = BOTTOM_FONT)
        self.lbl_save.grid(row = 0, column = 0)
        self.btn_save = tk.Button(self,text = "Ok", font = BOTTOM_FONT,command=self.go_back)
        self.btn_save.grid(row = 2, column = 0)          
       
    def go_back(self):
        Screen.current = 0
        Screen.switch_frame()        
       
#Main
if __name__ == "__main__":

    data_file = open("game_lib.pickle", "rb")
    games = pickle.load(data_file)
    data_file.close()
    root = tk.Tk()
    root.title("Game Lib")
    root.geometry("500x500")
    root.grid_columnconfigure(0, weight = 1)
    root.grid_rowconfigure(0, weight = 1)    
    screens = [MainMenu(),AddScreen(),SearchScreen(),EditScreen(), RemoveScreen(),SaveScreen()]
    screens[0].grid(row = 0, column = 0, sticky = "news")
    screens[1].grid(row = 0, column = 0, sticky = "news")
    screens[2].grid(row = 0, column = 0, sticky = "news")
    screens[3].grid(row = 0, column = 0, sticky = "news")
    screens[4].grid(row = 0, column = 0, sticky = "news")
    screens[5].grid(row = 0, column = 0, sticky = "news")    
    screens[0].tkraise()

    root.mainloop()