"""
8.1
子供がn段の階段を駆け上がる時、一歩で1段・2段・3段を登ることが
できるとすると、考え得る階段の上がり方は何通りあるか？
"""

import time
from functools import lru_cache

def countWays(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays(n-1) + countWays(n-2) + countWays(n-3)

def countWays_memo(n):
    memo = [-1]*(n+1)
    def _countWays(n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            if memo[n] > -1:
                return memo[n]
            else:
                memo[n] = _countWays(n-1) + _countWays(n-2) + _countWays(n-3)
                return memo[n]
    return _countWays(n)

@lru_cache(maxsize=None)
def countWays_lru_cache(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return countWays_lru_cache(n-1) + countWays_lru_cache(n-2) + countWays_lru_cache(n-3)

def do_countWays(n):
    start = time.time()
    answer = countWays(n)
    end = time.time()
    print("do_countWays({})".format(n))
    print("answer:{}".format(answer))
    print("time:{} second".format(end-start), end="\n\n")

def do_countWays_memo(n):
    start = time.time()
    answer = countWays_memo(n)
    end = time.time()
    print("do_countWays_memo({})".format(n))
    print("answer:{}".format(answer))
    print("time:{} second".format(end-start), end="\n\n")

def do_countWays_lru_cache(n):
    start = time.time()
    answer = countWays_lru_cache(n)
    end = time.time()
    print("do_countWays_lru_cache({})".format(n))
    print("answer:{}".format(answer))
    print("time:{} second".format(end-start))

if __name__ == "__main__":
    do_countWays(30)
    do_countWays_memo(30)
    do_countWays_lru_cache(30)
