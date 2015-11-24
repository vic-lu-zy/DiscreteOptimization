#!/usr/bin/python
# -*- coding: utf-8 -*-
from operator import attrgetter
from collections import namedtuple
Item = namedtuple("Item", ['index', 'value', 'weight'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')
    item_count,capacity = map(int,lines.pop(0).split())
    print(item_count,capacity)
    items = []

    for i in range(item_count):
        parts = list(map(int,lines[i].split()))
        if parts[1]<=capacity:
            items.append(Item(i, parts[0], parts[1]))
    items.sort(key=lambda x:x.value/x.weight,reverse=True)

    # for i in items:
    #     print(i)
    # print('')

    #approximate optimal solution
    optimal,weight = 0,capacity
    for item in items:
        # optimal += item.value
        if weight+item.weight<=capacity:
            optimal += item.value
            weight  -= item.weight
        else:
            optimal += int(item.value*weight/item.weight+1)
            weight = 0
            break
    #DFS:
    best = -float('inf')
    sol = []
    q = [(0,capacity,optimal,0,[])]
    while q:
        # print(q)
        value,room,est,i,r = q.pop()
        if i == len(items):
            if value>best:
                best = value
                sol = r
                print(best,r)
        if i<len(items):
            if est<best:
                continue
            else:
                q.append((value,room,est-items[i].value,i+1,r))
                if items[i].weight<=room:
                    q.append((value+items[i].value,
                        room-items[i].weight,est,i+1,r+[i]))

    taken=[0]*item_count
    weight = capacity
    for i in sol:
        taken[items[i].index]=1
        weight -= items[i].weight
    # prepare the solution in the specified output format
    output_data = str(best) + ' ' + str((weight==0)*1) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print (solve_it(input_data))
    else:
        print ('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')
