# Welcome to Meta!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!



# Please join Zoom for the mock coding interview:
#  https://fb.zoom.us/j/99989466116?pwd=QkZpSHlPYUlvdkMzZ2hKYzdENEtCUT09
    
    
# zoom is updating. few mins

# no worries

# Facebook logo stickers cost $2 each from the company store. I have an idea.
# I want to cut up the stickers, and use the letters to make other words/phrases.
# A Facebook logo sticker contains only the word 'facebook', in all lower-case letters.
#
# Write a function that, given a string consisting of a word or words made up
# of letters from the word 'facebook', returns an integer with the number of
# stickers I will need to buy.
#
# get_num_stickers('coffee kebab') -> 3
# get_num_stickers('boook') -> 2
# get_num_stickers('ffacebook') -> 2
#
# You can assume the input you are passed is valid, that is, does not contain
# any non-'facebook' letters, and the only potential non-letter characters
# in the string are spaces.

def get_num_stickers(string):
    kv = {}
    max_value = 0 
    for c in string:
        if c in kv:
            kv[c] += 1
        else:
            kv[c] = 1
            
        # sticker_value = max(kv[c])
    if "o" in kv.keys():
        kv["o"] = int(kv["o"] / 2) + (kv["o"] % 2 > 0)
        
    for item in kv:
        if max_value < kv[item]:
            max_value = kv[item]
        
    return max_value
  

res = get_num_stickers('coffee kebab')
# res = get_num_stickers('boook')
print(res)



# Write a function that takes a list of words as input, and returns 
# a list of those words bucketized by anagrams.
#
# "Anagram" definition: a word, phrase, or name formed by rearranging
# the letters of another, such as cinema, formed from iceman.
#
# Example:
# 
# anagram_buckets(word_list)
#
# Input:  ["star", "rats", "car", "arc", "arts", "stars"]
# Output:  [ ["star", "rats", "arts"], ["car", "arc"], ["stars"] ]


# def anagram_buckets(word_list):
#     word_list = sorted(word_list)
#     print(word_list)
            
# word_list = ["star", "rats", "car", "arc", "arts", "stars"]
# anagram_buckets(word_list)