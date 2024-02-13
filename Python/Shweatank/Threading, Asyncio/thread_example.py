'''
import threading
import time

def say_hello(name, nsc):
    print("hello from "+name)
    time.sleep(nsc)
    print(name + " slept %d seconds" % nsc)
    
print("Starting three threads!")
threading._start_new_thread(say_hello, ("1st thread", 3))
threading._start_new_thread(say_hello, ("2nd thread", 2))
threading._start_new_thread(say_hello, ("3rd thread", 1))
time.sleep(4)
print("Done!")


import thread6
import time
@thread6.threaded()
def say_hello(name,nsc):
    # says hello and sleeps n seconds 
    print ('hello from ' + name)
    time.sleep(nsc)
    print(name + 'slept %d seconds' % nsc)
print("starting three threads")
First = say_hello('Bob',4)
Second = say_hello('Dylan',2)
Third = say_hello('Rob',1)

'''

'''
import logging
import threading
import time
def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main : before running thread")
    x.start()
    logging.info("Main : wait for the thread to finish")
    # x.join()
    logging.info("Main : all done")
'''

'''
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    threads = list()
    for index in range(3):
        logging.info("Main : create and start thread %d", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
        
    for index, thread in enumerate(threads):
        logging.info("Main : before joining thread %d", index)
        thread.join()
        logging.info("Main : thread %d done", index)
        
        
import threading
import time
class myThread (threading.Thread):

    def __init__(self, threadID, name, counter):

        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):

        print ("Starting " + self.name)

        # Get lock to synchronize threads

        threadLock.acquire()

        print_time(self.name, self.counter, 3)

        # Free lock to release next thread

        threadLock.release()

def print_time(threadName, delay, counter):

    while counter:

        time.sleep(delay)

        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

threadLock = threading.Lock()

threads = []

# Create new threads

thread1 = myThread(1, "Thread-1", 1)

thread2 = myThread(2, "Thread-2", 2)

# Start new Threads

thread1.start()

thread2.start()

# Add threads to thread list

threads.append(thread1)

threads.append(thread2)

# Wait for all threads to complete

for t in threads:

    t.join()

    print("Exiting Main Thread")
    
'''

'''
#!/usr/bin/python
import queue
import threading
import time
exitFlag = 0
class myThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("Starting " + self.name)
        process_data(self.name, self.q)
        print ("Exiting " + self.name)

def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = q.get()
            queueLock.release()
            print ("%s processing %s" % (threadName, data))
        else:
            queueLock.release()
            time.sleep(1)

threadList = ["Thread-1", "Thread-2", "Thread-3"]           
nameList = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
# Create new threads
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1
# Fill the queue
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()
# Wait for queue to empty
while not workQueue.empty():
    pass
# Notify threads it's time to exit
exitFlag = 1
# Wait for all threads to complete
for t in threads:
    t.join()
    print ("Exiting Main Thread")

'''

'''
import asyncio
import time
async def cor1():
    print("Cor 1 started")

    for i in range(5):
        await asyncio.sleep(1.5)
        print("Cor1", i)

async def cor2():
    print("Cor 2 started")

    for i in range(8):
        await asyncio.sleep(1)
        print("Cor2", i)

loop = asyncio.get_event_loop()
cors = asyncio.wait([cor1(), cor2()])
loop.run_until_complete(cors)

'''

'''
import asyncio
import time
async def main():
    # Using asyncio.create_task() method to create a task    
    task1 = asyncio.create_task(foo('task 1'))
    task2 = asyncio.create_task(foo('task 2'))
    print("started at", time.strftime('%X'))
    # Wait until both tasks are completed    
    await task1
    await task2
    print("finished at", time.strftime('%X'))
async def foo(text):
    print(text)
    await asyncio.sleep(1)

asyncio.run(main())
'''

'''
import asyncio

async def printing(task, text):
    while True:
        print(task, text)
        
        try: 
            await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            break
        
async def main():
    try:
        await asyncio.wait_for(
            asyncio.gather(
                printing("A", "Message"),
                printing("B", "Message"),
                printing("C", "Message")
        ), 3)
        
    except asyncio.TimeoutError:
        print("Time Over")
        
asyncio.run(main())
'''


        

