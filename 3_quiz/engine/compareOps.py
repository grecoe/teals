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

        if self.compare.value == CompareOp.eq.value:
            returnValue = self.getValue(self.left) == self.getValue(self.right)
        elif self.compare.value == CompareOp.lt.value:
            returnValue = self.getValue(self.left) < self.getValue(self.right)
        elif self.compare.value == CompareOp.lte.value:
            returnValue = self.getValue(self.left) <= self.getValue(self.right)
        elif self.compare.value == CompareOp.gt.value:
            returnValue = self.getValue(self.left) > self.getValue(self.right)
        elif self.compare.value == CompareOp.gte.value:
            returnValue = self.getValue(self.left) >= self.getValue(self.right)
        elif self.compare.value == CompareOp.opand.value:
            returnValue = self.getValue(self.left) and self.getValue(self.right)
        elif self.compare.value == CompareOp.opor.value:
            returnValue = self.getValue(self.left) or self.getValue(self.right)

        return returnValue

    def getPrintableVersion(self, obj):
        returnValue = obj
        if obj.__class__.__name__ == "Comparision":
            returnValue = "({})".format(obj.getStatement())
        elif obj.__class__.__name__ == "str":
            returnValue = "'" + obj + "'"

        return returnValue

    def getValue(self, obj):
        if obj.__class__.__name__ == "Comparision":
            return obj.executeStatement()
        return obj
