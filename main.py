##  from stats import get_num_words
import sys

def get_num_words(book_text: str) -> int:
    """
    This function takes a book_text string and returns the total number of words.
    
    :param book_text: String containing the text of the book
    :return: Total number of words
    """
    word_count = int(len(book_text.split()))
    return word_count

def text_to_charcount(book_text: str) -> dict:
    """
    This function takes a book_text string and returns the total number of characters.
    
    :param book_text: String containing the text of the book
    :return: Total number of characters
    """
    char_count_dict = {}
    lower_text = book_text.lower()
    for char in lower_text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
            
    ## char_count = int(len(book_text))

    return char_count_dict

def get_book_text(book_name:str) -> str:
        
    with open(book_name, "r") as f:
        file_contents = f.read()
    return file_contents

def main():

    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    elif len(sys.argv) == 2:
        book_name = sys.argv[1]
        print(f"Book Title: {book_name}")
    
    ##book_namw = str(sys.argv[1]) 
    
    book_text = get_book_text(book_name)
    ##print(book_text)
    
    word_count = get_num_words(book_text)
    ## char_dict
    ##print(f"{word_count} words found in the document")
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_name}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    char_dict = text_to_charcount(book_text)
    ##print(char_dict)
    sorted_char_dict = sorted(char_dict.items(), key=lambda x: x[1], reverse=True)
    print("--------- Character Count -------")
    for char, count in sorted_char_dict:
        print(f"{char}: {count}")
    print("============= END ===============")
        
    

if __name__ == "__main__":
    main()
     