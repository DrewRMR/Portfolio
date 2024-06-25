import hashlib

strings = ["test"]
#    "Hello, world!",
#    "This is my test dictionary",
#    "This is going to look very strange shortly!",
#]

hash_dict = {}
for string in strings:
    hash_value = hashlib.sha512(string.encode()).hexdigest()
    hash_dict[string] = hash_value
    
for key, val in hash_dict.items():
    print(f"{key:<5}{val:>128}")