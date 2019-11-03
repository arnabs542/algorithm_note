class Solution443:
    def compress(self, chars):
        l, r, counter = 0, 0, 0 # counter for the length of the current char
        while r < len(chars):
            if chars[r] == chars[l]: # if equals, right ++
                r += 1
                counter += 1
            else:
                if counter != 1: # if only one char, inplace replace, l ++, char[l] = char[r]
                    l = self.replace(chars, l, counter)
                counter = 0
                l += 1
                chars[l] = chars[r]
        
        if counter == 1:
            return l + 1 # consider the last type of char has only one length
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
    
    def print_compuressed(self, chars):
        index = self.compress(chars)
        print(index)
        print(chars[:index])
        return
S = Solution443()
S.print_compuressed(["a","b","b","b","b","b","b","b","b","b","b","b","b"])


