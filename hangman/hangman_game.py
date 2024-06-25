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
        password_hash = hashlib.sha512(password.encode()).hexdigest()  #user1 password is "test"
        
        # Compare the stored hash with the hash of the provided password
        if hash_dict[username] == password_hash:
            print("Login successful!")
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("Username not found.")
        return False

# Read hashed passwords from JSON file
hash_dict = read_passwords_from_file("passwords.json")

# Verify login
while True:
    username = input("Enter username: ")
    password = input("Enter password: ")
    if verify_login(username, password, hash_dict):
        break  # Exit loop if login is successful

import random
import time
import os
import requests
from database import get_word_list
from webscrape import get_words_from_web
from jotform_api import get_words_from_jotform

# Initialize words as an empty list
words = ["temporary", "align", "elephant"]

def Import_database():
    os.system("cls")
    
    # Securely input username and password
    username = "db_aa9650_hangman_admin"
    password = "TeamBRules123"

    # Fetch the word list using the provided credentials
    new_word_list = get_word_list(username, password)
    
    # Use the global keyword to modify the global words variable
    global words
    words = new_word_list
    
    return new_word_list


def csv_menu():
    os.system("cls")
    print("==================")
    print("CSV MENU")
    print("==================\n\n")
    print(" 1) Create Word List")
    print(" 2) Read Words From File")
    print(" 3) Update Word")
    print(" 4) Delete Word")
    print(" 5) Back to Main Menu")
    print("==================\n\n")

    choice = input('Input An Option: ')
    if choice == "1":
        create_word_list("words.csv")
    elif choice == "2":
        read_words_from_file("words.csv")
    elif choice == "3":
        update_word("words.csv")
    elif choice == "4":
        delete_word("words.csv")
    elif choice == "5":
        main()
    else:
        input("Please Input Valid Option")
        csv_menu()


def main():
    os.system("cls")
    print("==================")
    print("WELCOME TO HANGMAN")
    print("==================\n\n")
    print("    Main Menu\n\n")
    print(" 1) Play Game")
    print(" 2) Add New Word")
    print(" 3) Play With Words Online")
    print(" 4) Get From SQL")
    print(" 5) CSV Options")
    print(" 6) Import From Jotform")
    print(" 7) Exit\n\n")
    print("==================\n\n")

    choice = input('Input An Option: ')
    if choice == "1":
        splash()
        game()
    elif choice == "2":
        Add_word()
    elif choice == "3":
        splash()
        global words
        words = get_words_from_web()
        game()
    elif choice == "4":
        splash()
        Import_database()
        game()
    elif choice == "5":
        csv_menu()
    elif choice == "9":
        api_key = input('Enter your Jotform API key: ')
        form_id = input('Enter your Jotform form ID: ')
        new_words = get_words_from_jotform(api_key, form_id)
        if new_words:
            words.extend(new_words)
            print("New words imported successfully.")
        else:
            print("No new words were imported.")
        input("Press ENTER to continue...")
        main()
    elif choice == "10":
        os._exit(0)
    else:
        input("Please Input Valid Option")
    #main()
    

def Add_word():
    os.system("cls")
    print("Old word list: ", ", ".join(words))
    New_word = input('Input New word: ')
    if len(New_word) > 0:
        words.append(New_word)
    os.system("cls")
    print("New word list", ", ".join(words))
    input("Press ENTER to continue...")

def splash():
    os.system("cls")
    # introduction to the game
    delay = 3
    while delay:
        print ('  ===================')
        print ('  LET\'S PLAY HANGMAN')
        print ('  ', delay, "secs to start")
        print ('  ===================\n\n')
        print('''
        _______
        |/    |
        |     O
        |   \_|_/
        |     |
        |    / \\
        |   /   \\
    ____|____
    \n''')
        print ('  ===================')
        time.sleep(1)
        delay = delay - 1
        os.system("cls")

def game():
    #Randomly choose a word from the list
    global secret
    secret = random.choice(words)
    secret = secret.upper()
    guessed = ''
    turns = 7
    placed = '_'*len(secret)
    l = list(placed)
    done = 0

    while turns:

        while True:
            os.system("cls")
            hang(turns)
            print("\n\nSecret Word.....:",' '.join(l))
            print("\n\nLetters Used....:",guessed)
            print("\n\nTries to go.....: ",turns)
            typed = input("\n\nGuess a Letter..: ")
            if typed not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or len(typed) > 1:
                input("Single Upper Case Letters ONLY!. Press ENTER to continue...")
            else:
                break

        turns = 7
        if typed not in guessed:
            guessed = guessed + typed
        g = list(guessed)
        s = list(secret)

        for k in range(len(g)):
            kstr = guessed[k]
            if kstr in s:
                for i in range(len(s)):
                    if kstr == s[i]:
                        l[i] = kstr
            else:
                turns = turns - 1

        if l == s:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("CONGRATULATIONS! YOU GUESSED: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break

        if turns == 0:
            os.system("cls")
            hang(turns)
            print("=============================================")
            print("GAME OVER! SECRET WORD: ", secret)
            print("=============================================")
            input("Press ENTER to continue...")
            break



def create_word_list(file_name):    
    userInput = input("Enter words separated by comma:  ").replace(" ","")
    userList = userInput.split(",")
    file = open(file_name,"w")
    for word in userList:
        file.write(word+'\n')
    file.close()
    
def read_words_from_file(file_name):
    file = open(file_name,"r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()
    return words

def update_word(file_name):    
    userInput = input("Enter word to find and word to replace separated by comma:  ").replace(" ","")
    userList = userInput.split(",")

    #read file contents list
    file = open(file_name,"r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()
    
    i=0
    while i <= len(words)-1:
        if words[i] == userList[0]:
            words[i] = userList[1]
        i +=1
    
    #write to file
    file = open(file_name,"w")
    for word in words:
        file.write(word + '\n')
    file.close()
    
def delete_word(file_name):    
    userInput = input("Enter word to delete:  ").replace("","")
    words = read_words_from_file(file_name)
    
    #read file contents to list
    file = open(file_name,"r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()

    #write to file
    file = open(file_name,"w")
    for word in words:
        if word !=userInput:
            file.write(word+'\n')
    file.close()




def hang(turn):
    if turn < 7:
        print('   _______   ')
        print('   |/    |   ')
    else:
        print('   _______   ')
        print('   |/        ')

    if turn < 6:
        print('   |     O   ')
    else:
        print('   |         ')

    if turn < 5:
        print('   |   \_|_/ ')
    else:
        print('   |         ')

    if turn < 4:
        print('   |     |   ')
    else:
        print('   |         ')

    if turn < 3:
        print('   |    / \\ ')
    else:
        print('   |         ')

    if turn < 2:
        print('   |   /   \\')
    else:
        print('   |         ')

    print(' __|____')

if __name__ == '__main__':
    main()

