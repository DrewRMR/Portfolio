import random
import getpass
from database import get_word_list

def Import_database():
    os.system("cls")

    username = input("db_aa9650_hangman_admin")
    password = getpass.getpass("TeamBRules123")
    
    new_word_list = get_word_list(username, password)
    
    global words
    words = new_word_list
    
    return new_word_list