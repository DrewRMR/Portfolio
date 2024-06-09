import hashlib
import json

# Function to read hashed passwords from JSON file
def read_passwords_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to verify login
def verify_login(username, password, hash_dict):
    if username in hash_dict:
        # Calculate SHA-512 hash for the provided password
        password_hash = hashlib.sha512(password.encode()).hexdigest()
        
        # Compare the stored hash with the hash of the provided password
        if hash_dict[username] == password_hash:
            print("Login successful!")
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")

# Prompt user for username and password
username = input("Enter username: ") #user1
password = input("Enter password: ") #test

# Read hashed passwords from JSON file
hash_dict = read_passwords_from_file("passwords.json")

# Verify login
verify_login(username, password, hash_dict)
