import sys

def print_report(*args):
    number_of_words = args[0]
    list_of_characters = args[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in list_of_characters:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

def get_sys_args():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        return path
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)