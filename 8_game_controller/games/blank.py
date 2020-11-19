"""
Empty game....example on how to create one and how to mark it. Look into the gameconfig.json
file to see how this is added to the main app.
"""

# Include the logger so we can output from here as well
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def play():
    print("This game does nothing!")
    Logger.add_log("Just a dummy entry")
