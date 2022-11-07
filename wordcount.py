"""Count words in file."""

#open the input text file
text = open("test.txt")

#initialize an empty dict that will show the count (of each space-sep words)
word_dict = {}

#create a for loop to create a line split differentiating space-sep words)
for line in text:
    line = line.rstrip()
    words = line.split()

        #create a for loop that retrieves each word and numbers it
    for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

    #counts each word and print
for word, count in word_dict.items():
        print(word, count)
