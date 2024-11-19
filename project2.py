#open txt and read it in
with open("story.txt", "r") as f:
    story = f.read()

#create set of all the words
#set only contains unique words compared to a list which contains every word
words = set()
start_of_word = -1   
target_start = "<" 
target_end = ">"

#locates all the different words in the story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    #finds the end of the word and grabs it and adds it to the set then reset start of word
    if char == target_end and start_of_word != 1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

#has user place answers for each word
for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

#replaces all words in the story with users answers
for word in words:
    story = story.replace(word, answers[word])

print(story)