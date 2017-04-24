import string


def count(charecter):
    histogram = {}
    for charecter in text:
        if charecter in string.letters:
            key = charecter()
            charecter_count = histogram.get(key, 0)
            charecter_count += 1
            histogram[key] = character_count

    return histogram


histogram = count('to be or not to be')
for key, value in histogram.items():
    print("{}: {}".format(key, value))
