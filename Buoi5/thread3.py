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
        threadLock.acquire()
        print_time(self, threadName = self.name, delay = self.counter, counter = 5)
        print('Existing ' + self.name)
        threadLock.release()

def print_time(self, threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print('%s: %s' %(threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()
threads    = []
thread1 = MyThread(1, 'Thread 01', 1)
thread2 = MyThread(2, 'Thread 02', 2)
# Start new thread
thread1.start()
thread2.start()

# Add thread to threads list
threads.append(thread1)
threads.append(thread2)


for t in threads:
    t.join()

print('Existing main thread')