#This code was originallyfound here: https://favtutor.com/blogs/avl-tree-python
#but was modified to include search

class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.l = None
        self.r = None
        self.h = 1
        self.pred = None
        self.succ = None 

class AVLTree(object):
    
    def __init__(self):
        self.maxValue = -1;

    def insert(self, root, key):
    
        #if this is the largest insert, then update that
        if key > self.maxValue:
            self.maxValue = key
    
        if not root:    
            return treeNode(key)
        elif key < root.value:
            root.l = self.insert(root.l, key)
            if root.l.succ == None and root.l.pred == None:
                root.l.pred = root
                root.l.succ = root.succ
                root.l.pred.succ = root.l
                if root.l.succ != None:
                    root.l.succ.pred = root.l
        else:
            root.r = self.insert(root.r, key)
            if root.r.succ == None and root.r.pred == None:
                root.r.succ = root
                root.r.pred = root.pred
                root.r.succ.pred = root.r
                if root.r.pred != None:
                    root.r.pred.succ = root.r
                

        root.h = 1 + max(self.getHeight(root.l),
                        self.getHeight(root.r))

        b = self.getBal(root)

        if b > 1 and key < root.l.value:
            return self.rRotate(root)

        if b < -1 and key > root.r.value:
            return self.lRotate(root)

        if b > 1 and key > root.l.value:
            root.l = self.lRotate(root.l)
            return self.rRotate(root)

        if b < -1 and key < root.r.value:
            root.r = self.rRotate(root.r)
            return self.lRotate(root)

        return root

    def lRotate(self, z):

        y = z.r
        T2 = y.l

        y.l = z
        z.r = T2

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def rRotate(self, z):

        y = z.l
        T3 = y.r

        y.r = z
        z.l = T3

        z.h = 1 + max(self.getHeight(z.l),
                        self.getHeight(z.r))
        y.h = 1 + max(self.getHeight(y.l),
                        self.getHeight(y.r))

        return y

    def getHeight(self, root):
        if not root:
            return 0

        return root.h

    def getBal(self, root):
        if not root:
            return 0

        return self.getHeight(root.l) - self.getHeight(root.r)

    def preOrder(self, root):

        if not root:
            return

        print("{0} ".format(root.value), end="")
        self.preOrder(root.l)
        self.preOrder(root.r)

    def find(self, root, val):
        if root == None:
            return None
        
        if val == root.value:
            return root
        elif val < root.value:
            return self.find(root.l, val)
        else:
            return self.find(root.r, val)
        

    def includes(self, root, val):
        return self.find(root, val) != None