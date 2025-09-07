def get_book_text(filepath):  # language: python
    with open(filepath) as f:
        return f.read()

def word_counter(text):  # language: python
    return len(text.split())

def character_counter(text):  # language: python
    counts = {}
    for ch in text.lower():
        counts[ch] = counts.get(ch, 0) + 1
    return counts

def sort_on(item):  # language: python
    return item["num"]

def sort_char_counts(char_counts):  # language: python
    items = [{"char": ch, "num": n} for ch, n in char_counts.items()]
    items.sort(key=sort_on, reverse=True)
    return items