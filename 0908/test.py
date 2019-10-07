class Solution520:
    def detectCapitalUse(self, word):
        if word == None:
            return False
        
        pointer = 0
        while pointer < len(word):
            print(word)
            if pointer == 0 and word[0] != word[0].upper():
                return False
            else:
                temp = word[pointer - 1:pointer + 1] 
                if temp != temp.lower() and temp != temp.upper():
                    return False
            pointer += 1
        return True

S = Solution520()
print(S.detectCapitalUse('USA'))