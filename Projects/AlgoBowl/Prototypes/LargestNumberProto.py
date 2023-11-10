
class Sum:
    def __init__(self, list):
        self.list = list
        self.i = -1 
        self.j = -1
        
    def __str__(self) -> str:
        return str(self.list[self.i]) + " + " + str(self.list[self.j]) + " = " + str(self.getSum())
    
    def getSum(self):
        return self.list[self.i] + self.list[self.j]
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.i == -1:
            self.i = len(self.list) -1
            self.j = len(self.list) -1
            return self
    
        if self.j > 0:
            self.j -= 1
        elif self.i > 0:
            self.i -= 1
            self.j = self.i
        else:
            raise StopIteration
        
        return self


def findSums(list):
    #sort the list
    list = sorted(list)
    print("List has been sorted. Starting to find sums:")
    #create set of possible numbers to add with (binary tree maybe?)
    nums = [1]
    count = 0;
    
    #iteratively
        #find the largest combo of numbers available that do not go over the next target, choose that one
        #once a target is found, move on to the next target
    
    for target in list:
        while nums[len(nums) -1 ] < target:
            largest = 0
            largestS = ""
            for s in Sum(nums):
                if s.getSum() <= target and s.getSum() > largest and s.getSum() not in nums:
                    largestS = str(s)
                    largest = s.getSum()
                    pass
                    
            print(largestS)
            count += 1
            nums.append(largest)
    
    print(f"That took {count} summations to complete.")
    return count