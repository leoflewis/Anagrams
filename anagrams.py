#Anagrams project from the book Impractical Python Projects
#Practice for python, git and utilising the command line.
import load_dictionary
import sys
from collections import Counter

word_list = load_dictionary.load('dictionary.txt')
word_list.append('a')
word_list.append('i')
ini_name = input("Hello friend, please enter a name:")
word_list = sorted(word_list)

def find_anagrams(name, word_list):
    name_letter_map = Counter(name)
    anagram_list = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for letter in word:
            if word_letter_map[letter] <= name_letter_map[letter]:
                test += letter
        if Counter(test) == word_letter_map:
            anagram_list.append(word) 
    print(*anagram_list, sep='\n')
    print()
    print('Remaining letters = {}',format(name))
    print('Number of remaining letters = {}'.format(len(name)))
    print('Number of remaining real word anagrams = {}'.format(len(anagram_list)))

def process_choice(name):
    while True:
        choice = input('\nMake a choice or else Enter to start over or # to end:')
        if choice == '':
            main()
        elif choice == '#':
            sys.exit()
        else:
            candidate = ''.join(choice.lower().split())
        left_over_list = list(name)
        for letter in candidate:
            if letter in left_over_list:
                left_over_list.remove(letter)
        if len(name) - len(left_over_list) == len(candidate):
            break
        else:
            print('wont work! Make another selection!', file = sys.stderr)
    name = ''.join(left_over_list)
    return choice, name

def main():
    name = ''.join(ini_name.lower().split())
    name = name.replace('-','')
    limit = len(name)
    phrase = ''
    running = True
    while running:
        temp_phrase = phrase.replace(' ','')
        if len(temp_phrase) < limit:
            print('Lenth of anagram = {}'.format(len(temp_phrase)))
            find_anagrams(name, word_list)
            print('Current anagram phrase = ',phrase, end=' ')
            print(phrase, file=sys.stderr)
            choice, name = process_choice(name)
            phrase += choice + ' '
        elif len(temp_phrase) == limit:
            print('\nFINISHED')
            print('Anagram = ',phrase, end = ' ')
            print(phrase, file=sys.stderr)
            print()
            tryagain = input('Try Again? (n or y)')
            if tryagain == 'n':
                running = False
                sys.exit()
            else:
                main()

if __name__ == '__main__':
    main()
