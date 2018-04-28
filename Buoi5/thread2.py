import threading
import time

class MyThread(threading.Thread):

    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name     = name
        self.counter  = counter

    def run(self):
        print('Starting: ' + self.name)
        print_time(self, threadName = self.name, delay = self.counter, counter = 5)
        print('Existing ' + self.name)

def print_time(self, threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s: %s' %(threadName, time.ctime(time.time())))
        counter -= 1

thread1 = MyThread(1, 'Thread 01', 1)
thread2 = MyThread(2, 'Thread 02', 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('Existing main thread')