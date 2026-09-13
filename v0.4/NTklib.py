import subprocess as sbp
import time as t
from SysFunc.NTkSysFunc import *
from GUIElements.NTkelm import *

class NorthTkinter:
    def __init__(self, VERIFICATION):
        self.log = Log()
        self.sck = StdCmdKit()
        self.dftgm = "400x500"
        self.dfttitle = "new app"
        def LogVerification():
            test = Log()
            test.logt("start initialization... ")
            t.sleep(1)
            test.logt(f"\"Log\" class manager status: self.log.status={test.status}")
            t.sleep(1)
        
        def InfoLog():
            LogDftConfiguration = f"--- default config ---\nwindow geometry: {self.dftgm}\nwindow title: {self.dfttitle}"
            self.log.logt(f"NTK default settings: \n{LogDftConfiguration}")
            t.sleep(3)
            self.log.logt("verification script work is finished...")
            t.sleep(1)

        def ColoramaVerification():
            try:
                from colorama import init, Fore
                init(autoreset=True)
                colorama_available = True
            except ImportError:
                colorama_available = False
            
            if colorama_available == True:
                from colorama import Fore
                t.sleep(1)
                status = Fore.GREEN + "is installed."
                print(f"\"ColoramaLib\" verification status: {status}")
                t.sleep(3)
            else:
                print("\"ColoramaLib\" is not installed...")
                t.sleep(0.5)
                print("starting autoinstalling protocol: ")
                t.sleep(0.5)
                print("------------------------------------")
                sbp.run("pip install colorama", shell=True)
                print("\ninstalling finished")
                print("------------------------------------")
        
        def CTkinterVerification():
            awalibe_status = False
            try:
                import customtkinter as ct
                awalibe_status = True
            except ImportError:
                def autoinstall_CTK():
                    print("------------------------------------")
                    sbp.run("pip install customtkinter", shell=True)
                    print("\ninstalling finished")
                    print("------------------------------------")
                autoinst = autoinstall_CTK
                error = "is not supported."
                t.sleep(1)
                self.log.logt(f"\"CTklib\" support status: {error}")
                t.sleep(1)
                self.log.logt("starting autoinstalling protocol: ")
                t.sleep(0.5)
                autoinst()
                
            if awalibe_status == True:
                t.sleep(1)
                self.log.logt(f"\"CTklib\" support status: is supported.")
                t.sleep(1)

        self.InstallCommandList = [
            LogVerification,
            ColoramaVerification,
            CTkinterVerification,
            InfoLog
        ]

        def verification_loop():
            for i in range(0, len(self.InstallCommandList)):
                self.InstallCommandList[i]()

        # Инициализируем логгер до проверок, чтобы он работал внутри них
        self.log = Log()

        if VERIFICATION == 1:
            verification_loop()
        elif VERIFICATION == 0:
            pass

        # <--- ПРАВКА 1: Теперь мы импортируем сторонние библиотеки ТОЛЬКО ПОСЛЕ того, как они скачаются
        global ct, Fore, init
        import customtkinter as ct
        from colorama import init, Fore
        init(autoreset=True)
        
        # --- Твоя родная инициализация элементов окна ---
        self.sck = StdCmdKit()
        self.dftgm = "400x500"
        self.dfttitle = "new app"
        self.main = ct.CTk()
        self.elm = NTkEm()
        self.main.geometry(self.dftgm)
        self.main.title(self.dfttitle)

        def on_closing():
            self.main.quit()     # Мягко останавливает главный цикл окна (mainloop)
            self.main.destroy()  # Уничтожает окно и отменяет все фоновые таймеры
            import os
            os._exit(0)          # Полностью гасит программу вместе с консолью

        # Привязываем функцию к кнопке закрытия окна (красный крестик)
        self.main.protocol("WM_DELETE_WINDOW", on_closing)

    def ntkcml(self):
        ConsoleOn = True
        def NtkStartText():
            init(autoreset=True)
            text = r"""
         _   _ _____ _  ______ __  __ ____  
        | \ | |_   _| |/ / ___|  \/  |  _ \ 
        |  \| | | | | ' / |   | |\/| | | | |
        | |\  | | | | . \ |___| |  | | |_| |
        |_| \_| |_| |_|\_\____|_|  |_|____/

        fullname: NorthTkinterLib (NTkLib)
        default_name: NorthTkinter (NTk)

        project_owner: North

        version: v0.1 (pre-alpha)""" + "\n"
            print(Fore.GREEN + text)
        NtkStartText()
        
        def ConsoleHandler(userinput):
            if userinput == "conf":
                self.ntkcnf()
            elif userinput == "start":
                self.infloop()
            elif userinput == "cls":
                self.sck.cls()
            elif userinput == "exit": # <--- ПРАВКА 2: Убрал .lower() у самой строки, теперь выход сработает
                return 0
            else:
                return 1
                
        while ConsoleOn == True:
            user = input("<NTk.Cml>: ")
            answer = ConsoleHandler(user)
            if answer == 0:
                ConsoleOn = False
            elif answer == 1:
                print(Fore.RED + "error: unknown command")
                
    def ntkcnf(self):
        w = input("window width: ")
        h = input("window height: ")
        title = input("window app title: ")
        full = w + "x" + h
        self.main.geometry(full)
        self.main.title(title)
        
    def Frame(self, element, name):
        if element == "Lb":
            lb = Lb(name)
            lb.load()
            lb.build()
        elif element == "Btn":
            btn = Btn(name)
            btn.load()
            btn.build()
            
    def FrameLoop(self):
        self.elm.Launch()
        
    def infloop(self):
        self.main.mainloop()
        
    def SetDflFunc(self, args):
        if args == "cmd":
            self.ntkcml()
        elif args == "old":
            self.infloop()
        else:
            pass