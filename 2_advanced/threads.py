'''
    Threading, in most languages, allows you to process more data faster. A thread 
    has it's own execution context and acts as something like another program within 
    your program. 

    In python you need to wait for a thread to complete. You can do this in one of 
    two ways. 

    1. Join the thread to the main thread
    2. Track thread completion

    Python is a little different in that if we join the threads, they seem to run 
    synchronously. If we do not join the main thread, they will run asyncrhonously. 
'''

from threading import *
from datetime import datetime, timedelta
import time

# Keep track of threads completed, will be used if not using join()
threadsCompleteCount = 0
# How many threads to start
threadsStarted = 2
# How many messages a thread should print
iterations = 5
# Flag used to determine if a thread joins the main thread.
joinThread = True

class Notification(Thread):

    def __init__(self, id, iterations):
        Thread.__init__(self)
        self.id = id
        '''
            Locks are important in threaded programming as they allow us to "lock" an 
            object to ensure that only one thread instance can access protected code. 
        '''
        self.lock = RLock()
        # How many times we want to print somethign out. 
        self.iterations = iterations

        self.message = "Thread ID " + str(self.id) + " : reporting"

    '''
        run

        Because this class derives from Thread, calling Thread.start() will execute this method.
        However, it is just a method that can be called, so we will distinguish between using threads or 
        not based on how we access this method. 

        Note that internally we are acquiring a releasing a lock even though there is no shared
        object we are protecting...it is simply for completeness of the example. 
    '''
    def run(self):
        # Global thread count to be used when NOT joining main thread.
        global threadsCompleteCount

        for i in range(self.iterations):

            self.lock.acquire()

            print("NOTIFY: " + self.message)

            self.lock.release()

            # Make the thread wait a little bit
            time.sleep(0.1)
        
        # Increment global count, just in case. 
        threadsCompleteCount += 1


'''
    Program Code

    Create the threads and start them. If the joinThread flag is set, have them 
    join the main thread. 
'''
for i in range(threadsStarted):
    notifyT = Notification(i, iterations)
    notifyT.start()
    if joinThread :
        notifyT.join()

'''
    If we did NOT join the main thread, then we need to wait until the 
    threads report being done.
'''
if not joinThread:
    while threadsCompleteCount != threadsStarted:
        time.sleep(1)


print("All ", threadsCompleteCount, " instances are complete. " )
