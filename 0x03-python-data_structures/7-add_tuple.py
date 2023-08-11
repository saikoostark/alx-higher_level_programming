#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a1, a2 = tuple_a + (0,0)[:max(0, 2-len(list(tuple_a)))]
    b1, b2 = tuple_b + (0,0)[:max(0, 2-len(list(tuple_b)))]
    return (a1+b1, a2+b2)
