


# leetcode 408
class Solution408:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
#         w: applestore
#         abb: app3to1e
#         index: 0
#               applestore             app3to1e
#                                       /     
#               pplestore            pp3to1e
#                                     /
#               plestore           p3to1e
#                                     \
#               lestore               3to1e
#                                    /
#               tore               to1e
#                                  /
#               ore              o1e, 7
#                                /
#               re              1e, 8
#                                \
#               e                 e
#                                 /
#               null              t
                        
        # word_id: the index of the word
        # abb_id: the index of the abbreviation
        # flag: whether prior index is digit
        def helper(word, abbr):
            # base case
            if word == '' and abbr == '':
                return True
            if word == '' or abbr == '':
                return False
            
            # recursive rule
            # abbrev's index
            i = 0
            counts = '0'
            # print(word, abbr)
            while i < len(abbr) and abbr[i].isdigit():
                if i == 0 and abbr[i] == '0':
                    return False
                counts += abbr[i]
                i += 1
            
            # number of indices we need to move
            counts = int(counts)
            
            # if the length is longer than remaining word
            if counts > len(word):
                return False
            
            if counts == 0 and word[0] == abbr[0]:
                return helper(word[1:], abbr[1:])
            elif counts != 0:
                return helper(word[counts:], abbr[counts // 10 + 1:])
                
        return helper(word, abbr)
                