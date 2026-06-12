###  Multiprocessing with ProcessPoolExecutor-this will use all cores of my cpu

from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(2)
    return f"Square: {number * number}"

numbers=[1,2,3,4,5,6,7,8,9,11,2,3,12,14]
#defining the starting point  
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(square_number,numbers)

    for result in results:
        print(result)