class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

#Create object from class Chai

masala = Chai()
print(f"Masala Origin: {masala.origin}")
print(f"Masala is Hot: {masala.is_hot}")

masala.is_hot=False
print(f"Class Is Hot: {Chai.is_hot}")
print(f"Masala is Hot: {masala.is_hot}")

masala.flavor = "Masala"

print(masala.flavor)