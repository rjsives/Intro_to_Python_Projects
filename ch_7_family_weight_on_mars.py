# Create a program to calculate weights on Mars for your entire family.
# The function should ask for each family member's weight, calculate how much they
# would weigh on Mars (by multiplying the number by 0.3782) and then add up and
# display the total weight.

# Defines a list of family members
family = ["Kelly", "Rich", "Lexi", "Cybil", "Clem", "Eddie", "Eli", "Marble", "Jeffrey"]
mars_weight_conversion = 0.3782


def calculate_family_weight():
    total_weight = 0
    for person in family:
        weight = int(input(f"Enter {person}'s weight:"))
        print(f"{person} weighs {weight} lbs on Earth: {round(weight * mars_weight_conversion)} lbs on Mars. \n")
        total_weight = total_weight + weight * mars_weight_conversion
    return round(total_weight)


print(f"Our family's total weight on Mars is {(calculate_family_weight())} lbs.")
