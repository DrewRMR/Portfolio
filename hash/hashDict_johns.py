import hashlib

def GetHash(input_string, algorithm='sha512'):
    # Create a hash object using the specified algorithm
    hash_object = hashlib.new(algorithm)
    # Encode the input string to bytes and update the hash object
    # because hashlib does not accept text only bytes
    hash_object.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    # hash_object value is the memory location, memory size etc.
    hash_hex = hash_object.hexdigest()
    return hash_hex

hashDictionary = {}

# a lambda expression is an inline function with inputString as a parameter
# returning Hello, World! as default text
getString = lambda inputString: "Hello, World!" if inputString == "" else inputString
stringToHash = getString(str(input("Enter text: ")))

for letterCharacter in stringToHash:
    # if hash is used instead of hashlib then the has value is not
    # repeated outside of the current session

    # hashCharacter = hash(letterCharacter)
    hashCharacter = GetHash(letterCharacter)
    if hashCharacter not in hashDictionary:
        hashDictionary[hashCharacter]=letterCharacter

for key, val in hashDictionary.items():
    # :<20 will ensure that a column has at minimum 20 characters in length and left alignment
    print(f"{key:<20}:{val:>2}")
    


