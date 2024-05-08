L =  [10, 20, 30, 40, 50, 60, 70, 80]

print(f"L initially:\t{L}")
L.extend([200, 300])
print(f"L after adding 200 and 300:\t{L}")
L.remove(10)
print(f"L after removing 10:\t{L}")
L.remove(30)
print(f"L after removing 30:\t{L}")
L.sort()
print(f"L in ascending order:\t{L}")
L.reverse()
print(f"L in descending order:\t{L}")
