#!/usr/bin/python3
import random

cab_num = 20
prob_trunk = 0.2
cab_list = [1 if x < cab_num * prob_trunk else 0 for x in range(cab_num)]
random.shuffle(cab_list)

def add_cab():
    cab = input("Big Trunk?: 0(not), 1(yes)\n")
    cab = int(cab)
    if (len(cab_list) == 73):
        print("=================== Warning!! ====================")
        print("Not possible to add any more cabs to this station")
        print("Max cap: 73")
        print("Cab not added")
        print("==================================================")
        return
    cab_list.append(cab)
    cab_count()

def cab_request():
    request = input("Do you need big trunk?: 0(not), 1(yes)\n")
    request = int(request)
    if request is 0:
        cab_list.pop(0)
    else:
        cab_list.remove(1)
    cab_count()

def cab_count():
    count = len(cab_list)
    print ("The number of taxis in queue is: {:d}".format(count))
    if count <= 10:
        print("Please request more Taxis to this location")

def run_station():
    print()
    wait = input("Enter:  (0) to exit\n\t(1) if a cab arrived\n\t(2) if requesting a cab from queue:\n")
    wait = int(wait)
    if wait is 1:
        add_cab()
    elif wait is 2:
        cab_request()
    elif wait is 0:
        return 0
