import importlib
from utils.tracer import TraceDecorator, Logger


@TraceDecorator
def load_module(module_name, entry_point):
    Logger.add_log("Load module {} for entry point {}".format(module_name, entry_point))

    game_entry = None
    try:
        game_module = importlib.import_module(module_name)
        game_entry = getattr(game_module, entry_point)
    except Exception as ex:
        Logger.add_log("load_module failed ({},{}) - {}".format(entry_point, module_name, str(ex)))

    return game_entry
