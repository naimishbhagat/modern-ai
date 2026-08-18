def make_chai():
    return "Here is your masala chai"

return_value = make_chai()

print(return_value)

def ideal_chaiwala():
    pass

print(ideal_chaiwala)

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "chai is ready"

print(chai_status(0))
print(chai_status(5))

def chai_report():
    return 100,20,10

sold, remaining,_ = chai_report()
print(sold)
print(remaining)