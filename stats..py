def get_num_words(book_text: str) -> int:
    word_count:int = 0
    """
    word_count : int
    This function takes a word count dictionary and returns the total number of words.
    
    :param word_count: Dictionary with words as keys and their counts as values
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
