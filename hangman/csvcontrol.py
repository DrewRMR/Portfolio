 #CRUD Operations


#READ file content
def read_words_from_file(file_name):
    file = open(file_name,"r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()
    return words

#CREATE a new list of words and save the file
def create_word_list(file_name):    
    userInput = input("Enter words separated by comma:  ").replace(" ","")
    userList = userInput.split(",")
    file = open(file_name,"w")
    for word in userList:
        file.write(word+'\n')
    file.close()

#UPDATE a word with a new word
# read a word to find and word to replace
def update_word(file_name):    
    userInput = input("Enter word to find and word to replace separated by comma:  ").replace(" ","")
    userList = userInput.split(",")

    #read file contents list
    file = open(file_name,"r")
    words = []
    for word in file:
        words.append(word.strip("\n"))
    file.close()

 #search through list and replace

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

#DELETE a word
# read word to find and word to replace
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

print(read_words_from_file("words.csv"))
create_word_list("words.csv")
update_word("words.csv")
delete_word("words.csv")

