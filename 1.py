#!/usr/bin/env python3

def solution(x, y):
    x.sort()
    y.sort()
    for i in range(max(len(x), len(y))):
        if x[i] == y[i]:
            pass
        else:
            if len(x) > len(y):
                return x[i]
            else:
                return y[i]
