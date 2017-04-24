import string


def count(text):
    histogram = {}
    for character in text:
        if character in string.letters:
            key = character.lower()
            character_count = histogram.get(key, 0)
            character_count += 1
            histogram[key] = character_count

    return histogram


histogram = count('banana')
for key, value in histogram.items():
    print("{}: {}".format(key, value))
