%%writefile compound_interest_calculator.py

def CalcCompound(principal, interest, time):
  r = interest / 100 #converting to decimal from %
  amount = principal*((1+r)**time)
  cInterest = amount - principal
  return cInterest