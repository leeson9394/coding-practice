def toGoatLatin(S):
    vowel = {'a', 'e', 'i', 'o', 'u'}
    s_list = S.split()
    for i in range(len(s_list)):
        s = s_list[i]
        if s[0].lower() in vowel:
            s_list[i] += 'ma'
        else:
            s_list[i] = s[1:]+s[0] + 'ma'
        s_list[i] += ('a' * (i+1))
    r = ''
    for s in s_list:
        r = r + s + ' '
    return r[:-1]


if __name__ == '__main__':
    print(toGoatLatin("The quick brown fox jumped over the lazy dog"))
