"""
More on inheritance....

    Logic:
        A is a B
        B is a C

        Therefore
        A is a C

    Consider
        Rb13 (Redbull) is a Formula 1 car
        Formula 1 cars are fast

        Therefore RB13 is fast

    super()
        Gets you the instance of the inherited class
"""


class RootClass:
    def report_me(self):
        print("RootClass Checking In")

    def third_level(self):
        print("RootClass is the only one with third_level")


class IntermediateClass(RootClass):
    def report_me(self):
        super().report_me()
        print("IntermediateClass Checking In")

    def second_level(self):
        print("IntermediateClass is the only one with second_level")


class TopClass(IntermediateClass):
    def report_me(self):
        super().report_me()
        print("TopClass Checking In")


tc = TopClass()

# Show the full chain
tc.report_me()
# Show a fn from one level up
tc.second_level()
# Show a fn from two levels up
tc.third_level()