### Multithreading




import threading
import time

def print_number():
    for i in range (5):
        time.sleep(1)
        print(f"Number:{i}")

def print_latter():
    for latter in "abcde":
        time.sleep(1)
        print(f"Latter:{latter}")

## create a 2 thread
t1=threading.Thread(target=print_number)
t2=threading.Thread(target=print_latter)

t=time.time()
## start the thread
t1.start()
t2.start()

## wait for the thread to complete
t1.join()
t2.join()

finshed_time=time.time()-t
print(finshed_time)