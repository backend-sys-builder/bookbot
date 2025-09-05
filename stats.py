def get_book_text (filepath):
    with open(filepath) as file:
        file_string = file.read()
    return file_string
def main():
    text = get_book_text("books/frankenstein.txt")

def word_counter():
    text = get_book_text("books/frankenstein.txt") 
    text_string = text.split()
    word_count = len(text_string)
    print (f"{word_count} words found in the document")

def character_counter():
    character_count = {}
    text = get_book_text("books/frankenstein.txt") 
    all_lowercase = text.lower()
    for character in all_lowercase:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    print (character_count)