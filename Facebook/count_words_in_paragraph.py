import re

def count_words_in_paragraph(file_path, num):
    word_to_ocurrance = {}
    with open(file_path, "r") as f:
        article = f.readlines()
        for line in article:
            words = line.split(" ")
            
            for word in words:
                filtered_word = re.sub('[^A-Za-z0-9]+', '', word).lower()
                if filtered_word in word_to_ocurrance.keys():
                    word_to_ocurrance[filtered_word] += 1
                else:
                    word_to_ocurrance[filtered_word] = 1

            sorted_words_tup = sorted(word_to_ocurrance.items(), key = lambda x : (-x[1], x[0]) )
            print(sorted_words_tup)
            print(word_to_ocurrance)
            # for i in range(num):
            #     print(sorted_words_tup[i][0], sorted_words_tup[i][1])


file_path = "Facebook/data/count_words.txt"
num = 10

count_words_in_paragraph(file_path, num)

