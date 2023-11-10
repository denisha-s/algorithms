class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)
# findval method to compare the value with nodes
    def exists(self, val):
        
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)
      
def verify(fileTarget, fileSolution):
#file1 = open("algoin.txt", "r")
  #read in the target file and split it
  inputLines = fileTarget.readlines()
  origInpCnt = inputLines[0]
  targetItems = inputLines[1].split()

  # check if there are the correct amount 
  ##print(inputLines[0])
  ##print(len(targetItems))
  if (int(inputLines[0]) != len(targetItems)):
    return False
  
  #print(targetItems[0]) # #print count of targets
  #print(inputLines[1]) #

  # initializing arrays
    #instead of having arrays use trees 
    # search tree to find sol1 and sol2 and add them together to get solution
    #with 50 numbers its too slow - max of 1000
  sol1 = []
  sol2 = []
  solAdd = []

  #reads in solution file
  solutionLines = fileSolution.readlines()
  #print (solutionLines)
  solCnt = solutionLines[0]
  root = BSTNode(solCnt)
  
  #check that there are the correct number of solutions
  if (int(solutionLines[0]) != len(solutionLines) -1):
    return False
    
  #print(solCnt)
  
  for j in range(1, int(solCnt)+1):
    # maps row by row input from solutions 
    inpsol =  solutionLines[j].split()
    #print(inpsol[0] +" sols "+ inpsol[1])
    # append solutions to array
    sol1.append(int(inpsol[0]))
    sol2.append(int(inpsol[1]))
    # add the 2 together to store the result
    #solAdd.append(float(inpsol[0])+float(inpsol[1]))
    root.insert(str(int(inpsol[0])+int(inpsol[1])))
  ##prints the solutions and results   
  #for j in range(0, int(solCnt)):
    #print(sol1[j], sol2[j],solAdd[j])
  #solItems = solutionLines[1].split()
    
  # converted results into a list  
  #trg_list = list(solAdd)
  ##print(trg_list)
  
  #loop through targets
  for trg in targetItems:
    #print(str(trg) + str(trg_list.count(int(trg))))
    #print("trg"+str(trg))
    #counts how many times the target is in the list
    #if trg_list.count(int(trg)) == 0:
    if root.exists(str(trg))==False:
      #target is not there 
      print(str(trg) + " not found") 
      #print("trg false")
      return False
      
  for search1 in sol1:
    #print(str(search1) + str(trg_list.count(int(search1))))
    #counts how many times the target is in the list
    #if trg_list.count(int(search1)) == 0 and int(search1) != 1:
    #print("search1"+str(search1))
    if root.exists(str(search1))==False and int(search1) != 1:
      #target is not there 
      print(str(search1) + " not found") 
      #print("search1 false")
      return False

  for search2 in sol2:
    #print(str(search2) + str(trg_list.count(int(search2))))
    #counts how many times the target is in the list
    #if trg_list.count(int(search2)) == 0 and int(search2) != 1:
    #print("search2"+str(search2))
    if root.exists(str(search2))==False and int(search2) != 1:
      #target is not there 
      print(str(search2) + " not found") 
      #print("search2 false"+str(search2))
      return False
      
  return True
