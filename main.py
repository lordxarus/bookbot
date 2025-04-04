#!/bin/python3
from stats import get_char_occurence, get_num_words, sort_occurences
import sys


def get_book_text(path):
    with open(path) as f:
        return f.read()


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    count = get_num_words(text)

    occ = sort_occurences(get_char_occurence(text))
    occ_str = ""

    for entry in occ:
        occ_str += f"{entry["char"]}: {entry["num"]}\n"
    print(
        f"""
============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {count} total words
--------- Character Count -------
{occ_str}
============= END ===============
"""
    )


if __name__ == "__main__":
    main()
