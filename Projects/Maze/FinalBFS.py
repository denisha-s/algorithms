
import sys
import networkx as nx

data = sys.argv[1]


with open(data,"r") as rf:
   rln = rf.readlines()

lscol0 = [mm.split()[0] for mm in rln[1:]]
lscol1 = [mm.split()[1] for mm in rln[1:]]

ls0    = rln[0].rstrip().split()
Tstart = ls0[2]
Tend   = ls0[3]

if Tstart in lscol0: TstartPair = Tstart + lscol1[lscol0.index(Tstart)]
if Tstart in lscol1: TstartPair = Tstart + lscol0[lscol1.index(Tstart)]



#TfinalPair  = 'mn'
#print ('start from: {}    end: {}'.format(TstartPair,TfinalPair))



## create dictionary 2 ways that contain property
dpath = {}   ### key = AB / BA = [Color,linetype]

dconnect = {}   ### key = Node+Color / linetype     value = [destinasi kota]   pas nyari kota darinya dihilangkan di list

for i in rln[1:]:
   ii = i.rstrip().split()
   
   
   ky1 = ii[0]+ii[1]
   ky2 = ii[1]+ii[0]
   prop = [ii[2],ii[3]]
   
   if ky1 not in dpath: dpath[ky1]=prop
   else: print ("  double entry read already exist ",ii)
   
   if ky2 not in dpath: dpath[ky2]=prop
   else: print ("  double entry read already exist ",ii)
   
   ########    kota + color + (RGB)   -- value kota dest
   con1     = 'c'+ii[0]+ii[2]
   ########    kota + type + (HCTB)   -- value kota dest
   con2     = 't'+ii[0]+ii[3]
   if con1 in dconnect: dconnect[con1] += [ii[1]]
   else               : dconnect[con1]  = [ii[1]]
   if con2 in dconnect: dconnect[con2] += [ii[1]]
   else               : dconnect[con2]  = [ii[1]]

   ########    kota + color + (RGB)   -- value kota dest
   con3     = 'c'+ii[1]+ii[2]
   ########    kota + type + (HCTB)   -- value kota dest
   con4     = 't'+ii[1]+ii[3]
   if con3 in dconnect: dconnect[con3] += [ii[0]]
   else               : dconnect[con3]  = [ii[0]]
   if con4 in dconnect: dconnect[con4] += [ii[0]]
   else               : dconnect[con4]  = [ii[0]]
   


def findnextTown(findnext):
   lsfound1 = [findnext[1]+kk for kk in dconnect['c'+findnext[1]+dpath[findnext][0]]]
   lsfound2 = [findnext[1]+kk for kk in dconnect['t'+findnext[1]+dpath[findnext][1]]]
   
   if findnext[1]+findnext[0] in lsfound1 : lsfound1.remove(findnext[1]+findnext[0])
   if findnext[1]+findnext[0] in lsfound2 : lsfound2.remove(findnext[1]+findnext[0])
   
   for kk in lsfound2:
      if kk not in lsfound1: lsfound1+= [kk]
   
   return lsfound1


#print ( findnextTown('ab') )

adj_list = {}
for i in rln[1:]:
   ii = i.rstrip().split()
   
   #print (ii[0]+ii[1] , findnextTown(ii[0]+ii[1]))
   #print (ii[1]+ii[0] , findnextTown(ii[1]+ii[0]))
   
   lsres1 = findnextTown(ii[0]+ii[1])
   lsres2 = findnextTown(ii[1]+ii[0])
   #if lsres1 != []: adj_list[ ii[0]+ii[1] ] = lsres1
   #if lsres2 != []: adj_list[ ii[1]+ii[0] ] = lsres2
   
   adj_list[ ii[0]+ii[1] ] = lsres1
   adj_list[ ii[1]+ii[0] ] = lsres2

from queue import Queue

#bfs code
visited = {}
level   = {}
parent  = {}
bfs_traversal_output = [] 
queue = Queue()

for node in adj_list.keys():
   visited[node] = False
   parent[node] = None
   level[node] = -1
   
   
#TstartPair = 'AB'
visited[TstartPair] = True
level[TstartPair] = 0
queue.put(TstartPair)

while not queue.empty():
   u = queue.get()
   bfs_traversal_output.append(u)
   
   for v in adj_list[u]:
      try:
       if not visited[v]:
         visited[v] = True
         parent[v] = u
         level[v] = level[u]+1
         queue.put(v)
      except:
       pass
         
#print (bfs_traversal_output)


#shortest path of from  any node from source code

TfinalPair = ""

if Tend in lscol0: TfinalPair = lscol1[lscol0.index(Tend)] + Tend
if Tend in lscol1: TfinalPair = lscol0[lscol1.index(Tend)] + Tend

if len(TfinalPair) == 2:


#v = 'ij'
   path = []
   while TfinalPair is not None:
      path.append(TfinalPair)
      TfinalPair = parent[TfinalPair]
   path.reverse()


   if path == [] or len(path)<= 1: pathresult = 'NO PATH'
   else                          : 
      lspath = [ll[0] for ll in path]
      pathresult = " ".join(lspath) + " " + path[-1][-1]

else:
   pathresult = "NO PATH"
   # print (path)


print(pathresult)

