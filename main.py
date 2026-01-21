import sys
from stats import word_count, letter_count
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents



def main():
    #reading_book = get_book_text(path_to_book)
    #words_thing = word_count(reading_book)
    #words_thing_2 = letter_count(reading_book)
    # 1. guard: wrong number of args
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # 2. now it's safe to use sys.argv[1]
    path_to_book = sys.argv[1]
    # use path_to_book instead of a hardcoded string

    reading_book = get_book_text(path_to_book)
    words_thing = word_count(reading_book)
    words_thing_2 = letter_count(reading_book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {path_to_book}...\n ----------- Word Count ----------\nFound {words_thing} total words\n --------- Character Count -------")
    for char, num in words_thing_2:
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

main()
