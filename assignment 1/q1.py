class subject:
  marks = []

  def AddMarks(self):
    print("Add marks of 10 students:\n")
    for i in range(10):
      self.marks.append(int(input(f"Student {i+1} : ")))

  def calculate_stats(self):
    highest = max(self.marks)
    lowest = min(self.marks)
    avg = sum(self.marks) / len(self.marks) #len() is for length
    stats = [highest, lowest, avg]

    return stats

#main function below

maths = subject()
science = subject()
english = subject()
IT = subject()

maths.AddMarks()
MathStats = maths.calculate_stats()

print(f"Math Stats:\n\nHighest marks = {MathStats[0]}\n Lowest marks = {MathStats[1]}\n Avg marks = {MathStats[2]}")

science.AddMarks()
SciStats = science.calculate_stats()

print(f"Science Stats:\n\nHighest marks = {SciStats[0]}\n Lowest marks = {SciStats[1]}\n Avg marks = {SciStats[2]}")

english.AddMarks()
SciStats = english.calculate_stats()

print(f"English Stats:\n\nHighest marks = {SciStats[0]}\n Lowest marks = {SciStats[1]}\n Avg marks = {SciStats[2]}")

IT.AddMarks()
ITStats = IT.calculate_stats()

print(f"IT Stats:\n\nHighest marks = {ITStats[0]}\n Lowest marks = {ITStats[1]}\n Avg marks = {ITStats[2]}")