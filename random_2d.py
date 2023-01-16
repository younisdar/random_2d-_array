import random

def create_2d_list(numberOfRows, numberOfColumns):
   
    my_list = [[0 for i in range(numberOfColumns)] for j in range(numberOfRows)]

    
    for i in range(numberOfRows):
        for j in range(numberOfColumns):
            my_list[i][j] = random.randint(0, 100)

    return my_list
    

