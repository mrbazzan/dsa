
"""
Given a string and n characters, find the shortest substring that contains
all desired characters.

Input - fa4chba4c --> fa4chb, a4chb, 4chba, chba, hba4c, ba4c
char - abc

"""

def shortest_substring(s, chars):
    left, right = 0, 0
    substring = []
    while left<len(s):

        container = set(chars)

        while container and right<len(s):
            container.discard(s[right])
            right = right + 1

        if not container:
            substring.append(s[left:right])

        left = left + 1
        right = left

    return substring

print(shortest_substring("fa4chba4c", "abc"))

