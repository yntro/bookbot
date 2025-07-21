from stats import *
from functions import *

def main():
    path = "./books/frankenstein.txt"
    text = get_book_text(path)
    number_of_words = get_word_count(text)
    character_count = get_character_count(text)

    new_character_count = sort_dictionary(character_count)

    print_report(number_of_words, new_character_count)


main()
