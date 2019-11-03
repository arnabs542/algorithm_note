# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:13:10 2019

@author: liuyu
"""

x = 'defining decade'
x_list = list(x)
cur = 5



def print_file(x, cur, sep='$'):
    print (x[0: cur] + sep + x[cur:])
    
print_file(x, 0)    

def cmd_h(x, cur):       # move left by one char
    if cur > 0:
        cur = cur - 1
    return x, cur

def cmd_I(x, cur):       # move right by one
    if cur < len(x):
        cur = cur + 1
    return x, cur

def cmd_X(x, cur):
    if cur > 0:
       left = x[0 : cur -1]
       right = x[cur : ]
       x = left + right
    return x, cur-1

def cmd_n(x, cur, target):
    if cur < len(x):
        pos = x.find(target, cur, len(x))
        if pos >=0 :
            if pos == cur:
                cur = cur + 1
                pos = x.find(target, cur, len(x))
            return x, pos
        else:
            return x, cur
    
    
# define some helper functions
def end_current_line(x, cur):
    pos = x.find('\n', cur, len(x))
    if pos > 0:
        return pos
    else:
        return len(x)
    
def start_current_line(x, cur):
    pos = x.rfind('\n', 0, cur)
    if pos > 0:
        return pos + 1
    else:
        return 0    

# this need to be fixed when cursor is at the first line    
def cmd_dd(x, cur):
    s_line = start_current_line(x,cur)
    e_line = end_current_line(x, cur)
    left = x[0 : s_line -1]
    right = x[e_line : ]
    return left+right, s_line
    

def cmd_D(x, cur): #  transpose two char left and right of cur
    if cur > 0 and cur < len(x)-1:
        l_char = x[cur-1]
        r_char = x[cur]
        x = x[0: cur -1] +  r_char + l_char + x[cur + 1 : ]
        return x, cur
    


def cmd_middle(x, cur):
    return x, int(len(x)/2)

    
x = """today is wed
tomorrow is thursday
next week is a long weekend 
and I will spend it all doing the
stupid assignment for cs521"""

cur = 50
print_file(x, cur)

x, cur = cmd_D(x, cur)
print('\n --------------- \n')
print_file(x, cur)
