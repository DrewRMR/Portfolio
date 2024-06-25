import hashlib

def personal_hash(input_string, salt):
    # Combine the input string with the salt
    salted_input = input_string + salt
    # Create the hash
    hash_value = hashlib.sha512(salted_input.encode()).hexdigest()
    return hash_value

# Your personal salt - this could be anything unique to you
my_salt = "JohnDoe1990"  # Replace with your own identifier

strings = ["test"]
#    "Hello, world!",
#    "This is my test dictionary",
#    "This is going to look very strange shortly!",
#]

hash_dict = {}
for string in strings:
    hash_value = personal_hash(string, my_salt)
    hash_dict[string] = hash_value
    
for key, val in hash_dict.items():
    print(f"{key:<10}{val:>128}")
