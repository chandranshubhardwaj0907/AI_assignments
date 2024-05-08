from compound_interest_calculator import CalcCompound

principal = int(input("Enter amount: "))
interest = int(input("Enter interest rate: "))
time = int(input("Enter time: "))

print(f"Compound interest is: {CalcCompound(principal, interest, time):.2f}")