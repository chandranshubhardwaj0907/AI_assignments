# PART A
class Restaurant:
  def __init__(self, rname, food):
    self.restaurant_name = rname
    self.cuisine_type = food

  def describe_restaurant(self):
    print(f"Resturant name is: {self.restaurant_name}")
    print(f"cuisine type is: {self.cuisine_type}")

  def open_restaurant(self):
    print("The resturant is OPEN!")

r1 = Restaurant("The Marriot", "Drinks")
r1.describe_restaurant()
r1.open_restaurant()

# PART B
class User:
  def __init__(self, firstName, lastName, age, mobileNumber):
    self.FirstName = firstName
    self.LastName = lastName
    self.Age = age
    self.MobileNumber = mobileNumber

  def describe_user(self):
    print(f"User's name: {self.FirstName} {self.LastName}")
    print(f"User's age: {self.Age}")
    print(f"User's mobile number: {self.MobileNumber}")

  def greet_user(self):
    print(f"Hello {self.FirstName}, how's your day.")

u1 = User('Chandranshu', 'Bhardwaj', 20, 104905838)
u1.describe_user()
u1.greet_user()

u2 = User('Ashmit', 'Thawait', 19, 968395820)
u2.describe_user()
u2.greet_user()

u1 = User('Aryan', 'Bansal', 20, 295957828)
u1.describe_user()
u1.greet_user()