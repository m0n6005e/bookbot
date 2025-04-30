from stats import num_words
from stats import num_characters
from stats import dictonary_sort
from stats import output_message
import sys

def main():
    #get book from somewhere and put it in book
    if len(sys.argv) > 1:
        book = sys.argv[1]          #"/home/m0n6005e/bookbot/books/frankenstein.txt"
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    book_text = get_book_text(book)
    word_count = num_words(book_text)  
    character_count = num_characters(book_text) 
    sorted_dictonary = dictonary_sort(character_count)
    output_message(word_count, sorted_dictonary, book)
   

def get_book_text(bookPath):
    with open(bookPath, "r", encoding="latin-1") as f:   
        return f.read()



main()
