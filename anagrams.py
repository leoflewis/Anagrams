#Anagrams project from the book Impractical Python Projects
#Practice for python, git and utilising the command line.
import load_dictionary
word_list = load_dictionary.load('dictionary.txt')
word_one = input("Hello friend, please enter a word:")
sorted_one = sorted(list(word_one))
anagram_list = []
for word in word_list:
    word = word.lower()
    if word != word_one:
        if sorted(list(word)) == sorted_one:
            anagram_list.append(word)
    
if len(anagram_list) == 0:
    print("None Found")
else:
    print("Anagrams of", word_one, ":")
    for w in anagram_list:
        print(w)

