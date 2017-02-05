from multiprocessing import Process
import time

def f(name):
    while True:
        print(name)
def g(name):
    while True:
        print(name)

if __name__ == '__main__':

    p = Process(target=f, args=(None,))
    q = Process(target=g, args=(None,))

    p.start()
    q.start()
    time.sleep(5)
    p.terminate()
    p.join()
    q.join()
    time.sleep(3)
