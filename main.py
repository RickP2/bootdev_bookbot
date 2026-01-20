from stats import word_count, letter_count
def get_book_text(path_to_file):
    
    with open(path_to_file) as f:
        # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents



def main():
    reading_book = get_book_text("books/frankenstein.txt")
    words_thing = word_count(reading_book)
    words_thing_2 = letter_count(reading_book)
    print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n ----------- Word Count ----------\nFound {words_thing} total words\n --------- Character Count -------\n {words_thing_2}\n ============= END ===============")

main()
