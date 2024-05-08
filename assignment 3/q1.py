import math
import random
def evaluate_sol(solution):
  clauses = [(
    (not solution[0]) or (solution[3])),
    (solution[2] or solution[1]),
    ((not solution[2]) or (not solution[3])),
    ((not solution[3]) or (not solution[1])),
    ((not solution[0]) or (not solution[3]))]
  return sum(clauses)

def movegen(solution):
  var_idx = random.randint(0,len(solution)-1)
  solution_copy = solution[:]
  solution_copy[var_idx] = not solution[var_idx]
  return solution_copy

def accept_badmove(delta,temperature):
  if delta < 0:
    return True
  probability = math.exp(-delta/temperature)
  return random.random() < probability

def simulated_annealing():
  T=500
  cooling_factor = 50
  current_sol = [True,True,True,True]
  current_energy=evaluate_sol(current_sol)
  best_sol = current_sol[:]
  best_energy = current_energy
  while T>0:
    for i in range(cooling_factor):
      new_sol = movegen(current_sol)
      new_energy = evaluate_sol(new_sol)
      delta = new_energy-current_energy
      if delta > 0 or accept_badmove(delta,T):
        current_sol=new_sol[:]
        current_energy=new_energy
        if(new_energy)>best_energy:
          best_sol=new_sol[:]
          best_energy=new_energy
    T-=1
  return best_sol

random.seed(42)
best_solution = simulated_annealing()
print("best solution",best_solution)
print("clauses satisfied",evaluate_sol(best_solution))