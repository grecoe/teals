import os
from datetime import datetime


class Logger:

    @staticmethod
    def add_log(message, controller_log='controller.log'):
        """
        Very simple logger that just dumps out the message with a time stamp
        with append only. Careful this could create an enormous log.
        """
        output = "\n{}\t{}".format(str(datetime.now()), message)
        with open(controller_log, 'a') as log_file:
            log_file.writelines(output)

    @staticmethod
    def clear_log(max_size=102400, controller_log='controller.log'):
        """
        Checks the size of the log and renames it if it is already
        a certain size.
        """
        if os.path.exists(controller_log):
            size = os.path.getsize(controller_log)
            print("Log is {} bytes".format(size))
            if size >= max_size:
                os.remove(controller_log)
                Logger.add_log("Log file cleared on size...")
