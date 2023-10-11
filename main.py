def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    char_count = letter_count(text)
    print(f"--- Report of Frankenstein By Mary Shelley ---")
    print(f"There are {num_words} words in {book_path}")
    
    print("--- Alphabet Character Counts ---")
    sorted_char_count = sorted(char_count.items())
    for char, count in sorted_char_count:
        if char.isalpha():
            print(f"'{char}' is found {count} times")
    print("--- End of Report ---")
    
    
def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    letter_count = {}
    for char in text:
        low_char = char.lower()
        if low_char in letter_count:
            letter_count[low_char] += 1
        else: 
            letter_count[low_char] = 1
    return letter_count


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()