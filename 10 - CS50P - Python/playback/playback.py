#input sentence
sentence = input("")

#adding split to separate the word
text = sentence.split()

#adding asteriks to add the dots between the words
#printing the result
print(*text, sep="...")
