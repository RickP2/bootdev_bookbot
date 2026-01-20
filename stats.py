def word_count(book_selected):
        words_in_work = book_selected.split()
        num_words = len(words_in_work)
        return num_words

def letter_count(book_selected):
    counts = {}

    for letter_from_book in book_selected:
        letter = letter_from_book.lower()
        counts[letter] = counts.get(letter,0) + 1
    def sort_counts(dict_key):
        return dict_key[1]
    
    sorted_counts = sorted(counts.items(),reverse=True, key=sort_counts)
    print(f"{counts}\n")


