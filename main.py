import sys


def get_book_text(path_to_book):
    with open(path_to_book) as f: # uses file path to open file (f)
        book_text = f.read() # reads f into a string sets variable to said string
    return book_text   # returns string


from stats import number_of_words
from stats import character_count
from stats import sorter
from stats import dict_lister



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {number_of_words(get_book_text(sys.argv[1]))} total words
--------- Character Count -------""")
    for i in range(0,len(dict_lister(character_count(get_book_text(sys.argv[1]))))):
        print(f"{dict_lister(character_count(get_book_text(sys.argv[1])))[i]["character"]}: {dict_lister(character_count(get_book_text(sys.argv[1])))[i]["count"]}")
    print("============= END ===============")


       
    return

main()