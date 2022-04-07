def oneEdit(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    distance = 0
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            distance += 1
            if distance > 1:
                return False
            if len(s1) == len(s2):
                i += 1
                j += 1
                continue
            if len(s1) < len(s2):
                j += 1
                continue
            if len(s1) > len(s2):
                i += 1
        else:
            i += 1
            j += 1
    return True


if __name__ == '__main__':
    print(oneEdit("peaks", "geeks"))
