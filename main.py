# Assignment 4: TeamOne
def main():
    maxMin([2,5,6])

def maxMin(inputList):
    myMin = min(inputList)
    myMax = max(inputList)
    maxMinTuple = (myMin,myMax)
    print(maxMinTuple)
    return maxMinTuple


if __name__ == "__main__":
    main()
