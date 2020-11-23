
figure = [
    # 0   1   2   3   4
    [".",".",".",".","."], #0
    [".",".","F","F","F"], #1
    ["F","F","F","F","."], #2
    [".","F","F","F","."], #3
    ["#","F","F","F","."], #4
    ["F","F","F",".","."], #5
    ["F","F","F",".","#"], #6
    [".",".",".","#","."], #7
    [".",".",".",".","."]  #8
]

# visited, bottom = set([]), []

def findBottom(figure, row, col, visited, bottom):
    # print(1)
    if row < 0 or col < 0 or row > len(figure) - 1 or col > len(figure[0]) - 1:
        return bottom
    if (row, col) in visited or figure[row][col] != "F":
        return bottom

    visited.add((row, col))

    if row + 1 > len(figure) - 1 or figure[row + 1][col] != "F":
        bottom.append((row, col))

    bottom = findBottom(figure, row + 1, col, visited, bottom)
    bottom = findBottom(figure, row, col - 1, visited, bottom)
    bottom = findBottom(figure, row, col + 1, visited, bottom)

    return bottom

bottom = findBottom(figure, 1, 2, set([]), [])
print(bottom)
global_smallest = float("inf")
for row, col in bottom:
    temp = 0
    while row + 1 <= len(figure) - 1 and figure[row + 1][col] != "#" and figure[row + 1][col] != "F":
        row += 1
        temp += 1
    
    global_smallest = min(global_smallest, temp)

print(global_smallest)
    