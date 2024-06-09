import requests
from bs4 import BeautifulSoup

url = "https://drewrmr.github.io/Portfolio/HangmanList.html"

def get_words_from_web():
    response = requests.get(url)
    response = response.content
    soup = BeautifulSoup(response, 'html.parser')

    ol =soup.find('ol')
    words = ol.find_all('li')
    wordList = []

    for tag in words:
        #tagContent = tag.find('value')
        word = tag.text.strip()
        wordList.append(word)
    return wordList

    word_list = get_words_from_web(url)
    print(word_list)
    input()
