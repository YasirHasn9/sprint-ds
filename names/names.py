
'''
#### Task 2. Runtime Optimization

***!Important!*** If you are running this using PowerShell by 
clicking on the green play button, you will get an error that 
`names1.txt` is not found.  To resolve this, run it, get the error, 
then `cd` into the `names` directory in the `python` terminal that opens in VSCode.

Navigate into the `names` directory. Here you will find two text 
files containing 10,000 names each, along with a program `names.py` 
that compares the two files and prints out duplicate name entries. 
Try running the code with `python3 names.py`. Be patient because it
 might take a while: approximately six seconds on my laptop. What is
  the runtime complexity of this code?

Six seconds is an eternity so you've been tasked with speeding up the
 code. Can you get the runtime to under a second? Under one hundredth of a second?

*You may not use the built in Python list, set, or dictionary in your
 solution for this problem.  However, you can and should use the provided 
 `duplicates` list to return your solution.*

(Hint: You might try importing a data structure you built during the week)
'''


import time


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value:
            return self.right.contains(target) if self.right else False
        else:
            return self.left.contains(target) if self.left else False


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
for name_1 in names_1:
    for name_2 in names_2:
        if name_1 == name_2:
            duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
