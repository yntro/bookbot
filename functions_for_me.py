import sys

# File for all the random

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
        #path = sys.argv[1]
        # return path
        return sys.argv[1:]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)