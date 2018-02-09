# Assignment 4: TeamOne
def maxMin(inputList):
    myMin = min(inputList)
    myMax = max(inputList)
    maxMinTuple = (myMin, myMax)
    print(maxMinTuple)
    return maxMinTuple
     
def add_list_numbers(list_var):
    final_sum = 0
    for i in list_var:
        final_sum += i
    return final_sum
  
if __name__ == "__main__":
    main()
 