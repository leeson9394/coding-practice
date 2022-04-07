# "ABCA" -> "A"
# "BCABA" -> "B"
# "ABC" -> "None"


def first_recurring_character(str):
    char_to_count = {}
    for char in str:
        if char in char_to_count:
            return char
        else:
            char_to_count[char] = 1
    return None

print(first_recurring_character("ABCA"))
print(first_recurring_character("BCABA"))
print(first_recurring_character("ABC"))