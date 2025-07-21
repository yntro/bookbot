def print_report(*args):
    number_of_words = args[0]
    new_character_count = args[1]
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for item in new_character_count:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")