def get_book_text (filepath):
    with open(filepath) as file:
        file_string = file.read()
    return file_string
def main():
    text = get_book_text("books/frankenstein.txt")

def word_counter(text):
    return len(text.split())

def character_counter(text):
    character_count = {}
    all_lowercase = text.lower()
    for character in all_lowercase:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    return (character_count)
