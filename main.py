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
    character_count = dict(Counter(book.lower()))
    char_count = {char:count for char, count in character_count.items() if char.isalpha()}
    return char_count

def generate_book_report(book_path):
    book = read_book(book_path)
    counts = word_count(book)
    chars_count = dict(character_counts(book))
    report = f"""
--- Begin report of {book_path} ---
{counts} words found in the document
    """
    #print(f" tpye got chars_count is: {type(chars_count)}")

    chars_count = sorted(chars_count.items(), key=lambda x: x[1], reverse=True)
    chars_count = {key: value for key,value in chars_count}
    for char,count in chars_count.items():
        char_info = f"\n'{char}' character was found {count} times"
        report += char_info
    report += "\n--- End report ---"

    return report



if __name__ == "__main__":

    book = read_book("books/frankenstein.txt")
    count = word_count(book)
    characters_counts = character_counts(book)
    # print(characters_counts)

    book_report = generate_book_report("books/frankenstein.txt")
    print(book_report)
