import bcrypt

strings = [
    "test",
    "Hello, world!",
    "This is my test dictionary",
    "This is going to look very strange shortly!",
]

# Hash the strings using bcrypt
hash_dict = {}
for string in strings:
    # Hash the string
    hashed_value = bcrypt.hashpw(string.encode(), bcrypt.gensalt())
    hash_dict[string] = hashed_value

# Print the hashed values
for key, val in hash_dict.items():
    print(f"{key:<30}{val}")

# Verify a string
test_string = "test"
if bcrypt.checkpw(test_string.encode(), hash_dict[test_string]):
    print("Password matches")
else:
    print("Password does not match")