def get_num_words(text):
    return len(text.split())


def get_char_occurence(text):
    count = {}
    skip = True
    for word in text.lower().split():
        for c in word:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
    return count


def sorted_on(dict):
    return dict["num"]


# If you wanted to sort by value and just use one dictionary
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# {k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
def sort_occurences(dict):
    sorted = []
    for key, val in dict.items():
        sorted.append({"char": key, "num": val})
    sorted.sort(reverse=True, key=lambda dict: dict["num"])
    return sorted
