import sys
import timeit

start = timeit.default_timer()

data = sys.argv[1]

#data = "data.txt"

### read data to list
with open(data,"r") as rf:
   rln = rf.readlines()

nline = int(rln[0].strip())

lspts = []
for i in range(nline):
   readdata = [int(j) for j in rln[i+1].strip().split()]
   lspts += [readdata]
   #print (readdata)


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
      
      #print ("tot dist before adding:",totdist)
      totdist  += d
      #print ("totdist:",totdist)
      pointseq += [p1]
   
### count back to initial index 0
#print ("end:",p1)
d = distance(p1,lspts[0])
totdist  += d

print ("{:.3f}".format(totdist))
#print (pointseq+[lspts[0]])

#print ("\n\nProcessing time {:.9f} secs\n\n".format(timeit.default_timer()-start))