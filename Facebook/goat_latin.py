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

def goat_latin(words):
    words_list = words.split(" ")
    vowels = ['a', 'e', 'i', 'o', 'u']
    word_count = 0
    res = ""
    for word in words_list:
        # print(word)
        word_count += 1
        characters = list(word)
        # print(characters[0])
        if characters[0].lower() in vowels: # if first letter is vowel, add ma to the end
            # print("found vowel")
            characters.append("m")
            characters.append("a")
        else:                               # if no vowel at first letter, move it to the end
            first_letter = characters[0] 
            characters.pop(0)
            characters.append(first_letter)
            characters.append("m")
            characters.append("a")

        for count in range(1, word_count+1): # add a's to the end of the word base on word index
            characters.append("a")

        # print(characters)
        # print(word_count)    
        to_string = "".join(characters) # put character list back to word string
        # print(to_string)
        res += to_string + " " # put all words back to a sentence
    return res

words = 'I speak Goat Latin'
result = goat_latin(words)
print(result)