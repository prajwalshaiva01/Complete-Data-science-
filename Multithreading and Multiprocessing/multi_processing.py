## it create a process that run parallel



import multiprocessing

import time
def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"square:{i * i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"cube:{i * i * i}")

if __name__=="__main__":
    t=time.time()
    ## create 2 processes
    p1=multiprocessing.Process(target=square_number)
    p2=multiprocessing.Process(target=cube_number)

    ## start the processes
    p1.start()
    p2.start()

    ## wait and join
    p1.join()
    p2.join()

    finshed_time=time.time()-t
    print(finshed_time)