import driverHeader as files
import AVLtree as Tree
import MaxSum as ms
import sys

#finds a set of summations that reach all targets in the targetfile
#returns a dictionary of the summations
def findAllSums(targetFilePath):
    targets = files.readInput(targetFilePath)
    prevSums = Tree.AVLTree()
    root = None
    #insert 1 into the array!
    root = prevSums.insert(root, 1)

    solutionArray = []
    
    targN = 1
    for target in targets: #targets is an array, so this will do an inOrder pass

        while prevSums.maxValue < target:
            maxSumComps = ms.getMaxSums(prevSums, root, target).split()
            maxSum = int(maxSumComps[0]) + int(maxSumComps[1])
            root = prevSums.insert(root, maxSum)
            solutionArray.append(int(maxSumComps[0]))
            solutionArray.append(int(maxSumComps[1]))
            # print(f'{maxSumComps} {maxSum}')
            printProgBar(targN, len(targets))
            
        targN += 1            
        
    solutionFilePath = getOutputFilePath(targetFilePath)
    files.printSolution(solutionFilePath, solutionArray)
    
            
def getOutputFilePath(targetFilePath):
    #go from all_inputs/inputs/'fileName'.txt -> all_inputs/outputs/'fileName'_output.txt
    temp = str(targetFilePath).replace('.txt', '') + "_output.txt"
    return temp.replace('\inputs\\', '\outputs\\')


def printProgBar(i, end_val, bar_length = 20):
    percent = float(i) / end_val
    hashes = '#' * int(round(percent * bar_length))
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()

    

