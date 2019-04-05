"""
17.10
正の整数の配列が与えられた時、過半数の要素があればそれを返し
存在しなければ-1を返せ。
"""

import time

def findMajorityElement(array):
    for x in array:
        if validate(array, x):
            return x
    return -1

def validate(array, majority):
    count = 0
    for n in array:
        if n == majority:
            count += 1
    return count > len(array)/2

def findMajorityElement2(array):
    candidate = getCandidate(array)
    if validate(array, candidate):
        return candidate
    else:
        return -1

def getCandidate(array):
    majority = 0
    count = 0
    for n in array:
        if count == 0:
            majority = n
        if n == majority:
            count += 1
        else:
            count -= 1
    return majority

def do_findMajorityElement(array):
    start = time.time()
    answer = findMajorityElement(array)
    end = time.time()
    print("findMajorityElement()")
    print("answer:{}".format(answer))
    print("time:{} second".format(end-start), end="\n\n")

def do_findMajorityElement2(array):
    start = time.time()
    answer = findMajorityElement2(array)
    end = time.time()
    print("findMajorityElement2()")
    print("answer:{}".format(answer))
    print("time:{} second".format(end-start), end="\n\n")


if __name__ == "__main__":
    sa1 = [3,1,7,1,7,7,3,7,1,7,7]*1000
    sa2 = [3,1,7,1,7,7,3,7,1,7,2]*1000
    do_findMajorityElement(sa1)
    do_findMajorityElement2(sa1)
    do_findMajorityElement(sa2)
    do_findMajorityElement2(sa2)
