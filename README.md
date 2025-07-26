# BookBot

BookBot is a Python text analysis tool that reads books and provides detailed statistics including word count and character frequency analysis. This is my first [Boot.dev](https://www.boot.dev) project!

## Features

- **Word Count Analysis**: Counts the total number of words in a text file
- **Character Frequency Analysis**: Analyzes the frequency of each alphabetic character
- **Formatted Output**: Displays results in a clean, organized format
- **Command Line Interface**: Easy-to-use CLI for analyzing any text file

## Project Structure

```
BookBot/
├── main.py              # Main application entry point
├── stats.py             # Text analysis functions
├── pyproject.toml       # Project configuration
├── README.md            # Project documentation
└── books/               # Sample books directory
    ├── frankenstein.txt
    ├── mobydick.txt
    └── prideandprejudice.txt
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/BDGeraghty/BookBot.git
cd BookBot
```

2. Ensure you have Python 3.6+ installed:
```bash
python3 --version
```

## Usage

Run BookBot from the command line by providing the path to a text file:

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

### Sample Output

```
Book Title: books/frankenstein.txt
77986 words found in the document
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 77986 total words
--------- Character Count -------
e: 46043
t: 30365
a: 26743
o: 25225
i: 24613
n: 24367
s: 21155
h: 19725
r: 18557
d: 16863
...
============= END ===============
```

## Functions

### `main.py`
- **`main()`**: Main function that orchestrates the text analysis process
- **`get_book_text(path)`**: Reads and returns the content of a text file

### `stats.py`
- **`get_num_words(text)`**: Counts the total number of words in the text
- **`get_chars_dict(text)`**: Creates a dictionary with character frequencies

## Requirements

- Python 3.6+
- No external dependencies required

## Sample Books

The project includes three classic literature texts for testing:
- **Frankenstein** by Mary Shelley
- **Moby Dick** by Herman Melville  
- **Pride and Prejudice** by Jane Austen

## Contributing

This is a learning project from Boot.dev. Feel free to fork and experiment!

## License

This project is open source and available under the [MIT License](LICENSE).

## About

Created as part of the Boot.dev Python course to learn:
- File I/O operations
- String manipulation
- Dictionary operations
- Command line argument parsing
- Code organization and modularity