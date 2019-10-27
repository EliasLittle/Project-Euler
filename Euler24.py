from functions import getPermutations

lst = getPermutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("Permutations Found")
print("Sorting...")
lst.sort()
print(str(lst[999999]))
