
def len_of_longest_substring(s):
    length = 0
    prev, right = 0, 0
    container = []

    while right < len(s):
        while s[right] in container:
            container.remove(s[prev])
            prev = prev + 1

        container.append(s[right])
        length = max(length, len(container))

        right = right + 1

    return length

print(len_of_longest_substring('bbbb'))
print(len_of_longest_substring('abcabcbb'))
print(len_of_longest_substring('pwwkewfgh'))

