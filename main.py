from stats import *
from functions_for_me import *

def main():
    
    paths = get_sys_args()
    for path in paths:
        text = get_book_text(path)
        number_of_words = get_word_count(text)
        character_count = get_character_count(text)
        sorted_character_count = sort_dictionary(character_count)
        print_report(number_of_words, sorted_character_count, path)


main()
