import hashlib

strings = [
    "Hello, world!",
    "This is my test dictionary",
    "Does this look good?",
    "I still dont quite get it..",
]

hash_dict = {}

for string in strings:
    hash_value = hashlib.sha512(string.encode()).hexdigest()
    hash_dict[string] = hash_value
    
for key, val in hash_dict.items():
    
    print(f"{key:<50}:{val:>2}")

