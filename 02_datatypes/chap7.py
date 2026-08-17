#Set

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices

print(f"Union: {all_spices}")

all_spices = essential_spices & optional_spices
print(f"Intersection: {all_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}")


print(f"Is 'cloves' in essential spices? {'cardamom' in essential_spices}")
