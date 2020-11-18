"""
TicTacToe Outline
"""

# Include the logger so we can output from here as well
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def play():
    print("This game does nothing!")
    Logger.add_log("Just a dummy entry")
