import sys

from stats import get_book_text, word_counter, character_counter, sort_char_counts  # language: python

def main():  # language: python
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    text = get_book_text(sys.argv[1])

    total = word_counter(text)
    print("----------- Word Count ----------")
    print(f"Found {total} total words")

    counts = character_counter(text)
    sorted_chars = sort_char_counts(counts)

    print("--------- Character Count -------")
    for item in sorted_chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")
    print("============= END ===============")

if __name__ == "__main__":  # language: python
    main()