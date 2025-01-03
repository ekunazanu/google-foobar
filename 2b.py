#!/usr/bin/env python3

from fractions import Fraction

def solution(pegs):
    altDistanceSum = -pegs[0]
    for i in range(1, len(pegs) - 1):
        if i % 2 == 0:
            altDistanceSum -= 2 * pegs[i]
        else:
            altDistanceSum += 2 * pegs[i]
    if len(pegs) % 2 == 0:
        altDistanceSum += pegs[len(pegs) - 1]
        r0 = (2 * float(altDistanceSum))/3
    else:
        altDistanceSum -= pegs[len(pegs) - 1]
        r0 = 2 * float(altDistanceSum)

    r = r0
    for i in range(len(pegs) - 1):
        if r < 1:
            return [-1, -1]
        else:
            r = (pegs[i + 1] - pegs[i]) - r

    r0 = Fraction(r0).limit_denominator()
    return [r0.numerator, r0.denominator]
