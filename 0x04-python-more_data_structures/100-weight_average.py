#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    div = 0 if len(my_list) else 1

    for i in my_list:
        sum += i[0]*i[1]
        div += i[1]
    return sum / div
