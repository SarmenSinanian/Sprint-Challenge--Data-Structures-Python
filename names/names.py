import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Create root node
binary_search_tree = BinarySearchTree(names_1[0])

# Create empty duplicate array
duplicates = []

# Start for loop at 2nd item (item after root which was used to create the tree)
for item in names_1[1:]:
# Insert items iteratively into the binary search tree
    binary_search_tree.insert(item)
# Start for loop at first item because searching tree, not making tree
for item in names_2:
# Check if tree contains item
    if binary_search_tree.contains(item):
# Add item to duplicates array if item is within tree (aka duplicate item)
        duplicates.append(item)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# Starter code has a time complexity of O(n^2)

# duplicates = []
# # for name_1 in names_1:
# #     for name_2 in names_2:
# #         if name_1 == name_2:
# #             duplicates.append(name_1)


# Time complexity of O(n log n)

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
