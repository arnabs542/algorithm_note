# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:45:09 2019

@author: liuyu
"""
def initialize(x):
    return list('^' + x), 0

#def print_ret(x, cur):
#    print(x[:cur] + '^' + x[cur+1:])
#    return

#def cmd_h(x, cur): # move left
#    if cur > 0:
#        cur -= 1
#    return x, cur
#
#def cmd_l(x, cur): # move right
#    if cur < len(x):
#        cur += 1
#    return x, cur
    
def print_list_ret(x_list):
    print(''.join(x_list))
    return

def cmd_h(x_list, cur): # move left
    if cur > 0:
        x_list[cur] = x_list[cur - 1]
        x_list[cur - 1] = '^'
        cur -= 1
    return x_list, cur

def cmd_i(x_list, cur): # move right
    if cur < len(x_list):
        x_list[cur] = x_list[cur + 1]
        x_list[cur + 1] = '^'
        cur += 1
    return x_list, cur  

def cmd_j(x_list, cur): # vertical up # find 2 cloest element
    #0123    
    #abc\n
    #456
    #d^e
    
    #0123    
    #abc\n
    #4567
    #def\n
    #8910
    #g^h
    enter_list = []
    for i in range(cur + 1, len(x_list)):
        if i == '\n':
            enter_list.append(i)
    
    if len(enter_list) == 0:
        return x_list, cur
    
    if len(enter_list) == 1:
        end = 0 + cur - enter_list[0]
    
    else:
        end = enter_list[-2] + 1 + (cur - enter_list[-1])
    
    while cur >= end:
        x_list[cur] = x_list[cur - 1]
        cur -= 1 
    
    x_list[cur] = '^'
    
    return x_list, cur

def cmd_k(x_list, cur): # vertical down
    #0123    
    #a^b/n
    #456
    #cde
        
    enter_list = []
    for i in range(cur,len(x_list) + 1):
        if i == '\n':
            enter_list.append(i)
    
    if len(enter_list) == 0:
        return x_list, cur
    
    if len(enter_list) == 1:
        end = 0 + cur - enter_list[0]
    
    else:
        end = enter_list[0] + 1 + cur - enter_list[1]
    
    while cur >= end:
        x_list[cur] = x_list[cur - 1]
        cur -= 1 
    
    x_list[cur] = '^'
    
    return x_list, cur

def cmd_X(x, )

input_string = "today is wed\ntomorrow is thursday\nnext week is a long weekend\nand I will spend it all doing the\nstupid assignment for cs521\n"
x_list, cur = initialize(input_string)
print_list_ret(x_list)

x_list, cur = cmd_i(x_list, cur) # to the right
x_list, cur = cmd_i(x_list, cur)
x_list, cur = cmd_i(x_list, cur)
print_list_ret(x_list)

x_list, cur = cmd_h(x_list, cur) # to the left
print_list_ret(x_list)
#
#print_ret(x)
#
#print_ret(x)