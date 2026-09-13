import customtkinter as ct
import NTkmem as mem
from SysFunc.NTkSysFunc import *

class NTkEm:
    def __init__(self):
        self.v2 = mem.StackV2()
        self.asm = mem.NTkASM()
        self.memarr = mem.StackArr()
        # self.main = ct.CTk() <--- МАГИЧЕСКАЯ ПРАВКА 2: удаляем или комментируем, чтобы не плодить окна
        
    def Launch(self):
        pass # mainloop уже крутится в app.py (self.infloop), оставляем пустым

class Lb(NTkEm):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.text = "example text"
        self.text_color = "red"
        self.font = ("arial", 16)
        self.lb = ct.CTkLabel(
            # master=self.main, <--- Просто убираем эту строку, CustomTkinter сам найдет окно!
            text=self.text,
            text_color=self.text_color,
            font=self.font
        )
    def load(self):
        self.asm.ADD(self.name, self.asm.freepos)
    def build(self):
        self.lb.pack()

class Btn(NTkEm):
    def __init__(self, name):
        super().__init__()
        self.text = "Click me"
        self.name = name
        def example_command():
            print("command \"example_command()\": hello world")
        self.command = example_command
        self.fg_color = "red"
        self.hover_color = "blue"
        self.corner_radius = 5
        self.btn = ct.CTkButton(
            # master=self.main, <--- Убираем строку здесь тоже
            text=self.text,
            command=self.command,
            fg_color=self.fg_color,
            hover_color=self.hover_color,
            corner_radius=self.corner_radius
        )
    def load(self):
        self.asm.ADD(self.name, self.asm.freepos)
    def build(self):
        self.btn.pack()