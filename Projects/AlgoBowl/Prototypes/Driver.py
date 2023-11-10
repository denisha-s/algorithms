import sys
import Prototypes.LargestNumberProto as ln

inFileName = sys.argv[1] if len(sys.argv) > 1 else "List.txt"
fin = open(inFileName)
lines = fin.readlines()
lineCount = int(lines.pop(0)) #removes the count of lines

#clean them up: removes new line chars, and then casts them to ints
for i in range(lineCount):
    lines[i] = int(lines[i].replace("\n",""))
    
ln.findSums(lines)
