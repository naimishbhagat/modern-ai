# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

value = 13
if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")

available_sizes = ["small", "medium", "large"]

if (requestd_size := input("Enter you chai cup suze: ")) in available_sizes:
    print(f"Serving {requestd_size} chai")
else:
    print(f"Size is unavailable - {requestd_size}")

flavours = ["masala", "ginger", "lemon", "mint"]
print("Available flavours: ",flavours)

while(flavor := input("Enter flavour: ")) not in flavours:
    print(f"Sorry , {flavor} is not available")
print(f"You choose {flavor} chai")