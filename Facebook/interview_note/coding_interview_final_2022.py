"""
Determine if a string is a palindrome
- case insensitive
- ignore non-letters
- input can be > 1/2 RAM

"Race car!"

"""

def valid_palidrome(string):
    # valid_list = []
#     striped_string = ""
# #  ["c","a","b"]
#     for char in string:
#         if char.isalpha():
#             # valid_list.append(char)
#             striped_string += char

    if not string:
        return False

    left = 0
    right = len(string) - 1

    # while left < right:
    #     # if valid_list[left] != valid_list[right]:
    #     if striped_string[left] != striped_string[right]:
    #         return False
    #     left += 1
    #     right -= 1
    
    while left < right:
        if string[left] != string[right]:
            return False
        if not string[left].isalpha():
            left += 1
        if not string[right].isalpha():
            right -= 1
        else:
            left += 1
            right -= 1
            
    return True


"""
Fortune

===START FILE===(This part is not inside the file)
Notice From Management:
All Leave will be suspended until morale improves!
%
Dumb terminal
%
Parkinson's Law:  Work expands to fill the time allotted it.
%
%
The Law, in its majestic equality, forbids the rich, as well as the poor,
to sleep under the bridges, to beg in the streets, and to steal bread.
            -- Anatole France
%
CPUs running at 150%
%
% really is an ugly character!
%
50% of the time it works every time!
%
.______.
|      |
| ASCII|
| BOX  |
.______.
%
===END FILE===(This part is not inside the file)

res = [
    
]

msgs = [
"Notice From Management:\nAll Leave will be suspended until morale improves!"
    ]

"""

import random

def fortune(file):
    msgs = []
    break_point = 0
    with open(file, "r") as f:
        article = f.readlines()
        print(article)
        for i in range(len(article)):
            if article[i] == "%\n":
                msgs.append(article[break_point:i]) # capture the paragraph between break point to termination mark "%\n" 
                break_point = i + 1 # update the break point with skipping the termination mark "%\n" 

    lucky = random.randint(0, len(msgs) - 1)
    print(msgs[lucky])

file = "Facebook/data/fortune.txt"
fortune(file)