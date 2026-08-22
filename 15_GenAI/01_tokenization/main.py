import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "Hey There! My name is Naimish Bhagat"
tokens = enc.encode(text)
print("Tokens: ",tokens)

decoded_text = enc.decode([25216, 3274, 0, 3673, 1308, 382, 478, 4441, 1109, 29182, 73457])
print("Decoded Text: ", decoded_text)