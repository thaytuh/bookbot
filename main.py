from stats import (word_counter, character_counter, sort_char_counts)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_filepath = sys.argv[1]
    result = get_book_text(book_filepath)
    word_count = word_counter(result)
    char_count = character_counter(result)
    sorted_chars = sort_char_counts(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_filepath}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print(sorted_chars)
 
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()