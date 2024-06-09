import hashlib

def get_hash(input_string, algorithm='sha512'):
    # Create a hash oject using the specified algorithm
    hash_object = hashlib.new(algorithm)
    # Encode the input string to bytes and update the hash object
    hash_object.update(input_string.encode('utf-8'))
    # Get the hexadecimal representation of the hash
    hash_hex = hash_object.hexdigest()
    return hash_hex


# Example Usage
# Common algorithms md5, sha1, sha224, sha256, sha384, and sha512

algoList = ('md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512')

input_string = "Sample Text to be Coded"
for algo in algoList:
    hash_value = get_hash(input_string, algo)
    print(f"The '{algo:<10}' hash of '{input_string}' is: {hash_value}")
