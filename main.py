from stats import num_words

def main():
    book_text = get_book_text("/home/m0n6005e/bookbot/books/frankenstein.txt")
    num_words(book_text)

def get_book_text(bookPath):
    with open(bookPath) as f:        
        return f.read()



main()
