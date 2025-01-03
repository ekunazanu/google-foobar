#!/usr/bin/env python3

def solution(xs):

    positive = [x for x in xs if x > 0]
    negative = [x for x in xs if x < 0]

    if len(positive) == 0 and (len(negative) == 0 or len(negative) == 1):
        return str(0)

    product = 1
    for i in positive:
        product *= i
    for i in negative:
        product *= i
    if len(negative) % 2 == 1:
        product /= max(negative)

    return str(product)
