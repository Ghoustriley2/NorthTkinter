import customtkinter as ct

class StackV2:
    def __init__(self):
        self.mem = {
            "fullstack": {},
            "manualstack": {
                "names": [],
                "pos": []
            }
        }
    def _malloc(self, arr):
        for i, name in enumerate(arr):
            self.mem["manualstack"]["names"].append(name)
            self.mem["manualstack"]["pos"].append(i)
    def _falloc(self, arr):
        for i, cell_name in enumerate(arr["values"]):
            self.mem["fullstack"][cell_name] = i
    def _stackout(self, stacktype):
        if stacktype == "full":
            print(f"fullstack: {self.mem['fullstack'].items()}")
        elif stacktype == "manual":
            print(f"manualstack: {self.mem['manualstack'].items()}")

class StackArr(StackV2):
    def __init__(self):
        super().__init__()

class NTkASM():
    def __init__(self):
        self.freepos = 1
        self.v2 = StackArr()
    def DEB(func):
        def wrapper(self, *args, **kwargs):
            try:
                return func(self, *args, **kwargs)
            except (TypeError, KeyError) as e:
                print(f"{e}: {self.v2.mem['fullstack']}")
        return wrapper
        
    def ADD(self, name, pos):
        self.v2.mem["fullstack"][name] = pos
        self.freepos += 1  # <--- МАГИЧЕСКАЯ СТРОЧКА 1: сдвигаем позицию
        
    def REM(self, name):
        del self.v2.mem["fullstack"][name]
    @DEB
    def OUT(self, name):
        key = name; value = self.v2.mem['fullstack'][key]
        print(f"{key}: {value}")