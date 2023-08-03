#Create a program to calculate weights on Mars for your entire family. The function should ask for each family member's weight, calculate how much they would weigh on Mars (by multiplying the number by 0.3782) and then add up and display the total weight.

family = ["Kelly", "Rich", "Lexi", "Cybil", "Eddie", "Eli"]
moon_weight_conversion = 0.3782

def calculate_family_weight():
  total_weight = 0
  for person in family:
    weight = int(input(f"Enter {person}'s weight:"))
    total_weight = total_weight + weight*0.3782
  return total_weight

print(calculate_family_weight())