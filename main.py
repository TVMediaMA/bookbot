from stats import word_count, char_count, print_report
import sys

def get_book_text(book):
    try:
        with open(book) as f:
            text = f.read()
            return text
    except FileNotFoundError:
        return None
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]  
    book = get_book_text(path)
    if not book:
        print("Error: Book not found.")
        sys.exit(1)
    num_words = word_count(book)
    charcs = char_count(book)
    report = print_report(charcs)
    print(f"""
        ============ BOOKBOT ============
        Analyzing book found at {path}...
        ----------- Word Count ----------
        Found {num_words} total words
        ----------- Character Count ------
        {report}
        ============= END ===============

        """)

main()