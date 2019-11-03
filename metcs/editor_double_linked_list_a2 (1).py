# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:45:23 2019

@author: epinsky
"""

N_PTR = 0; P_PTR = 1; DATA = 2
x = """art
of
war"""
x_list = x.split('\n')
print(x_list)
def construct_linked_list(x_list):
    start = None
    end = None
    for e in x_list:
        next_node = [None, None, e]
        if start is None and end is None:
            start = next_node; end   = next_node
#            next_node[P_PTR] = next_node; next_node[N_PTR]=next_node
        else:
            end[N_PTR] = next_node
            next_node[P_PTR] = end
            end = next_node
    return start, end



n_start, n_end = construct_linked_list(x_list)
print(n_start) # [next, prev, val]
print(n_end)   # [prev, next, val]

def print_line(n_start, level, cur):
    if level == cur[0]:
        print(n_start[2][:cur[1]] + '$' + n_start[2][cur[1]:])
    else:
        print(n_start[2])
    return

def print_file_from_start(n_start, level, cur):
    if n_start[0] == None:
        print_line(n_start, level, cur)
        return

    print_line(n_start, level, cur)
    print_file_from_start(n_start[0], level + 1, cur)
    return 

print('use the n_start')
print_file_from_start(n_start, 0, (0,1))

def print_file_from_end(n_end, level, cur):
    if n_end[1] == None:
        print_line(n_end, level, cur)
        return

    print_file_from_end(n_end[1], level - 1, cur)
    print_line(n_end, level, cur)
    return

print('use the n_end')
print_file_from_end(n_end, len(x_list) - 1, (1,0))
