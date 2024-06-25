import hashlib

def GetHash(input_string, algorithm='sha512'):
    hash_object = hashlib.new(algorithm)
    hash_object.update(input_string.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_hex

# Function to prompt user for input and return it
getString = lambda inputString: "Hello, World!" if inputString == "" else inputString

# Read hash dictionary from file
hashDictionary = {}
with open('hash_dictionary.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            key, val = line.split(':')
            hashDictionary[key] = val

# Verification process
print("\nVerification:")
verificationString = getString(str(input("Enter the same text to verify: ")))

verified = True
for letterCharacter in verificationString:
    hashCharacter = GetHash(letterCharacter)
    if hashCharacter in hashDictionary and hashDictionary[hashCharacter] == letterCharacter:
        print(f"Hash for '{letterCharacter}' is verified.")
    else:
        print(f"Hash for '{letterCharacter}' is not verified.")
        verified = False

if verified:
    print("\nAll hashes verified successfully.")
else:
    print("\nVerification failed.")
