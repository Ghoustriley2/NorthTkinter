from colorama import init, Fore, Back, Style
import subprocess as sbp
import time

class StdCmdKit:
    # (Твой оригинальный код StdCmdKit без изменений)
    def __init__(self):
        self.StdCmdBase = {
            "cmdargs": {},
            "pip": {
                "commands": {"pip": "pip", "py": "py"},
                "pip_op": {"install": "install", "uninstall": "uninstall", "update": "update"},
                "args": {"read_mode": "/r"}
            },
            "commands": {"cls": "cls", "echo": "echo", "mkdir": "mkdir", "rmdir": "rmdir"}
        }
    @staticmethod
    def cls():
        sbp.run("cls", shell=True)

class Log:
    def __init__(self):
        init(autoreset=True)
        self.dftdsc = "ntklog"
        self.on = True
        self.iterate = 0
        self.status = Fore.GREEN + "supported"
    def logt(self, log):
        print(f"{self.dftdsc}: {log}")
    def auto(self, log):
        i = self.iterate
        while self.on:
            print(log[i])
            # <--- МАГИЧЕСКАЯ СТРОЧКА 3: двигаем индекс, чтобы цикл не завис
            i += 1 
            if i >= len(log):
                break