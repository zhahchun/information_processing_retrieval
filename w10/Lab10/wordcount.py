import sys, string
stop_words = ['i', 'of', 'to', 'a', 'an', 'the', 'and', 'you', 'my', 'sir', 'in', 'that', 'is', 'not', 'with', 'for', 'this', 
              'be', 'your', 'but', 'it', 'will', 'as', 'me', 'he', 'or', 'have', 'if', 'thou', 'what', 'do', 'by', 'no', 
              'his', 'thy', 'are', 'him', 'so', 'am', 'shall', 'at', 'let', 'all', 'their', 'they', 'we', 'our', 'on', 
              'from', 'then', 'how', 'her', 'most', 'was', 'may', 'more']
# with open("short.txt", "r", encoding = 'utf-8') as f: # Exercise 5: Change the file you read from
# with open("medium.txt", "r", encoding = 'utf-8') as f:
word_dict = {}
input_filename = sys.argv[1] # Exercise 10: Change the file you read from, pt 2
output_filename = sys.argv[2] # Challenge 1: Change the file you write to

with open(input_filename, "r", encoding = 'utf-8') as f: # Exercise 1: Print out a file’s contents
    count = 0
    word_count = 0    
    # print("Print out a file’s contents:")
    for line in f:
        # line = f.readline() 
        line = line.translate(str.maketrans('', '', string.punctuation))
        word_count += len(line.split())
        count += 1        
        # print(count, line, end= '') # Exercise 2: Print line numbers
        for word in line.split(): # Exercise 6: Count how many of each word
            if word.lower() in stop_words: # Exercise 9: Stop List
                continue
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 1
            else:
                 word_dict[word.lower()] += 1
        
    print('\nThere are a total of', count, 'lines in this file.') # Exercise 3: Print out the total number of lines in the file
    print('There are a total of', word_count, 'words in this file.\n') # Exercise 4: Count the total number of words in the file
    # print(word_dict)
    count = 0

with open(output_filename, 'w') as f: 
# with open(output_filename, 'a') as f: # Challenge 3: Append to the output
    print('Top 10 most common words:')
    for k in sorted(word_dict, key=word_dict.get, reverse=True): # Exercise 7: Sort the words by frequency
        if count == 10: # Exercise 8: Top 10 most common words
            break
        print(k, ':', word_dict[k])
        print(k, ':', word_dict[k], file=f) # Exercise 11: Write the results to a file
        count += 1
