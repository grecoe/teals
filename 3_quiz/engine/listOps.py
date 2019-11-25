from enum import Enum

class ListOps(Enum):
    index = 1
    append = 2
    extend = 3
    pop = 4
    contains = 5

class Lists:

    def __init__(self, listname, list, listop, *args):
        self.listname = listname
        self.list = list
        self.listop = listop
        self.arguments = args

        self.switchLookup =  {
            1: "[{}]",
            2: "append({})",
            3: "extend({})",
            4: "pop({})",
            5: "in"
        }

    def getStatement(self):
        op = self.switchLookup[self.listop.value]
        
        returnValue = None
        if self.listop.value == 1:
            indexValues = None
            if len(self.arguments) > 1:
                indexValues = "{}:{}".format(self.arguments[0], self.arguments[1])
            else:
                indexValues = self.arguments[0]
            returnValue = self.listname + op.format(indexValues)
        elif self.listop.value == 2 or self.listop.value == 3:
            returnValue = self.listname + "." + op.format(self.arguments[0])
        elif self.listop.value == 4:
            returnValue = self.listname + "." + op.format('')
            if len(self.arguments) > 0:
                returnValue = self.listname + "." + op.format(self.arguments[0])
        elif self.listop.value == 5:
            returnValue = str(self.arguments[0]) + " in " + self.listname
                
        return returnValue


    def executeStatement(self):
        returnValue = None

        if self.listop.value == 1:
            if len(self.arguments) > 1:
                returnValue = self.list[int(self.arguments[0]) : int(self.arguments[1])]
            else:
                returnValue = self.list[int(self.arguments[0])]
        elif self.listop.value == 2:
            self.list.append(self.arguments[0])
            returnValue = self.list
        elif self.listop.value == 3:
            self.list.extend(self.arguments[0])
            returnValue = self.list
        elif self.listop.value == 4:
            if len(self.arguments) > 0:
                returnValue = self.list.pop(self.arguments[0])
            else:
                returnValue = self.list.pop()
        elif self.listop.value == 5:
            returnValue = self.arguments[0] in self.list
        return returnValue
