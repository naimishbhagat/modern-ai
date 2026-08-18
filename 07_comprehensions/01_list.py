menu = [
    "Masala chai",
    "Iced lemon tea",
    "Green Tea",
    "Iced Peach tea",
    "Ginger chai"
]

#iced_tea = [tea for tea in menu if "tea" in tea]
iced_tea = [tea for tea in menu if len(tea) > 12]
print(iced_tea)