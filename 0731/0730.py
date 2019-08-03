def a_pow_b(a,b):
    if b == 1:
        return a
    elif b == 0:
        return 1
    if b % 2 == 0:
        temp = a_pow_b(a, b/2)
        return temp*temp
    else:
        temp = a_pow_b(a,(b+1)/2)
        return temp*temp/a

# classical binary_search
def bs(sorted_arr, tar):
    if sorted_arr == None or len(sorted_arr) == 0: 
        return -1
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if sorted_arr[mid] == tar:
            return mid
        elif sorted_arr[mid] > tar:
            right = mid - 1 
        else:
            left = mid + 1
    return -1

# 2d array binary_Search
# in the code the col and row are reverse
def two_d_bs(sorted_2darr, tar):
    if sorted_2darr == None or len(sorted_2darr) == 0 or len(sorted_2darr[0]) == 0:
        return -1
    row_left, row_right = 0, len(sorted_2darr[0]) - 1  # i.e.   the col id   (the index for a row)
    col_left, col_right = 0, len(sorted_2darr) - 1 # i.e. the row id of the  (the index for a column)
    while col_left <= col_right:
        col_mid = col_left + int((col_right - col_left)/2)
        col_arr = sorted_2darr[col_mid]
        if col_arr[row_left] <= tar <= col_arr[row_right]: 
            while row_left <= row_right:
                row_mid = row_left + int((row_right - row_left)/2)
                if col_arr[row_mid] == tar:
                    return row_mid, col_mid
                elif col_arr[row_mid] > tar:
                    row_right = row_mid - 1
                else:
                    row_left = row_mid + 1
        elif col_arr[row_left] > tar:
            col_right = col_mid - 1
        else:
            col_left = col_mid + 1

    return -1

# a better solution, consider the 2d array as 1d array, and find the 1d index at first and mapt it to its corresponding 2d index
def two_d_bs_t(sorted_2darr, tar):
    if sorted_2darr == None or len(sorted_2darr) == 0 or len(sorted_2darr[0]) == 0:
        return -1
    row, col = len(sorted_2darr), len(sorted_2darr[0])
    left, right = 0, row * col - 1
    
    while left <= right:
        mid = left + int((right - left)/2)
        row_id, col_id = int(mid/col), mid % col
        mid_num = sorted_2darr[row_id][col_id]
        if mid_num == tar:
            return row_id, col_id
        elif mid_num > tar:
            right = mid - 1
        else:
            left = mid + 1

    return -1



def main():
  #print(bs([1,3,5,7,9,11,13,15, 17],1))
  #print(two_d_bs([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 8))
  print(two_d_bs_t([[1,2,3,4],[5,6,7,8],[9,10,11,12]], 17))

if __name__ == '__main__':
    main()