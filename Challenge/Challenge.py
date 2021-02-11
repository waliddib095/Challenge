def max_total(file1):
    
    
    lines = file1.readlines()   #read all lines
    
    triangle_matrix = []   #initiate triangle matrix
    
    for line in lines:
        row = line.strip().split()
        triangle_matrix.append(row)   #populate triangle matrix
        
        
    num_of_lines = len(triangle_matrix)   # get number of lines
    
    for row in range(num_of_lines - 2, -1, -1):
        for col in range(row + 1):
            
            # itirate from the line before the last line to the first line
            # itirate through each element from left to right
            
            if num_of_lines == 1:
                return triangle_matrix[0][0]
            
            # Edge case: if triangle has 1 line, print the element
            
            triangle_matrix[row][col] = int(triangle_matrix[row][col])
            
            # Turn char to int
            
            element_1 = int(triangle_matrix[row + 1][col])
            
            element_2 = int(triangle_matrix[row + 1][col + 1])
            
            # get bottom left and bottom right elements
            
            triangle_matrix[row][col] += max(element_1, element_2)  
            
            # add the value of current element to maximum of bot elements
    
    file1.close()   #close file
    
    return triangle_matrix[0][0]   # return total sum


'''
Code Explanation (Dynamic Programming): 
    
    * First start by creating a matrix, in which each row has varying length 
    since we are dealing with a triangle.
    
    * Itirate from the second line (starting from the bottom) to the first
    line.
    
    * The reason I do that is so I can look at the 2 elements below me and 
    compare them.
    
    * Change the value of the current element to the sum of current_element
    + the maximum of both elements I checked below the current element. 
    
    * Keep repeating the same process for all elements until I reach
    element [0][0]
    
    * Return the first elemnt in the matrix where the max sum has aggregated 
    element [0][0]
    
    
    *Time complexity: O(N) where N is the total number of numbers in the triangle
    
    *Space complexity: O(N) where N is the total number of numbers in the triangle

'''
            
        
# Main code      
    
triangle = open("triangle.txt", "r")

max_total(triangle)
