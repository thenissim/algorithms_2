### Exercise 3 - q1: Dynamic Programming ###

### Template ###

#import libraries:

#a. main function

def knapsack_bottom_up(items, maximum_weight):

    h = len(items)+1 #height of matrix (number of rows) including first with zero
    w = maximum_weight + 1 #width of matrix (number of columns) including first with max 0
    mat = [[0 for x in range(w)] for y in range (h)] #creating the matrix and filling it with 0
    for item in range(1,h): #first row remains zero
        for weight in range(w):
            if items[item-1][0] > weight: #this item's weight is more than this sub problem capacity
                mat[item][weight] = mat[item-1][weight]
                continue 
            #in every other case:
            prior = mat[item-1][weight]
            #value of the current item + value of remaining weight after inserting curent item
            new_option = items[item-1][1] + mat[item -1][weight - items[item-1][0]]
            mat[item][weight] = max(prior, new_option)  
    total_value = mat[h-1][w-1] #first row and col are zeros 
    packed = []
    #items packed restoration
    cur_weight = maximum_weight
    for item in range (h-1,0,-1): #from last to first
        #if the above cell is equal, current item was not packed
        if mat[item][cur_weight] != mat[item -1][cur_weight]: 
            packed.insert(0,item-1) #current item was packed
            cur_weight -= items[item-1][0]
    return total_value, packed

#b. subset-sum function (remember 3 code line is 3 points extra!)

def subset_sum_algo(numbers, subset_sum):
    items = [(number,number) for number in numbers] #knapsack_bottom_up func is with tuples
    check = knapsack_bottom_up(items, subset_sum) 
    return  check[0] == subset_sum #returns tuple, we only need total_value

