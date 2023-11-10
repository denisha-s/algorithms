def readInput(targetFilePath):
    f = open(targetFilePath)
    numPoints = int(f.readline())
    digits = f.readline().split(" ")
    digits = [int(i) for i in digits] #convert to ints!
    return digits

def printSolution(solutionFilePath, solutionArray):
    with open(solutionFilePath, 'w') as f:
        nums = solutionArray
        totalNums = len(nums)
        i = 0
        f.write(f'{int(totalNums/2)}\n')
        while i < totalNums:
            f.write(f'{nums[i]} {nums[i+1]}\n')
            i = i+2
