def num_words(book_text):
    words = book_text.split()
    return len(words) 
    

def num_characters(book_text):
    text = book_text.lower()
    letter_dict = {}
    for char in text:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1

    return letter_dict

def dictonary_sort(charactor_dictonary):
    char_count_list = []
    for key, value in charactor_dictonary.items():
        if key.isalpha():
            dict1 = {} 
            dict1["char"] = key
            dict1["num"] = value
            char_count_list.append(dict1)
    char_count_list.sort(reverse=True, key=sort_on)          
    return char_count_list

def output_message(word_count, sorted_list, book):
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {book}")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END =============")

def sort_on(charactor_dictonary):
    return charactor_dictonary["num"]

    
    