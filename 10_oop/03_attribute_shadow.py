class Chai:
    temperature = "hot"
    strength="Strong"

cutting = Chai()
print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "Small"
print("After Chaning",cutting.temperature)
print("Cup size is",cutting.cup)
print("Direct look into the class ",Chai.temperature)

del cutting.temperature
del cutting.cup

print(cutting.temperature)
print(cutting.cup)
