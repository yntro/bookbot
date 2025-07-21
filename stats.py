def get_book_text(path):
    with open(path) as f:
        text = f.read()
        return text       

def get_word_count(text):
    number_of_words = 0
    text_list = text.split()
    number_of_words = len(text_list)
    return number_of_words

def get_character_count(text):
    character_count = {}
    text = text.lower()
    for character in text:
        if character not in character_count:
            character_count[character] = 1
        else:
            character_count[character] += 1
    return character_count

def sort_dictionary(dictionary):
    sorted_dictionary = sorted(dictionary.items(), key= lambda item: item[1], reverse=True)
    return sorted_dictionary
# where value == character -> add to list & value++ 