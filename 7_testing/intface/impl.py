from iface import Distractor

dum_string = ' string value '

class MyImp(Distractor):
    def __init__(self):
        super().__init__()

    def func(self, p1):
        print("MyImp", p1)
