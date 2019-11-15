from collections import deque
from copy import copy
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # same question with word ladder
        # in this case, we will maintain a data struc to track all possible answer
        # we will track the path rather than the length, the length is just the len(path)
        
        # initial state: queue will store the current word and the current length of the transformation path
        queue = deque([[beginWord]])
        wordList = set(wordList)
        # visited = set(beginWord)
        ret = []
        global_min_length = float('inf')
        
        while queue:
            # expand: queue will pop the first in word and its transformation path's length, add the word to the visited matrix
            path = queue.popleft()
            currWord = path[-1]
            length = len(path)
            path_set = set(path)
            if length > global_min_length:
                # if length is bigger than global_min_length, we will not continue generate the currWord
                continue
            
            # termination: if currWord is the endWord, it means we have found the shortest path
            if currWord == endWord:
                global_min_length = min(len(path), global_min_length)
                ret.append(path)
                # if we found the result, we will not generate the currWord
                continue 
            
            # generate: try every possible 'one letter different' word to the currWord. If it is inside the wordList and it has not been shown before, then we will add it toe the BFS queue

            for i in range(len(currWord)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    tempWord = currWord[:i] + ch + currWord[i + 1:]
                    if tempWord in wordList and (tempWord not in path_set):
                        path.append(tempWord)
                        queue.append(copy(path))
                        path.pop()
                        # visited.add(tempWord)
        return ret

