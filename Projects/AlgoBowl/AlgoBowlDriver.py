import sys
import LargestNumber as ln
import Prototypes.Verification as v

if(len(sys.argv) != 2):
    print("Usage: python3 AlgoBowlDriver <target filePath>")
    exit(0)
    
ln.findAllSums(sys.argv[1])
valid = v.verify(open(sys.argv[1]), open(ln.getOutputFilePath(sys.argv[1])))
if not valid:
    print("Err: the output created was not valid.")
    