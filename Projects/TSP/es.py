import sys
import timeit

start = timeit.default_timer()

#data = "data.txt"

### read data to list
def readfile(filein):
   with open(filein,"r") as rf:
      rln = rf.readlines()
    
   nline = int(rln[0].strip())
   
   lspts = []
   for i in range(nline):
      readdata = [int(j) for j in rln[i+1].strip().split()] # list comprehension 4 di dalem list
      lspts += [readdata]
      #print (readdata)
   return lspts # stores in list set

### find distance
def distance(p1,p2):
   " find distance from p1 to p2 "
   dist = ( (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 ) ** 0.5
   return dist


def findclosest(p1,lsp):
   " find closest distance from p1 to list of points lsp "
   distinit = 10e10
   ptfound = []
   distfound = 0
   idxfound  = 0
   iidx = -1
   for p2 in lsp:
      iidx += 1
      dist = distance(p1,p2)
      if dist < distinit: 
         distinit = dist
         ptfound   = p2
         distfound = dist
         idxfound  = iidx
   
   return ptfound,distfound,idxfound


def main_NN(lspts): #nearest neighbor

   totdist  = 0
   pointseq = [lspts[0]]

   for i in range(len(lspts)-1):
      if i==0:
         #print (i)
         
         lssearch = lspts[1:]
         p1,d,idxf = findclosest(lspts[0],lssearch)
         #print (lspts[0],lssearch,idxf,d,p1)
         
         totdist  += d
         pointseq += [p1]
         
         #print ("totdist:",totdist)
         
      else:
         #print ("\n-----",i)
         del lssearch[idxf]
         #print (p1,lssearch)
         
         p1,d,idxf = findclosest(p1,lssearch)
         #print ("   found:",idxf,p1,d)
         
         #print ("tot dist before add:",totdist)
         totdist  += d
         #print ("totdist:",totdist)
         pointseq += [p1]
      
   ### count back to initial index 0
   #print ("end:",p1)
   d = distance(p1,lspts[0])
   totdist  += d

   print ("\nTotal distance = {:.3f}".format(totdist))
   print (pointseq+[lspts[0]])
   
   return totdist,pointseq+[lspts[0]]
   
   
def main_Distance(lspts):
   
   totdist  = 0
   for i in range(len(lspts)-1):
      d = distance(lspts[i],lspts[i+1])
      totdist += d
   ### count back to 0
   d = distance(lspts[i+1],lspts[0])
   totdist += d
   
   #print (totdist)
   
   return totdist
   
   
# exhaustive search
filein = sys.argv[1]
lsptsr = readfile(filein)

if False:
   main_NN(lsptsr)
if True:
   TotDistMin = 10e10
   seqselect  = ""
   
   lsidx = [ i for i in range(len(lsptsr))]
   # ambil index aja
   
   import itertools 
   # to use premutation
   
   permutation = list(itertools.permutations(lsidx[1:],len(lsidx)-1)) # ambil index yg dari 1 since 0 is fixed then add (0,0) at the end
   for lsidx in permutation:                                          # do not hardcode use len
      #print ("\n========================")
      lsptsi = [lsptsr[0]] + [lsptsr[j] for j in lsidx] # list comprehension
      #print (lsidx , lsptsi )
   
      totdisti = main_Distance(lsptsi)
      #print ("     ",totdisti)
      
      if totdisti<TotDistMin: # simpen dulu point that's less that 10e10
         TotDistMin = totdisti
         seqselect  = lsptsi # sequence select

   print("{:.3f}".format(TotDistMin))
   #print ("\nExhaustive --> min distance {:.3f}    seq = {}".format(TotDistMin,seqselect))
   
#print ("\n\n  Processing time {:.9f} secs\n\n".format(timeit.default_timer()-start))
