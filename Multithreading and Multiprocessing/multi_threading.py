### Multithreading
## When to use Multi Threading
###I/O-bound tasks: Tasks that spend more time waiting for I/O operations (e.g., file operations, network requests).
###  Concurrent execution: When you want to improve the throughput of your application by performing multiple operations concurrently.

import threading #library for multithreading
import time 

#two process to execute,if we execute it order wise that is print_number() and print_letters() , it will get processed as single threads.
#by utilising abiltiy to sleep we can exceute multithreading and proceed with next available thread in os to save time until the thread 1 is available again

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter: {letter}")

##create 2 threads
t1=threading.Thread(target=print_numbers)
t2=threading.Thread(target=print_letter)

t=time.time()
## start the thread , when one goes to sleep other t2 will start and vice versa
t1.start()
t2.start()

### Wait for the threads to complete and join to main base thread
t1.join()
t2.join()

finished_time=time.time()-t
print(finished_time)