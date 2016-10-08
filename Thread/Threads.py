import time
import threading
from threading import Thread
import queue

# Worker thread processing from queue
def worker(i):
    while True:
        item = workQ.get()
        if item is None:
            break
        print("Thread ", i, " Process item: ", item)
        workQ.task_done()


if __name__ == "__main__":

    workQ = queue.Queue()
    threads = []

    # Create source items
    sourceItems = []
    for i in range(10000):
        sourceItems.append("Test_"+str(i))

    # Create threads
    numWorkers = 5
    for i in range(numWorkers):
        t = threading.Thread(target=worker, args=(i,))
        t.start()
        threads.append(t)

    for item in sourceItems:
        workQ.put(item)

    for i in range(numWorkers):
        workQ.put(None)

