#problem is robot want to get to the bottom right of the matrix

"""
1 2 3
4 5 6
7 8 9
ans= (0,0) => (1,1) => (2,2) =15  because (1+5+9)

"""

"""
1 2 3 
5 4 9 
7 6 8 
ans= 27 (1 => 5=> 7=> 6=> 8)

"""






def is_within_grid(r,c,rows,cols):
    return 0<=r<rows and 0<=c<cols

def get_neibghours(i,j,rows,cols):
    direction_list=[(1,0),(0,1),(1,1)] # this will give us the neibghours(down,right,diagnoal) of the element in matrix
    return [(r,c) for di,dj in direction_list  if is_within_grid(r:=i+di,c:=j+dj,rows,cols)]

def argmax(lst):
    return lst.index(max(lst))

def get_path_sum(matrix,r=0,c=0):
    total_sum=matrix[r][c]
    rows,cols=len(matrix),len(matrix[0])
    if not (positions:=get_neibghours(r,c,rows,cols)):
        return total_sum
    values=[matrix[i][j] for  i,j in positions]
    r,c=positions[argmax(values)]
    total_sum+=get_path_sum(matrix,r,c)
    return total_sum
