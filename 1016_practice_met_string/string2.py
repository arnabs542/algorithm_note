# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 09:57:21 2019

@author: liuyu
"""
input_string = ["Beautiful is better than ugly.",
                "Explicit is better than implicit.",
                "Simple is better than complex.",
                "Complex is better than complicated."]

def initialize(x, cur = (0,0)):
    if cur[0] < 0 or cur[1] < 0 or cur[0] > len(x) + 1 or cur[1] > len(x[cur[0]]) - 1:
        raise ValueError("Invalid cur")
    return x, cur

def print_list(x, cur):
    for i in range(len(x)):
        s = x[i]
        if i == cur[0]: 
            print(s[:cur[1]] + '^' + s[cur[1]:])
        else:
            print(s)
    return
        
def cmd_h(x, cur): # move left
    if cur[1] > 0 :
        cur = (cur[0], cur[1] - 1)
        
    if cur[1] == 0 and cur[0] > 0:
        cur = (cur[0] - 1, len(x[cur[0] - 1]))
    
    return cur

def cmd_i(x, cur): # move right
    if cur[1] < len(x[cur[0]]) - 1:
        cur = (cur[0], cur[1] + 1)
        
    if cur[1] == len(x[cur[0]]) - 1 and cur[0] < len(x) - 1:
        cur = (cur[0] + 1, 0)
    
    return cur

def	cmd_j(x, cur): # vertical up
    if cur[0] == 0:
        return (cur[0], 0)
    
    if cur[1] > len(x[cur[0] - 1]) - 1:
        col = len(x[cur[0] - 1]) - 1
        row = cur[0] - 1
    
    else:
        col = cur[1]
        row = cur[0] - 1
    
    return (row, col)

def	cmd_k(x, cur): # vertical down
    if cur[0] == len(x) - 1:
        return (cur[0], 0)
    
    if cur[1] > len(x[cur[0] + 1]) - 1:
        col = len(x[cur[0] + 1]) - 1
        row = cur[0] + 1
    
    else:
        col = cur[1]
        row = cur[0] + 1
    
    return (row, col)

def	cmd_X(x, cur): # delete left
    if cur[0] == 0 and cur[1] == 0:
        return cur
    
    if cur[1] == 0:
        x[cur[0] - 1] = x[cur[0] - 1][:-1]
        return x, (cur[0] - 1, len(x[cur[0] - 1]) - 2)
    
    x[cur[0]] = x[cur[0]][:cur[1] - 1] + x[cur[0]][cur[1]:]
    return x, (cur[0], cur[1] - 1)

#def	cmd_dd(x, cur):
#    if cur

def	cmd_dd(x, cur): # delete line,
    if cur[0] == len(x) - 1:
        x = x[:-1]
        x.append(' ')
        return x, (len(x) - 1, len(x[len(x) - 1]) - 1)
    
    x = x[:cur[0]] + x[cur[0] + 1:]
    return x, (cur[0], 0)

def cmd_ddp(x, cur): # transpose two adjacent lines
    if len(x) <= 1:
        return x
    if cur[0] == len(x) - 1:
        temp = x[cur[0]]
        x[cur[0]] = x[cur[0] - 1]
        x[cur[0] - 1] = temp
    
    temp = x[cur[0]]
    x[cur[0]] = x[cur[0] + 1]
    x[cur[0] + 1] = temp
    
    return x, (cur[0], 0)
    
def cmd_mid(x, cur):
    lens = []
    for i in x:
        lens.append(len(i))
    mid = int(sum(lens) / 2)
    
    current, index = 0, 0 # sum of totall length, row of list
    while True:
        current += lens[index]
        if current >= mid:
            break
        index += 1
    return (index, mid - index)

def	cmd_n(x, cur, target): # find
    for i in range(cur[0], len(x)):
        if i == cur[0]:
            temp = x[i].find(target, cur[1])
        else:
            temp = x[i].find(target)
        
        if temp < 0:
            pass
        else:
            cur = (i, temp)
            break
    return x, cur

def cmd_wq(x, cur, file_path = 'C:/Users/liuyu/Desktop/2019_summer/1016/question10_1.txt'):  #write your representation as text file and save it
    output = ''
    for i in range(len(x)):
        s = x[i]
        if i == cur[0]: 
            output += s[:cur[1]] + '^' + s[cur[1]:] + '\n'
        else:
            output += s + '\n'
    f = open(file_path,'w')
    f.write(output)
    f.close()
    return
    
x, cur = initialize(input_string, (3,34))
print_list(x, cur)

print("\n-----1-----")
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
cur = cmd_i(x, cur)
print_list(x, cur)

print("\n-----2-----")
cur = cmd_h(x, cur)
cur = cmd_h(x, cur)
print_list(x, cur)

print("\n-----3-----")
cur = cmd_j(x, cur)
print_list(x, cur)

print("\n-----4-----")
cur = cmd_k(x, cur)
print_list(x, cur)

print("\n-----5-----")
x,cur = cmd_X(x, cur)
print_list(x, cur)

print("\n-----7-----")
x, cur = initialize(input_string, (1,25))
print_list(x, cur)
print("\n")

x, cur = cmd_dd(x, cur)
print_list(x, cur)

print("\n-----8-----")
x, cur = cmd_ddp(x, cur)
print_list(x, cur)

print("\n-----additional-----")
cur = cmd_mid(x, cur)
print_list(x, cur)

print("\n-----9-----")
x, cur = initialize(input_string, (1,15))
print_list(x, cur)
print("\n")

x, cur = cmd_n(x, cur, 'better')
print_list(x, cur)

print("\n-----10-----")
cmd_wq(x, cur)
print("finished")

