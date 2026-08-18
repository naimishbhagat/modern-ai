def pure_chai(cups):
    return cups * 10

total_chai = 0

#Not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups

def pour_chai(n):
    if n == 0:
        return "All cups poured"
    print(n-1)
    return pour_chai(n-1)

print(pour_chai(3))

#Lambda

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak",chai_types))
print(strong_chai)