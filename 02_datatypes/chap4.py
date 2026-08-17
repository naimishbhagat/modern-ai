chai_type = "Ginget chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and bold"

print(chai_description[-1])
print(chai_description[0:8:2])
print(chai_description[::-1]) # reverse

label_text = "Chai Special"

encoded_label = label_text.encode("utf-8")
print(encoded_label)
decoded_label = encoded_label.decode("utf-8")
print(decoded_label)
