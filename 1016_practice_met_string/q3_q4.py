# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 20:26:47 2019

@author: liuyu
"""

def initialize(x, cur = 0):
    return x, cur

def print_cursor(x, cur):
    print(x[:cur] + '^' + x[cur:])
    return

def cmd_j(x, cur):
    pos_l = x.rfind('\n', 0, cur) # left side of the cursor
    if pos_l > 0:
        pos_ll = x.rfind('\n', 0, pos_l) # left side of the pos_l
        if cur - pos_l < pos_l - pos_ll:
            cur = pos_ll + (cur - pos_l)
        else:
            cur = pos_l
    else:
        cur = cur
    return cur

def cmd_k(x, cur):
    pos_r = x.find('\n', cur, len(x)) # right side of cursor
    pos_l = x.rfind('\n', 0, cur) # left side of cursor
    if pos_r != len(x):
        po_rr = x.find('\n', pos_r + 1, len(x)) # right side of the pos_r
        if cur - pos_l < po_rr - pos_r:
            cur = pos_r + (cur - pos_l)
        else:
            cur = pos_r + 1
    else:
        cur = cur
    return cur

def add_enter(x, cur):
    return x[:cur] + '\n' + x[cur:], cur + 1

def first(x, cur):
    return x, 0

def last(x, cur):
    return x, len(x) - 1

input_string = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\n"

print('-----3-----')
x, cur = initialize(input_string, 55)
print_cursor(x, cur)
cur = cmd_j(x, cur)
print_cursor(x, cur)

print('-----4-----')
x, cur = initialize(input_string, 55)
print_cursor(x, cur)
cur = cmd_k(x, cur)
print_cursor(x, cur)

x, cur = initialize(input_string, 10)
print_cursor(x, cur)
x, cur = add_enter(x, cur)
print_cursor(x, cur)

x, cur = first(x, cur)
print_cursor(x, cur)

x, cur = last(x, cur)
print_cursor(x, cur)
