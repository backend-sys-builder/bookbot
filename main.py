def get_book_text (filepath):
    with open(filepath) as file:
        file_string = file.read()
    return file_string
def main():
    text = get_book_text("books/frankenstein.txt")
     
     
main()
def word_counter():
    text = get_book_text("books/frankenstein.txt") 
    text_string = text.split()
    word_count = len(text_string)
    print (f"{word_count} words found in the document")
    

word_counter()