
# leetcode 151
# i love yahoo trick, and deduplication (spaces)
# note: 1.1, 1.2, 4.1, 4.2
class Solution151:
    def reverseWords(self, s: str) -> str:
        if s is None or len(s) == 0:
            return s

        # remove leading and trailing space, and reduce duplicate spaces
        def remove_space(s_list):
            # find the last valid character that is not space
            end = len(s_list) - 1
            while end >= 0 and s_list[end] == " ":
                end -= 1
            
            if end == -1:
                return []
            
            slow, fast = 0, 0
            
            # remove leading spaces
            while fast <= len(s_list) - 1 and s_list[fast] == " ":
                fast += 1
            
            slow, fast = copy_helper(s_list, slow, fast)

            # remove duplicate spaces
            flag = True
            while fast <= end:
                # fast is point to a char
                if s_list[fast] != " ":
                    flag = True
                    slow, fast = copy_helper(s_list, slow, fast)

                # fast is point to a space
                else:
                    if flag:
                        slow, fast = copy_helper(s_list, slow, fast)
                        flag = False
                    else:
                        fast += 1
            
            return s_list[:slow]
        
        def reverse(s_list):
            # step1, reverse whole string
            reverse_helper(s_list, 0, len(s_list) - 1)
            
            # step2, reverse each word
            slow = fast = 0
            
            while fast < len(s_list):
                while fast < len(s_list) and s_list[fast] != " ":
                    fast += 1
                reverse_helper(s_list, slow, fast - 1)

                slow = fast = fast + 1
            
            return s_list
        
        def reverse_helper(s_list, i, j):
            if i >= j:
                return
            
            s_list[i], s_list[j] = s_list[j], s_list[i]
            
            return reverse_helper(s_list, i + 1, j - 1)
        
        def copy_helper(s_list, slow, fast):
            s_list[slow] = s_list[fast]
            return slow + 1, fast + 1
            
        # main
        s_list = list(s)
        
        s_list = reverse(remove_space(s_list))
        
        return ''.join(s_list)
        

# laicode 79
# deduplicate char
# notes: 2.1
class Solution_lai79(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if input is None or len(input) <= 1:
      return input
    
    input_list = list(input)

    slow = 0
    fast = 1

    while fast <= len(input_list) - 1:
      if input_list[fast] == input_list[slow]:
        fast += 1
      else:
        slow += 1
        input_list[slow] = input_list[fast]
        fast += 1

    return ''.join(input_list[:slow + 1])

# laicode 82 leetcode 
# note: 2.2
# use slow pointer to maintaince a stack
class Solution_lai84(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if input is None or len(input) <= 1:
      return input

    input_list = list(input)

    slow = -1 
    fast = 0

    while fast <= len(input_list) - 1:
      # if stack is not empty
      # if the top of stack equals to the fast index element
      if slow >= 0 and input_list[fast] == input_list[slow]:
        fast += 1
        while fast <= len(input_list) - 1 and input_list[fast] == input_list[fast - 1]:
          fast += 1
        # stack.pop()
        slow -= 1
      # if the top of stack not equals to the fast index element
      # or the stack is empty
      else:
        # stack.append()
        slow += 1
        input_list[slow] = input_list[fast]
        fast += 1
    
    return ''.join(input_list[:slow + 1])

# laicode 80
class Solution_lai80(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if input is None or len(input) <= 1:
      return input

    input_list = list(input)

    slow = 0
    fast = 1
    counter = 1

    while fast <= len(input_list) - 1:
      if input_list[fast] == input_list[slow]:
        if counter >= 2:
          fast += 1
        else:
          slow += 1
          input_list[slow] = input_list[fast]
          fast += 1
          counter += 1
      else:
        slow += 1
        input_list[slow] = input_list[fast]
        fast += 1
        counter = 1
      
    return ''.join(input_list[:slow + 1])

# lacicode 81
class Solution_lai81(object):
  def deDup(self, input):
    """
    input: string input
    return: string
    """
    # write your solution here
    if input is None or len(input) <= 1:
      return input

    input_list = list(input)

    slow = 0
    fast = 1
    counter = 1

    while fast <= len(input_list):
      counter = 1

      while fast <= len(input_list) - 1 and input_list[fast] == input_list[fast - 1]:
        fast += 1
        counter += 1
      
      if counter == 1:
        input_list[slow] = input_list[fast - 1]
        slow += 1
        fast += 1
      else:
        fast += 1

    
    return ''.join(input_list[:slow])

# laicode 172 string replace
# note: 1.5
class Solution(object):
  def replace(self, input, source, target):
    """
    input: string input, string source, string target
    return: string
    """
    # write your solution here
    # return all start point of the source substring in string
    def search(input, source, left):
      if left > len(input) - len(source):
        return False

      isEqual = True
      for ch in source:
        if input[left] != ch:
          isEqual = False
          break
        left += 1
      
      return isEqual

    # case1: length source >= target
    def replace1(input, source, target):
      input_list = list(input)
      slow = fast = 0

      while fast <= len(input_list) - 1:
        if search(input, source, fast):
          fast += len(source)
          for i in range(len(target)):
            input_list[slow] = target[i]
            slow += 1
        else:
          input_list[slow] = input_list[fast]
          slow += 1
          fast += 1

      return ''.join(input_list[:slow])

    # case2: length source < target
    def replace2(input, source, target):
      input_list = list(input)
      ptn = 0
      break_points = set([])

      while ptn <= len(input) - len(source):
        if search(input, source, ptn):
          ptn += len(source)
          break_points.add(ptn - 1)
        else:
          ptn += 1
      
      extra_space = len(break_points) * (len(target) - len(source))

      for i in range(extra_space):
        input_list.append(" ")

      slow = len(input_list) - 1
      fast = len(input) - 1

      while fast >= 0:
        if fast in break_points:
          fast -= len(source)
          for i in range(len(target) - 1, -1, -1):
            input_list[slow] = target[i]
            slow -= 1
        else:
          input_list[slow] = input_list[fast]
          slow -= 1
          fast -= 1

      return ''.join(input_list[slow + 1:])


    
    if len(source) >= len(target):
      return replace1(input, source, target)
    else:
      return replace2(input, source, target)

# string shuffling
# 1.1 First direction : “A1B2C3D4” —> “ABCD1234” ==> Merge sort

# A 1 B 2 C 3 D 4

#  A1 B2  C3  D4

#  AB12   CD34

#   ABCD1234
class Solution_shuffle:
  def shuffle(self, input_str):
    
    def helper(input_str, left, right):
      if left >= right:
        return

      mid = (left + right + 1) // 2

      helper(input_str, left, mid - 1)
      helper(input_str, mid, right)

      temp = []
      i = left
      j = mid

      while i <= mid - 1 and j <= right:
        if (
              ( # if left is char, and right is digit
                ord("A") <= ord(input_str[i]) <= ord("Z") and input_str[j].isdigit()
              ) or 
              ( # if both are char
                ord("A") <= ord(input_str[i]) <= ord("Z") and ord("A") <= ord(input_str[j]) <= ord("Z") and ord(input_str[i]) <= ord(input_str[j])
              ) or 
              ( # if both are digit
                input_str[i].isdigit() and input_str[j].isdigit() and ord(input_str[i]) <= ord(input_str[j])
              )
            ):
          temp.append(input_str[i])
          i += 1
        
        else:
          temp.append(input_str[j])
          j += 1
      
      while i <= mid - 1:
        temp.append(input_str[i])
        i += 1

      while j <= right:
        temp.append(input_str[j])
        j += 1
      
      input_str[left:right + 1] = temp.copy()

      return 
    
    input_str = list(input_str)
    helper(input_str, 0, len(input_str) - 1)
    return ''.join(input_str)

solver = Solution_shuffle()
input_str = 'A1B2C3D4'
print(solver.shuffle(input_str))

