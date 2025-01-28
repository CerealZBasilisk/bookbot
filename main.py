from collections import Counter


def read_book(book_path):
    file_contents = None
    with open(book_path) as f:
        file_contents = f.read()
    # print(file_contents)
    return file_contents


def word_count(book):
    count = len(book.split())
    # print(count)
    return count

def character_counts(book):
    character_count = Counter(book.lower())
    return character_count

if __name__ == "__main__":

    book = read_book("books/frankenstein.txt")
    count = word_count(book)
    characters_counts = character_counts(book)
    print(characters_counts)
