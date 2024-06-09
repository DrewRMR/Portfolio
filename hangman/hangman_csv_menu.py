def pageCSV():
    os.system("cls")
    print ("==================\n\n")
    print ("    CSV Options\n\n")
    print (" 1) See List")
    print (" 2) Write new list")
    print (" 3) Change word")
    print (" 4) Delete Word")
    print (" 5) Back\n\n")
    Choice= input('Input An Option: ')
    if Choice == "1":
        fileName=input('Which file would you like to see?')
        viewCSV(fileName)
    elif Choice == "2":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.create_word_list(fileName)
        viewCSV(fileName)
    elif Choice == "3":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.update_word(fileName)
        viewCSV(fileName)
    elif Choice == "4":
        fileName=input('Which file would you like to use?')
        print(csvcontrol.read_words_from_file(fileName))
        csvcontrol.delete_word(fileNadef viewCSV(fileName):
    listCSV=csvcontrol.read_words_from_file(fileName)
    print(listCSV)
    addList=input('Import this list?  y/n')
    if addList == 'y':
        global words
        words=listCSV
        animation.loading(0.5)
        main()
    elif addList == 'n':
        pageCSV()
    else:
        input("Please Input Valid Option")
    viewCSV()
