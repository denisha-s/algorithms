"""

Update version can Run with town more than 1 letter

But fail when start and end contain multiple branch

#### start option:   "A_B"      "A_Q"     "A_P"
#### end option  :   "Db_Dp"    "Do_Dp"
#TstartPair = "A_Q"
#TfinalPair = "Do_Dp"



"""


import sys
# import networkx as nx
# import matplotlib.pyplot as plt


filein = sys.argv[1]


# filein = "input.txt"
# filein = "BFS.txt"
with open(filein,"r") as rf:
   rln = rf.readlines()

lscol0 = [mm.split()[0] for mm in rln[1:]]
lscol1 = [mm.split()[1] for mm in rln[1:]]

ls0    = rln[0].rstrip().split()
Tstart = ls0[2]
Tend   = ls0[3]


lsTstartPair = []
lsTfinalPair = []
for ii in rln[1:]:
   ii1 = ii.rstrip().split()
   if Tstart==ii1[0]:
      lsTstartPair += ["{}_{}".format(Tstart,ii1[1]) ]
   if Tstart==ii1[1]:
      lsTstartPair += ["{}_{}".format(Tstart,ii1[0]) ]
   if Tend==ii1[1]:
      lsTfinalPair += [ "{}_{}".format(ii1[0],Tend) ]
   if Tend==ii1[0]:
      lsTfinalPair += [ "{}_{}".format(ii1[1],Tend) ]

print ("\n")
print ("   Possible Pair start:",lsTstartPair)
print ("   Possible Pair end:",lsTfinalPair)




#if Tstart in lscol0: TstartPair = "{}_{}".format(Tstart , lscol1[lscol0.index(Tstart)])
#if Tstart in lscol1: TstartPair = "{}_{}".format(Tstart , lscol0[lscol1.index(Tstart)])
#
#if Tend in lscol0: TfinalPair = "{}_{}".format(lscol1[lscol0.index(Tend)] , Tend)
#if Tend in lscol1: TfinalPair = "{}_{}".format(lscol0[lscol1.index(Tend)] , Tend)




#### start option:   "A_B"      "A_Q"     "A_P"
#### end option  :   "Db_Dp"    "Do_Dp"
#TstartPair = "A_Q"
#TfinalPair = "Do_Dp"

#print ('start from: {}    end: {}'.format(TstartPair,TfinalPair))



## create dictionary 2 ways that contain property
dpath = {}   ### key = TownFrTo _ TownToFr = [Color,linetype]

dconnect = {}   ### key = "c"/"t" _ Color/linetype _ Town _ Color/linetype       --> value = [destinasi kota]   pas nyari kota darinya dihilangkan di list

for i in rln[1:]:
   ii = i.rstrip().split()
   
   
   ky1 = "{}_{}".format(ii[0],ii[1])
   ky2 = "{}_{}".format(ii[1],ii[0])
   prop = [ii[2],ii[3]]
   
   if ky1 not in dpath: dpath[ky1]=prop
   else: print ("  double entry read already exist ",ii)
   
   if ky2 not in dpath: dpath[ky2]=prop
   else: print ("  double entry read already exist ",ii)
   
   ########    kota + color + (RGB)   -- value kota dest
   con1     = "{}_{}_{}".format('c',ii[0],ii[2])
   ########    kota + type + (HCTB)   -- value kota dest
   con2     = "{}_{}_{}".format('t',ii[0],ii[3])
   if con1 in dconnect: dconnect[con1] += [ii[1]]
   else               : dconnect[con1]  = [ii[1]]
   if con2 in dconnect: dconnect[con2] += [ii[1]]
   else               : dconnect[con2]  = [ii[1]]

   ########    kota + color + (RGB)   -- value kota dest
   con3     = "{}_{}_{}".format('c',ii[1],ii[2])
   ########    kota + type + (HCTB)   -- value kota dest
   con4     = "{}_{}_{}".format('t',ii[1],ii[3])
   if con3 in dconnect: dconnect[con3] += [ii[0]]
   else               : dconnect[con3]  = [ii[0]]
   if con4 in dconnect: dconnect[con4] += [ii[0]]
   else               : dconnect[con4]  = [ii[0]]
   



#for ky in dpath:
#   print (ky, dpath[ky])
#   # B_A ['R', 'C']
#   # A_B ['R', 'C']
#   # B_E ['B', 'C']
#   # E_B ['B', 'C']
#   # B_C ['B', 'T']
#   # C_B ['B', 'T']
#   # C_D ['G', 'T']
#   # D_C ['G', 'T']
#   
#for ky in dconnect:
#   print ("---",ky, dconnect[ky])
#   # --- c_B_R ['A', 'F']
#   # --- t_B_C ['A', 'E']
#   # --- c_A_R ['B']
#   # --- t_A_C ['B']
#   # --- c_B_B ['E', 'C']
#   # --- c_E_B ['B']
#   # --- t_E_C ['B', 'O']
#   # --- t_B_T ['C', 'F']
#   # --- c_C_B ['B']
#   # --- t_C_T ['B', 'D']
#   # --- c_C_G ['D']
  

def findnextTown(findnext):
   findnext1 = findnext.split("_")[1]
   findnext0 = findnext.split("_")[0]
   
   
   #lsTfound1 = dconnect["{}_{}_{}".format('c',findnext1,dpath[findnext][0])]   ### find next town from findnext0_findnext1
   #lsfound1 = []                   ### combine next find town with end of first town
   #for kk in lsTfound1:
   #   lsfound1 += [ "{}_{}".format(findnext1,kk) ]
   
   
   lsfound1 = [ "{}_{}".format(findnext1,kk) for kk in  dconnect["{}_{}_{}".format('c',findnext1,dpath[findnext][0])] ]
   if "{}_{}".format(findnext1,findnext0) in lsfound1:  lsfound1.remove("{}_{}".format(findnext1,findnext0))
   
   lsfound2 = [ "{}_{}".format(findnext1,kk) for kk in  dconnect["{}_{}_{}".format('t',findnext1,dpath[findnext][1])] ]
   if "{}_{}".format(findnext1,findnext0) in lsfound2:  lsfound2.remove("{}_{}".format(findnext1,findnext0))
   
   for kk in lsfound2:
      if kk not in lsfound1: lsfound1+= [kk]

   return lsfound1


### Make Dictionary with key=TownFrTo and value=next TownFrom(end of town key search) to Next Town
adj_list = {}
for i in rln[1:]:
   ii = i.rstrip().split()
   
   #print ( "{}_{}".format(ii[0]+ii[1]) , findnextTown( "{}_{}".format(ii[0]+ii[1]) ) )
   #print ( "{}_{}".format(ii[1]+ii[0]) , findnextTown( "{}_{}".format(ii[1]+ii[0]) ) )
   
   lsres1 = findnextTown( "{}_{}".format(ii[0],ii[1]) )
   lsres2 = findnextTown( "{}_{}".format(ii[1],ii[0]) )
   #if lsres1 != []: adj_list[ ii[0]+ii[1] ] = lsres1
   #if lsres2 != []: adj_list[ ii[1]+ii[0] ] = lsres2
   
   adj_list[ "{}_{}".format(ii[0],ii[1]) ] = lsres1
   adj_list[ "{}_{}".format(ii[1],ii[0]) ] = lsres2



###########################################################################
###########################################################################
######   this part start to calculate possible path by combination
######      and then select the smallest
###########################################################################
###########################################################################


nominpath = 9999999999999999999999999999999.

from queue import Queue

pathresultfinal = "NO PATH"

for istartpair in lsTstartPair:
   for ifinalpair in lsTfinalPair:
      
      
      TstartPair = istartpair
      TfinalPair = ifinalpair
      print ('\n==========   Version From:"{}" to "{}"   =========='.format(TstartPair,TfinalPair))

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
      
      
      #shortest path of from  any node from source code
      #v = 'ij'
      path = []
      while TfinalPair is not None:
         path.append(TfinalPair)
         TfinalPair = parent[TfinalPair]
      path.reverse()
      
      #print (path)
      #
      if path == [] or len(path)<= 1: pathresult = 'NO PATH'
      else                          : 
         lspath     = [ll.split("_")[0] for ll in path]
         pathresult = " ".join(lspath) + " " + path[-1].split("_")[-1]
      
      print ( "          no Town Transit : {}".format(len(path)) )
      print ( "          Shortest Path -->",pathresult  )
      
      #### this is to select final path
      if path == [] or len(path)<= 1: pass #pathresultfinal = "NO PATH"
      else :
         if len(path) < nominpath:
            nominpath = len(path)
            pathresultfinal = " ".join(lspath) + " " + path[-1].split("_")[-1]


print ("\n\n\n\n")
print ("   FINAL  Shortest Path -->", pathresultfinal)

