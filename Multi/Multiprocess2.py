# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:11:45 2022

@author: jdemt
"""
#https://www.youtube.com/watch?v=Tu0KbXWr5uA&list=PLNmsVeXQZj7q0ao69AIogD94oBgp3E9Zs&index=36

# TODO umbau . gleiche logik aber mit threads

import multiprocessing
import math

def factorize(num):
    res = []
    i = 2
    while True:
        if num == 1:
            return res
        
        rest = num % i
        
        if rest == 0:
            res.append(i)
            num = num // i
        else:
            i = i + 1


def mp_worker(queue, numbers):
    result = {}
    for i in numbers:
        result[i] = factorize(i)
    
    queue.put(result)


def mp_factor(numbers, processes):
    queue = multiprocessing.Queue()
    chunks = int(math.ceil(len(numbers)) / processes)
    procs = []
    for i in range(processes):
        proc = multiprocessing.Process(target=mp_worker, args=(queue, numbers[chunks*i:chunks*(i+1)]))
        
        procs.append(proc)
        proc.start()
        
    results = {}
    for i in range(processes):
        results.update(queue.get())
        
    for i in procs:
        i.join()
        
    return results


if __name__ == '__main__':
    res = mp_factor([10000535345345435453, 532532525], 2)
    print(res)




