import sys

# File for all the random functions

def print_report(*args):
    number_of_words = args[0]
    list_of_characters = args[1]
    name_of_the_book = args[2]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {name_of_the_book}...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in list_of_characters:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

def get_sys_args():
    if len(sys.argv) > 1:
        return sys.argv[1:]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def sort_dict_by_value_desc(dictionary):
    sorted_items = sorted(dictionary.items(), key=lambda item: item[1], reverse=True)
    return sorted_items
