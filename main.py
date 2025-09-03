def get_book_text (filepath):
    with open(filepath) as file:
        file_string = file.read()
    return file_string
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
     
     
main()

    
