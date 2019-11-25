from enum import Enum

class CompareOp(Enum):
    eq = 1
    lt = 2
    lte = 3
    gt = 4
    gte = 5
    opand = 6
    opor = 7

class Comparision:

    def __init__(self, left, right, compareOp):
        self.left = left
        self.right = right
        self.compare = compareOp

        self.switchLookup =  {
            1: "==",
            2: "<",
            3: "<=",
            4: ">",
            5: ">=",
            6: "and",
            7: "or"
        }

    def getStatement(self):
        op = self.switchLookup[self.compare.value]
        return "{} {} {}".format(self.getPrintableVersion(self.left), op, self.getPrintableVersion(self.right))

    def executeStatement(self):
        returnValue = None

        if self.compare.value == 1:
            returnValue = self.getValue(self.left) == self.getValue(self.right)
        elif self.compare.value == 2:
            returnValue = self.getValue(self.left) < self.getValue(self.right)
        elif self.compare.value == 3:
            returnValue = self.getValue(self.left) <= self.getValue(self.right)
        elif self.compare.value == 4:
            returnValue = self.getValue(self.left) > self.getValue(self.right)
        elif self.compare.value == 5:
            returnValue = self.getValue(self.left) >= self.getValue(self.right)
        elif self.compare.value == 6:
            returnValue = self.getValue(self.left) and self.getValue(self.right)
        elif self.compare.value == 7:
            returnValue = self.getValue(self.left) or self.getValue(self.right)

        return returnValue

    def getPrintableVersion(self, obj):

        if obj.__class__.__name__ == "Comparision":
            return "({})".format(obj.getStatement())
        
        return obj

    def getValue(self, obj):
        if obj.__class__.__name__ == "Comparision":
            return obj.executeStatement()
        return obj
