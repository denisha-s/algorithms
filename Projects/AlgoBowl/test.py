# import AVLtree as Tree

# tree = Tree.AVLTree()
# root = None

# root = tree.insert(root, 1)
# root = tree.insert(root, 2)
# root = tree.insert(root, 3)
# root = tree.insert(root, 4)
# root = tree.insert(root, 5)

# tmp = tree.find(root, 5)

# if tree.includes(root, 5):
#     print("success")
# else:
#     print("fail")



import LargestNumber as ln
ln.findAllSums("List.txt")

import Prototypes.Verification as Ver
print(Ver.verify(open("List.txt"), open("List_output.txt")))