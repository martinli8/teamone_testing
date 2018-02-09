# Assignment 4: TeamOne
'\n'
def max_diff(my_list):
    n = 0
    for i in range(len(my_list)-1):
        diff = abs(my_list[i+1] - my_list[i])
        if diff > n:
            n = diff
    return n
