#!/usr/bin/python3
cab_num = 72
prob_trunk = 0.2
cab_list = [1 if x < cab_num * prob_trunk else 0 for x in range(cab_num)]
def add_cab():
    cab = input("Big Trunk?: 0(not), 1(yes)")
    cab = int(cab)
    cab_list.append(cab)
    cab_count()

def cab_request():
    request = input("Do you need big trunk?: 0(not), 1(yes)")
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
    wait = input("Enter (1) if a cab arrived or (2) if requesting a cab from queue:")
    wait = int(wait)
    if wait is 1:
        add_cab()
    if wait is 2:
        cab_request()
