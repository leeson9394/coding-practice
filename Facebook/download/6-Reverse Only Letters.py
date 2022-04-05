import re


# def reverseOnlyLetters(S):
#     s = re.sub('[^a-zA-Z]', '', S)[::-1]
#     r = ""
#     j = 0
#     for i in range(len(S)):
#         if re.match('[^a-zA-Z]', S[i]): 
#             r += S[i]
#         else: 
#             r += s[j]
#             j += 1
#     return r


# Solution without regex
def reverseOnlyLetters(S):
    letter_only_str = ""
    ans_list = []
    for char in S: # remove non alphabets
        if char.isalpha():
            letter_only_str += char
    letter_only_str = letter_only_str[::-1] # reverse string
    print(letter_only_str)

    j = 0
    for i in range(len(S)):
        if S[i].isalpha():
            ans_list.append(letter_only_str[j])
            j += 1
        else:
            ans_list.append(S[i])

    ans_str = "".join(ans_list)

    return ans_str


if __name__ == '__main__':
    print(reverseOnlyLetters("a-bC-dEf-ghIj"))
