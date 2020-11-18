from utils.logger import Logger


class TraceDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):

        return_value = None

        out_message_base = "Function: {}, Module: {} ".format(
            self.function.__name__,
            self.function.__module__)

        Logger.add_log("ENTER {}".format(out_message_base))

        try:
            return_value = self.function(*args, **kwargs)
        except Exception as ex:
            Logger.add_log("EXCEPTION {} - {}".format(out_message_base, str(ex)))

        Logger.add_log("EXIT {} - returns {} ".format(out_message_base, return_value))

        return return_value
