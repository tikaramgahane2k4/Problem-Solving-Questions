"""Counting Vowels in String"""

# name = "TIkarAm GahAne OOo"

# vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# count = 0

# for char in name:
#     if char in vowels:
#         count += 1

# print(count)

def countVowels(name):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    count = 0

    for char in name:
        if char in vowels:
            count += 1

    return count

print(countVowels("toaoeeijdjfaoajorwotjaljaclaisdtawoiiappaadsfm"))