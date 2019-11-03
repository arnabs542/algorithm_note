# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 13:05:21 2019

@author: epinsky
"""

N_PTR = 0; P_PTR = 1; DATA = 2
x_str = """Monday
Tuesday
Wednesday"""

x_list = x_str.split('\n')
a = [None, None,'Monday']; b = [None, None, 'Tuesday']; 
c = [None, None, 'Wednesday']

def construct_linked_list(y_str):
    y_list = y_str.split('\n')
    new_start = None
    new_end = None
    for e in y_list:
        new_node = [None, None, e]
        if new_start is None and new_end is None:
            new_start = new_node
            new_end = new_node
        else:
            new_node[P_PTR] = new_end
            new_end[N_PTR] = new_node
            new_end = new_node
    return new_start, new_end
    
def print_sublist(first, last):
    next_node = first
    while next_node is not None:
        print(next_node[DATA])
        if next_node == last:
            break
        next_node = next_node[N_PTR]
    return

def get_record(first, last, pos):
    next_node = first
    counter = -1
    while next_node is not None:
        counter = counter + 1
        if counter == pos:
            break
        else:
            next_node = next_node[N_PTR]
    return next_node

def print_file(start, end, cur_node, delta):
    if cur_node is not start:
        end_left_sublist = cur_node[P_PTR]
        print_sublist(start, end_left_sublist)
    cur_line = cur_node[DATA]
    print(cur_line[ : delta] + '$' + cur_line[delta : ])    
    if cur_node is not end:    
        start_right_sublist = cur_node[N_PTR]
        print_sublist(start_right_sublist, end)
    print('\n')
    return


def cmd_h(start, end, z, delta):    # go back one character
    if delta > 0:
        delta = delta -1
    return start, end, z, delta

def cmd_I(start, end, z, delta):    # move cursor one pos to the right
    cur_line = z[DATA]
    if delta < len(cur_line)-1:
        delta = delta + 1
    return start, end, z, delta
    
def cmd_D(start, end, z, delta):    # transpose two chars
    cur_line = z[DATA]
    left_char  = cur_line[delta - 1]
    right_char = cur_line[delta]
    left_part = cur_line[ 0 : delta - 1]
    right_part = cur_line[delta + 1 : ]
    new_line = left_part + right_char + left_char + right_part
    z[DATA] = new_line
    return start, end, z, delta
    

def cmd_k(start, end, z, delta):  # vertically down
    if z != end:
        next_rec = z[N_PTR]
        next_line = next_rec[DATA]
        if delta > len(next_line):
            delta = len(next_line)- 1
        z = next_rec
    return start, end, z, delta
        
# this function looks for a target in a double linked list
# if it finds it, it will return record and delta
# otherwise it will return None, -1
def helper_find(x_start, x_end, target):
    if x_start is not None:
        next_record = x_start
        while next_record is not None:
            cur_line = next_record[DATA]
            pos = cur_line.find(target)
            if pos >= 0:
                return next_record, pos
            else:
                next_record = next_record[N_PTR]
        return None, -1
    else:
        return None, -1

# fix errors             
def cmd_n(start, end, z, delta, target):    
    cur_line = z[DATA]
    pos = cur_line.find(target, delta, len(cur_line))
    if pos >= 0:
        delta = delta + pos
        return start, end, z, delta
    else:
        x_start = z[N_PTR]
        rec, delta = helper_find(x_start, end, target)
        if rec is not None:
            return start, end, rec, delta
        else:
            return start, end, z, delta
        
# easy version: swap lines     
def cmd_ddp_easy(start, end, z, delta): # transpose adjacene tlines
    next_record = z[N_PTR]
    if next_record is not None:
        cur_line = z[DATA]
        next_line = next_record[DATA]
        temp_line = cur_line
        z[DATA] = next_line
        next_record[DATA] = temp_line
        return start, end, next_record, delta
    else:
        return start, end, z, delta
        
# hard - relink pointers    
# fix it at home 
def cmd_ddp_hard(start, end, z, delta): # transpose adjacene tlines
   next_record = z[N_PTR]
   x = z[P_PTR]
   y = next_record[N_PTR]
   x[N_PTR] = next_record
   next_record[N_PTR ] = z
   z[N_PTR] = y
   y[P_PTR] = z
   z[P_PTR] = next_record
   next_record[P_PTR] = x
   return start, end, z, delta
   

def cmd_dd(start, end, z, delta): # delete till end of line
   cur_line = z[DATA]
   new_line = cur_line[ : delta]
   z[DATA] = new_line
   return start, end, z, delta

def cmd_X(start, end, z, delta): # delete char to left of cursos
    if delta > 0:
        cur_line = z[DATA]
        new_line = cur_line[ : delta-1] + cur_line[delta : ]
        z[DATA] = new_line
        delta = delta - 1
    return start, end, z, delta


def cmd_start_file(start, end, z, delta):
    z = start
    return start, end, z, 0

def cmd_end_file(start, end, z, delta):
    z = end
    last_line = z[DATA]
    return start, end, z, len(last_line) 

def cmd_insert_line(start, end, z, delta, new_string):
    new_node = [None, None, new_string]
    if z != end:
        new_node[N_PTR] = z[N_PTR]
        w = z[N_PTR]
        w[P_PTR] = new_node
        z[N_PTR] = new_node
        new_node[P_PTR] = z
        return start, end, new_node, 0
    else:
        new_node[P_PTR] = z
        z[N_PTR] = new_node
        end = new_node
        return start, end, new_node, 0
    
    
    
    
    
    
    

    
new_start, new_end = construct_linked_list(x_str)
z = get_record(new_start, new_end, 1)
delta = 3

print_file(new_start, new_end, z, delta)

"""
print_file(new_start, new_end, z, delta)
new_start, new_end, z, delta = cmd_h(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta)   
"""
"""
new_start, new_end, z, delta = cmd_I(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta)   
"""
"""
new_start, new_end, z, delta = cmd_D(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_k(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_n(new_start, new_end, z, delta, 'nnn')
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_ddp_easy(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_ddp_hard(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_dd(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_X(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_start_file(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
"""
new_start, new_end, z, delta = cmd_end_file(new_start, new_end, z, delta)
print_file(new_start, new_end, z, delta) 
"""
new_start, new_end, z, delta = cmd_insert_line(new_start, new_end, z, delta, 'saturday')
print_file(new_start, new_end, z, delta) 


