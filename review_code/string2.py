class Solution394:
    def decodeString(self, s: str) -> str:
        s_list = list(s)
        res = '' # temp str
        countStack = [] # count int number
        resStack = [] # all temp str in stack 
        idx = 0 # index
        while idx < len(s_list):
            if s_list[idx].isdigit(): # if s_list[idx] is integer, then sotre it into the countstack
                count = 0
                while s_list[idx].isdigit():
                    count = 10 * count + int(s_list[idx]) # the real cont number with * 10
                    idx += 1
                countStack.append(count)
            elif s_list[idx] == '[':
                resStack.append(res)
                res = ''
                idx += 1
            elif s_list[idx] == ']':
                temp = resStack.pop()
                repeatTimes = countStack.pop()
                for i in range(repeatTimes):
                    temp += res
                res = temp
                idx += 1
            else:
                res += s_list[idx]
                idx += 1
        return res

class Solution443:
    def compress(self, chars: List[str]) -> int:
        l, r, counter = 0, 0, 0
        while r < len(chars):
            if chars[r] == chars[l]:
                r += 1
                counter += 1
            else:
                if counter != 1:
                    l = self.replace(chars, l, counter)
                counter = 0
                l += 1
                chars[l] = chars[r]
        
        if counter == 1:
            return l + 1
        else:
            l = self.replace(chars, l, counter)
            l += 1
        return l
        
    def replace(self, chars, l, counter):
        temp = str(counter)
        for s in temp:
            l += 1
            chars[l] = s
        return l

class Solution1047:
    def removeDuplicates(self, S):
        if len(S) <= 1:
            return S
        
        stack = []
        pnt = 0
        while pnt <= len(S) - 1:
            if len(stack) == 0:
                stack.append(S[pnt])
                pnt += 1
                
            while pnt <= len(S) - 1 and len(stack) != 0 and stack[-1] == S[pnt]:
                stack.pop()
                pnt += 1
            if pnt <= len(S) - 1:
                stack.append(S[pnt])
                pnt += 1
            
        return ''.join(stack)

# I love yahoo and remove spaces and duplicate spaces
class Solution151:
    def reverseWords(self, s):
        if len(s) == 0: 
            return ""
        
        sl = list(s)
        # step 1 reverse all words
        left, right = 0, 0
        pnt = 0

        while pnt < len(sl):
            if pnt == len(sl)-1:
                self.swap_word(sl, left, pnt)
            
            if sl[pnt] == ' ':
                right = pnt - 1
                self.swap_word(sl, left, right)
                pnt += 1
                left = pnt
            else:
                pnt += 1
        # expect 'eht yks si eulb'
        
        # step 2 reverse whole sentence
        self.swap_word(sl, 0, len(sl) - 1)
        # ecpect 'blue is sky the', but with leading and duplicate zeros
    
        # step 3 delete leading and duplicate zeros
        cut = self.delete_zero(sl)
        
        return ''.join(sl[:cut])
        
    def swap_word(self, sl, left, right):
        # base case
        if left >= right: 
            return
        
        # recursive rule
        temp = sl[left]
        sl[left] = sl[right]
        sl[right] = temp
        
        self.swap_word(sl, left + 1, right - 1)
        
        return
    
    def delete_zero(self, sl):
        slow, fast, word_count = 0, 0, 0
        while fast < len(sl):
            while fast < len(sl) and sl[fast] == ' ':
                fast += 1
            
            # delete leading zero and duplicate zero (if fast == len(sl) - 1, we are done, no need to manipulate slow)
            if fast < len(sl) and word_count != 0: 
                sl[slow] = ' '
                slow += 1
            
            while fast < len(sl)and sl[fast] != ' ':
                sl[slow] = sl[fast]
                fast += 1
                slow += 1
                
            word_count += 1
        return slow

# sliding windows
# longest unique substring
class Solution3(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        
        slow = 0
        fast = 1
        global_max = 1
        temp = fast - slow
        hashset = set(s[0])
        
        while fast < len(s):
            if s[fast] not in hashset:
                hashset.add(s[fast])
                fast += 1
                temp += 1
                global_max = max(global_max, temp)
            else: 
                hashset.remove(s[slow])
                slow += 1
                temp -= 1
                
        return global_max

# Longest Substring with At Most Two Distinct Characters (sliding window)
class Solution159(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) <= 1:
            return len(s)
        
        slow = 0
        fast = 1               # I will kepp the string between slow and fast always valid
        temp = fast - slow
        global_max = 0
        hashtable = {s[0]: 1} # I will keep the hashset always valid
        
        while fast < len(s):
            if s[fast] in hashtable:
                hashtable[s[fast]] += 1
                fast += 1
                temp += 1
                global_max = max(global_max, temp)
            
            elif s[fast] not in hashtable and len(hashtable) < 2:
                hashtable[s[fast]] = 1
                fast += 1
                temp += 1
                global_max = max(global_max, temp)
            
            elif s[fast] not in hashtable and len(hashtable) == 2:
                while len(hashtable) == 2:
                    hashtable[s[slow]] -= 1
                    if hashtable[s[slow]] <= 0:
                        hashtable.pop(s[slow])
                    slow += 1
                temp = fast - slow
            
        return global_max
        

class Solution1234:
    def balancedString(self, s: str) -> int:
        hashmap = {'Q': 0, 'W': 0, 'E': 0, 'R': 0}
        for char in s:
            hashmap[char] = hashmap.get(char, 0) + 1
        print(hashmap)
        left = 0
        right = 0
        ret = len(s)
        
        while right <= len(s) - 1:
            # right pointer earse one char
            hashmap[s[right]] -= 1
            right += 1
            # if the hashmap is valid, we could move the left pointer
            while left <= len(s) - 1 and all(len(s) / 4 >= hashmap[char] for char in 'QWER'):
                # we need update the result before we add back new characters
                ret = min(ret, right - left)  
                # after update the ret, we could add back the char at left pointer
                # so even one time we add back more charcter, it will not affect the ret
                # for QWER example:
                # at 1st round, we update the ret to 1, left and right both += 1
                # at 2nd round, we update the ret to 0, then left + 1, it make the hashmap invalid, and it will stop the while loop for left pointer 
                hashmap[s[left]] += 1
                left += 1
            
        
        return ret

# find Anagrams
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p):
            return []
        
        # hashmap to store the information of p
        hashmap = {}
        for char in p:
            hashmap[char] = hashmap.get(char, 0) + 1
        
        slow, fast = 0, 0
        ret = []
        
        # initial state, after that slow is at 0, fast is at len(p)
        while fast < len(p):
            self.update(hashmap, None, s[fast])
            fast += 1
        if self.check_hashmap(hashmap):
            ret.append(slow)
        
        # move the window, and update the hashmap each time
        while fast <= len(s) - 1:
            self.update(hashmap, s[slow], s[fast])
            slow += 1
            fast += 1
            if self.check_hashmap(hashmap):
                ret.append(slow)
        return ret
    
    def update(self,hashmap, moveout, movein):
        # remove the char at slow index
        temp = hashmap.get(moveout)
        if temp != None:
            hashmap[moveout] += 1
        
        # add the char at fast index
        temp = hashmap.get(movein)
        if temp != None:
            hashmap[movein] -= 1
        return
    
    def check_hashmap(self, hashmap):
        for num in hashmap.values():
            if num != 0:
                return False
            
        return True