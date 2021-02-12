lines = open("triangle.txt", "r").readlines()   
    
triangle_matrix = []   
    
for line in lines:
    row = line.split()
    triangle_matrix.append(row) 


dic = {}
def max_total(triangle_matrix, row, col):

    if (row, col) in dic:
        return dic[(row,col)]

    cur_val = int(triangle_matrix[row][col])

    if row == len(triangle_matrix) - 1:
        return cur_val

    left_val = max_total(triangle_matrix, row+1, col)
    dic[(row+1, col)] = left_val
    
    right_val = max_total(triangle_matrix, row+1, col+1)
    dic[(row+1, col+1)] = right_val

    return cur_val + max(left_val, right_val)
    
max_total(triangle_matrix, 0, 0)