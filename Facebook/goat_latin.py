# Goat Latin is a made-up language based off of English, sort of like Pig Latin.

# The rules of Goat Latin are as follows:

# 1. If a word begins with a consonant (i.e. not a vowel), remove the first
# letter and append it to the end, then add 'ma'.
# For example, the word 'goat' becomes 'oatgma'.

# 2. If a word begins with a vowel (a, e, i, o, or u), append 'ma' to the end of the word.
# For example, the word 'I' becomes 'Ima'.

# 3. Add one letter "a" to the end of each word per its word index in the
# sentence, starting with 1. That is, the first word gets "a" added to the
# end, the second word gets "aa" added to the end, the third word in the
# sentence gets "aaa" added to the end, and so on.

# Write a function that, given a string of words making up one sentence, returns
# that sentence in Goat Latin. For example:

# string_to_goat_latin('I speak Goat Latin')

# would return: 'Imaa peaksmaaa oatGmaaaa atinLmaaaaa'

def goat_latin(original_sentence):

    vowels = ['a', 'e', 'i', 'o', 'u']
    word_count = 0
    goat_latin_sentence = ""

    words_list = original_sentence.split(" ") # split sentence into word by space

    for word in words_list: 
        # print(word)
        word_count += 1
        characters = list(word)             # split word into character list
        # print(characters[0])
        if characters[0].lower() in vowels: # if first letter is vowel, add ma to the end
            # print("found vowel")
            characters.append("m")
            characters.append("a")
        else:                               # if no vowel at first letter, move it to last and add ma to the end
            first_letter = characters[0] 
            characters.pop(0)
            characters.append(first_letter)
            characters.append("m")
            characters.append("a")

        for count in range(1, word_count+1): # add a's to the end of the word base on word index
            characters.append("a")

        # print(characters)
        # print(word_count)    
        goat_latin_word = "".join(characters) # put character list back to word string
        # print(to_string)
        goat_latin_sentence += goat_latin_word + " " # put all words back to a sentence
    return goat_latin_sentence

original_sentence = 'I speak Goat Latin'
result = goat_latin(original_sentence)
print(result)

# one for loop only
def goat_latin(original_sentence):

    vowels = ['a', 'e', 'i', 'o', 'u']
    goat_latin_sentence = ""
    word_cnt = 0
    words = original_sentence.split(" ")

    for word in words:
        word_cnt += 1
        if word[0].lower() in vowels: # if first character is vowel
            goat_latin_sentence = goat_latin_sentence + word + "ma" + "a" * word_cnt + " "
        else:
            first_c  = word[0] # store first character
            word = word[1:] # pop out first character
            goat_latin_sentence = goat_latin_sentence + word + first_c + "ma" + "a" * word_cnt + " "

    return goat_latin_sentence

original_sentence = 'I speak Goat Latin'
result = goat_latin(original_sentence)
print(result)