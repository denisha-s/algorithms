import random as rand

outFile = 'List.txt'
n = 50
max = pow(10, 3)

fout = open(outFile, 'w')

fout.write(str(n) + "\n")
nums = []

while n > 0:
    randomNumber = rand.randint(2,max)
    if randomNumber not in nums:
        nums.append(rand.randint(2,max))
        n -= 1
    
nums = sorted(nums)

for i in range(len(nums)):
    fout.write(str(nums[i]))
    if i < len(nums)-1: #only put spaces if its not the last one
        fout.write(" ")