import AVLtree as Tree

def getMaxSums (prevSums, root, target):
    #CASE 1: a perfect sum already exists:
    #need to itterate first, starting at the max, and going though successors (for loop?)
    first = prevSums.maxValue
    while True:
        second = target - first

        if prevSums.includes(root, second):
            return f'{first} {second}'
        elif first == 1: # Always 1
            break
        elif first != 1: 
            first = prevSums.find(root, first).succ.value

    #Small side note, recursively call to solve for the diff as a stepping stone if it doesnt exist and is within the threshold
    
    #CASE 2: Do the nested for loop to find the maximum possible sum
    #first, find the max sum possible with the max prevSum
    maxNode = prevSums.find(root, prevSums.maxValue)
    secondNode = maxNode
    maxPrevSumVal = 0
    maxPrevSumString = ""
    while(secondNode.value > 1):
        curSum = maxNode.value + secondNode.value
        if(curSum > maxPrevSumVal and curSum < target):
            maxPrevSumVal = curSum
            maxPrevSumString = f'{maxNode.value} {secondNode.value}'
        secondNode = secondNode.succ
    
    
    #do the iteration around the rest of them
    maxIterSum = 2
    maxIterString = "1 1"

    firstNode = prevSums.find(root, prevSums.maxValue)
    if firstNode.value != 1:
        firstNode = firstNode.succ
        secNode = firstNode
        while True:
            if firstNode.value + secNode.value < target:
                maxIterSum = firstNode.value + secNode.value
                maxIterString =  f'{firstNode.value} {secNode.value}'
                break

            if firstNode.value == 1:
                firstNode = firstNode.succ
                secNode = firstNode
            elif firstNode.value + secNode.succ.value > (firstNode.succ.value)*2:
                secNode = secNode.succ
            else:
                firstNode = firstNode.succ
                secNode = firstNode
            
    #now, return the bigger of the two
    if(maxPrevSumVal > maxIterSum):
        return maxPrevSumString
    else:
        return maxIterString


# prevSums = Tree.AVLTree()
# root = prevSums.insert(None, 1)
# #root = prevSums.insert(root, 3) 
# #root = prevSums.insert(root, 5)

# t = 9
# string = getMaxSums(prevSums, root, t)
# print(string)
# # print(root.pred)
# # print(root.succ)



