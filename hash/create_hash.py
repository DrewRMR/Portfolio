import hashlib

def GetHash(input_string, algorithm='sha512'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(input_string.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_hex

# Function to prompt user for input and return it
getString = lambda inputString: "Hello, World!" if inputString == "" else inputString

# Prompt user for input
stringToHash = getString(str(input("Enter text to hash: ")))

hashDictionary = {}

# Hash each character in the input string
for letterCharacter in stringToHash:
    hashCharacter = GetHash(letterCharacter)
    if hashCharacter not in hashDictionary:
        hashDictionary[hashCharacter] = letterCharacter

# Print out the hash dictionary
print("Hash Dictionary:")
for key, val in hashDictionary.items():
    print(f"{key:<20}:{val:>2}")

# Save hashDictionary to a file for the receiver to use for verification
with open('hash_dictionary.txt', 'w') as file:
    for key, val in hashDictionary.items():
        file.write(f"{key}:{val}\n")

print("Hash dictionary saved to 'hash_dictionary.txt'.")