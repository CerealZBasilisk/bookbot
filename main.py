def read_book(book_path):
    file_contents = None
    with open(book_path) as f:
        file_contents = f.read()
    print(file_contents)


if __name__ == "__main__":
    read_book("books/frankenstein.txt")
