# bubble sort
def bubbleSort(nums):
    if nums == None or len(nums) <= 1:
        return nums

    for i in range(len(nums)):
        isSwap = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j + 1)
                isSwap = True
        if not isSwap:
            break

    return nums

def swap(nums, i, j):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp
    return

print("Problem 5: bubble sort")
print(bubbleSort([2, 6, -6, -3, 1, 19]))
print(bubbleSort([5,1,1,2,0,0]))
print(bubbleSort([5,2,3,1]))
print("")

# DNA sequence complementary
def iscomplementary(seq1, seq2):
    if len(seq1) != len(seq2):
        return False
    ptn1, ptn2 = 0, len(seq2) - 1
    while ptn1 < len(seq1):
        if (seq1[ptn1] == 'T' and seq2[ptn2] != 'A') or (seq1[ptn1] == 'A' and seq2[ptn2] != 'T') or (seq1[ptn1] == 'C' and seq2[ptn2] != 'G') or (seq1[ptn1] == 'G' and seq2[ptn2] != 'C'):
            return False
        ptn1 += 1
        ptn2 -= 1
    return True

print("Problem 6: dna sequence complementary")
print(iscomplementary('TTAC', 'GTAA'))
print(iscomplementary('TTACGGCA', 'TGCCGTAA'))
print(iscomplementary('TTACGC', 'GGGTAT'))