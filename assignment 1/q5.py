D= {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
  }

print(f"D initially: {D}")
D[6] = "Six"
print(f"D after adding 6: {D}")

D.pop(2)
print(f"D after removing 2: {D}")

if 6 in D:
  print("6 is present in D")
else:
  print("6 is not present in D")

print(f"total no of elements present in D is: {len(D)}")

TotalSum = sum(D.keys())
print(f"Total sum of keys of D: {TotalSum}")