import random

def isPrime(num):
  if num < 2:
    return False
  #here int(num**0.5) + 1 is used to check for all divisors till the square root of the number
  #this is for optimisation so not all factors need to be checked
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False
  return True

RandNumbers = OddNum = EvenNum = PrimeNum = []

for _ in range(100):
  RandNumbers.append(random.randint(100,900))

for num in RandNumbers:
  if num % 2 == 0:
    EvenNum.append(num)

for num in RandNumbers:
  if num % 2 != 0:
    OddNum.append(num)

for num in RandNumbers:
  if isPrime(num):
    PrimeNum.append(num)

print(f"All Odd Numbers: {OddNum}")
print(f"All even numbers: {EvenNum}")
print(f"All prime numbers: {PrimeNum}")