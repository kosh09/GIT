

# Import internal modules
import concurrent.futures as cf
import time

def Hello():
    while True:
        return 45
def Print():
    while True:
        print(data)
def Return():
    while True:
        data = Hello()

with cf.ThreadPoolExecutor(max_workers=2) as ex:
    ex.submit(Return)
    ex.submit(Print)
