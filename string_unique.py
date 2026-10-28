import random
import timeit
from collections import defaultdict


def is_unique(string: str) -> bool:
    duplicates: int = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if string[i] == string[j]:
                return False
    return True

    # for character in string:
    #     for character2 in string:
    #         if character == character2:
    #             duplicates += 1
    #
    #         if duplicates == 2:
    #             return False
    #
    # return True


def test(d):
    for x in range(1, len(d) // 2):
        a = d[x + 1]
        c = d[len(d) - x]
        d[x] = c
        d[len(d) - x] = a


def remove_dupesv1(*string: str, replace: str = None) -> str:
    string = ''.join(string)
    char = 1
    while char < len(string):
        for pos in range(char):
            # print(string[pos], char)
            if string[pos] == string[char]:
                string = string[:char] + (replace if (replace is not None) else '') + string[char + 1:]

                if replace is None:
                    char -= 1

                break

        char += 1
    return string


def remove_dupesv2(string: str, replace: str = None) -> str:
    # remove inner loop to use a set
    seen_characters: set[str] = {string[0]}

    char = 1
    while char < len(string):
        if string[char] in seen_characters:
            string = string[:char] + (replace if (replace is not None) else '') + string[char + 1:]

            if replace is None:
                char -= 1

            break

        else:
            seen_characters.add(string[char])

        char += 1

    return string


def anagrams_(string1, string2) -> bool:
    if len(string1) != len(string2):
        return False

    elif string1 == string2:
        return True

    else:
        # same length but different strings
        for c in range(len(string2)):
            found = False

            for r in range(len(string1)):
                if string1[c] == string2[r]:
                    string2 = string2[:r] + string2[r + 1:]
                    found = True

                    break

            if not found:
                return False

        return True

def anagrams_2(string1, string2) -> bool:
    if len(string1) != len(string2):
        return False

    elif string1 == string2:
        return True

    else:
        # same length but different strings
        characters: defaultdict[str, int] = defaultdict(int)
        for character in string1:
            characters[character] += 1

        for c in string2:
            if characters[c] <= 0:
                del characters[c]

            if not c in characters:
                return False

            characters[c] -= 1

        return True

print(is_unique('Hel lo World!'))
print(is_unique('Hel1o W0r|d!'))

b = ""
for _ in range(100000):
    b += chr(random.randint(33, 128))
l = list(b)
random.shuffle(l)
b2 = ''.join(l)
print('~~~~~~~~~~~~~~~')
# print(timeit.timeit(lambda: remove_dupesv2(b), number=3))
# print(timeit.timeit(lambda: remove_dupesv1(b), number=3))
print(timeit.timeit(lambda: anagrams_2(b, b2), number=3))
print(timeit.timeit(lambda: anagrams_(b, b2), number=3))