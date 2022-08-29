from threading import Thread, Semaphore

class Foo:
    def __init__(self):
        self.sem1 = Semaphore()
        self.sem2 = Semaphore()
        self.sem1.acquire()
        self.sem2.acquire()

    def first(self) -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.sem1.release()


    def second(self) -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.sem1.acquire()
        printSecond()
        self.sem2.release()


    def third(self) -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.sem2.acquire()
        printThird()
    
def printFirst():
    print('first', end='')

def printSecond():
    print('second', end='')

def printThird():
    print('third')

a = Foo()
p_dict = {1: a.first, 2: a.second, 3: a.third}
list_of_nums = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
for nums in list_of_nums:
    threads = []
    for n in nums:
        t = Thread(target=p_dict[n])
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    del threads
