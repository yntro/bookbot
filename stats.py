def get_book_text(path):
    with open(path) as f:
        text = f.read()
        word_count = get_word_count(text)
        print(f"{word_count} words found in the document")

def get_word_count(text):
    number_of_words = 0
    text_list = text.split()
    number_of_words = len(text_list)
    return number_of_words