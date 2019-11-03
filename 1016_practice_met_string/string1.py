# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 01:57:06 2019

@author: liuyu
"""

def initialize(x, cur = 0):
    return x, cur

def print_cursor(x, cur):
    print(x[:cur] + '^' + x[cur:])
    return

def find_enter(x): # find all \n
    ret = []
    for i in range(len(x)):
        if x[i] == '\n' and i != 0 and i != len(x) - 1:
            ret.append(i)
    return ret

def cmd_h(x, cur): # move left
    if cur > 0:
        cur -= 1
    return cur

def cmd_i(x, cur): # move right
    if cur < len(x) - 1:
        cur += 1
    return cur

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
        print(pos_l, pos_r, po_rr)
        if cur - pos_l < po_rr - pos_r:
            cur = pos_r + (cur - pos_l)
        else:
            cur = pos_r + 1
    else:
        cur = cur
    return cur

def cmd_X(x, cur): # delete left of cur
    if cur > 0:
        x = x[:cur-1] + x[cur:]
    return x, cur - 1
        
def cmd_D(x, cur): # transpose left of right of the cursor
    x = list(x)
    if cur > 0 and cur < len(x) - 1:
        temp = x[cur - 1]
        x[cur - 1] = x[cur + 1]
        x[cur + 1] = temp
    return ''.join(x)
        
def cmd_dd(x, cur):
    enter_ids = find_enter(x)
    print(enter_ids)
    if cur <= enter_ids[0]: # delete first line
        return x[enter_ids[0] + 1:], 0 
    if cur > enter_ids[-1]: # delte last line
        return x[:enter_ids[-1] + 1], enter_ids[-1] + 1
    
    for i in range(1, len(enter_ids)): # other cases
        if cur >= enter_ids[i - 1] and cur <= enter_ids[i]:
            x, cur = x[:enter_ids[i - 1] + 1] + x[enter_ids[i] + 1:], enter_ids[i - 1] + 1
            break

    return x, cur

def	cmd_ddp(x, cur):
    enter_ids = find_enter(x)
    if cur <= enter_ids[0]: # cursor in first line
        return x[enter_ids[0] + 1:enter_ids[1] + 1] + x[:enter_ids[0] + 1], 0 
    if cur > enter_ids[-1]: # cursor in last line
        return x[:enter_ids[-2] + 1] + x[enter_ids[-1] + 1:] + x[enter_ids[-2] + 1:enter_ids[-1] + 1], enter_ids[-2] + 1
    
    for i in range(1, len(enter_ids) - 2):
        if cur >= enter_ids[i] and cur <= enter_ids[i + 1]:
            x, cur = x[:enter_ids[i] + 1] + x[enter_ids[i + 1] + 1:enter_ids[i + 2] + 1] + x[enter_ids[i] + 1:enter_ids[i + 1] + 1] + x[enter_ids[i + 2] + 1:], enter_ids[i] + 1
            break
        
    return x , cur # if change the last line

def cmd_n(x, cur, tar):
    pos = x.find(tar, cur, len(x))
    if pos > 0:
        return x, pos
    else:
        return x, cur

def cmd_wq(x, cur, file_path = 'C:/Users/liuyu/Desktop/2019_summer/1016/question10.txt'):
    f = open(file_path,'w')
    f.write(x[:cur] + '^' + x[cur:])
    f.close()
    return

def cmd_mid(x, cur):
    return x, int(len(x)/2)

# methods
def add_enter(x, cur):
    return x[:cur] + '\n' + x[cur:], cur + 1

def first(x, cur):
    return x, 0

def last(x, cur):
    return x, len(x) - 1

def copy(x, cur):
input_string = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\n"

print('-----0-----')
x, cur = initialize(input_string)
print_cursor(x, cur)

print('-----1,2-----')
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
print_cursor(x, cur)

cur = cmd_h(x, cur)
print_cursor(x, cur)

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


print('-----5-----')
x, cur = cmd_X(x, cur)
print_cursor(x, cur)

print('-----6-----')
x = cmd_D(x, cur)
print_cursor(x, cur)

print('-----7-----')

input_string = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\n"
x, cur = initialize(input_string,78)
print_cursor(x, cur)

x, cur = cmd_dd(x, cur)
print_cursor(x, cur)

print('-----8-----')
input_string = "Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.\n"
x, cur = initialize(input_string,10)
print_cursor(x, cur)

x, cur = cmd_ddp(x, cur)
print_cursor(x, cur)

print("-----9-----")
x, cur = cmd_n(x, cur, "better")
print_cursor(x, cur)

x, cur = cmd_n(x, cur, "implicit")
print_cursor(x, cur)

print('-----10-----')
cmd_wq(x, cur)
print('finished\n')

print('-----addition-----')
x, cur = cmd_mid(x, cur)
print_cursor(x, cur)

print('-----add \\n-----')
x, cur = add_enter(x, cur)
print_cursor(x, cur)

#def cmd_j(x, cur): # vertical up
#    enter_ids = [-1] + find_enter(x) + [len(x) - 1]
#    if cur < enter_ids[0]: # if in the first line
#        return x, cur
#    
#    for i in range(2, len(enter_ids)): # other cases
#        if cur >= enter_ids[i - 1] and cur <= enter_ids[i]:
#            pos = cur - enter_ids[i - 1]
#            if pos > enter_ids[i-1] - enter_ids[i-2]:
#                cur = enter_ids[i-1]
#            else:
#                cur = enter_ids[i-2] + pos
#            break
#    
#    return cur
#    
    