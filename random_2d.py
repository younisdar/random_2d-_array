import random

def create_2d_list(nRows, nColumns):
    R_list = [[0 for i in range(nColumns)] for j in range(nRows)]
    for i in range(nRows):
        for j in range(nColumns):
            R_list[i][j] = random.randint(0, 100)
    return R_list
    
