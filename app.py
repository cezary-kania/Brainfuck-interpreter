import tkinter as tk
from tkinter import filedialog
import os
from tkinter import ttk

from Interpreter import Interpreter 


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.minsize(600,400)
        self.master.title("Brainfuck interpreter by Cezary Kania v 0.1")
        self.interpreter = Interpreter(self)
        self.init_menu()
        self.init_body()
        self.pack()
        
    
    def init_menu(self):
        menubar = tk.Menu(self)
        menubar.add_command(label = "Open File", command = self.get_file_data)
        self.master.configure(menu = menubar) 
    def init_body(self):
        self.code_text_box = tk.Text(self.master, height='35', width='50')
        self.code_text_box.pack(side = 'left')
        self.result_text_box = tk.Text(self.master, height='35', width='50', state='disabled')
        self.result_text_box.pack(side = 'right')
        self.run_btn = tk.Button(self.master, text='Run', command = self.execCode)
        self.run_btn.pack(side='bottom')
    def get_file_data(self):
        file = filedialog.askopenfilename(initialdir=os.getcwd(), title = 'Select code file', filetypes=(('bf files','*.bf'),))
        with open(file, 'r') as f:
            self.code_text_box.insert(tk.END,f.readlines())
    
    def fetchAscii(self, chr):
        self.result_text_box.configure(state='normal')
        self.result_text_box.insert('end', chr)
        self.result_text_box.configure(state='disabled')

    def execCode(self):
        code = Interpreter.ParseString(self.code_text_box.get('1.0',"end-1c"))
        if len(code) > 0:
            self.interpreter.Run(code)
if __name__ == "__main__":
    window = tk.Tk()
    app = Application(window)
    app.mainloop()
