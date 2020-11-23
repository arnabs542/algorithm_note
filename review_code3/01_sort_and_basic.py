# rainbow sort I
class Solution(object):
  def rainbowSort(self, array):
    if len(array) <= 3:
      return sorted(array)
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    # -1 -1 -1 -1 -1 0 0 0 1 1 1 1 
    #                1          2
    #                    3 

    p1 = ps = 0
    p2 = len(array) - 1

    while ps <= p2:
      if array[ps] == -1:
        array[p1], array[ps] = array[ps], array[p1]
        p1 += 1
        ps += 1 
      elif array[ps] == 0:
        ps += 1
      else:
        array[p2], array[ps] = array[ps], array[p2]
        p2 -= 1

    return array


    

# rainbow sort II
class Solution(object):
  def rainbowSortII(self, array):
    """
    input: int[] array
    return: int[]
    """
    # write your solution here
    # cases

    if len(array) == 0:
      return array
    
    # 0 0 0 0 1 2 1 2 1 3 3 3 3 
    #         p1      p2
    #                   ps
    
    # 1 2 1 2 1
    # p1      p2

    # 1 1 1 2 2
    #       p1
    #     p2  
    p1 = ps = 0
    p2 = len(array) - 1

    while ps <= p2:
      if array[ps] == 0:
        array[p1], array[ps] = array[ps], array[p1]
        p1 += 1
        ps += 1
      elif array[ps] == 3:
        array[p2], array[ps] = array[ps], array[p2]
        p2 -= 1
      else: # for other colors
        ps += 1

    while p2 >= p1:
      if array[p2] == 1:
        array[p1], array[p2] = array[p2], array[p1]
        p1 += 1
      else:
        p2 -= 1
    
    return array


# rainbow sort III
class Solution(object):
  def rainbowSortIII(self, array, k):
    """
    input: int[] array, int k
    return: int[]
    """
    # write your solution here

  # 1, 1, 2, 3, 4, 5, 5
  #          p1 
  #          p2
  #             ps

  # 1 2 3 4 5
  #     lu

    def helper(array, lb, ub, p1, p2):
      if lb >= ub:
        return
      
      ps = p1

      while ps <= p2:
        if array[ps] == lb:
          array[p1], array[ps] = array[ps], array[p1]
          p1 += 1
          ps += 1
        elif array[ps] == ub:
          array[p2], array[ps] = array[ps], array[p2]
          p2 -= 1
        else:
          ps += 1

      return helper(array, lb + 1, ub - 1, p1, p2)

    if k == 1:
      return array

    helper(array, 1, k, 0, len(array) - 1)

    return array