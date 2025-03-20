def number_of_words(book_text_counted):
    word_count = len(book_text_counted.split())  # pretty self-explanatory
    return word_count

def character_count(full_book):
    char_count = {}                       # empty dictionary set-up
    book = full_book.lower()              # puts whole book into lowercase
    for char in book:                     # for each character in the lowercase book
        if char not in char_count:        
            char_count[char] = 1          # create a key for the character and set its count to 1
        else:
            char_count[char] += 1         # if the key exists increase its count by 1
    return char_count                     # return the dictionary of character:count

def sorter(e):
    return e["count"]


def dict_lister(character_dict):
    dict_list = []                        # empty list of dictionaries
    for key in character_dict:
        if key.isalpha() == True:
            diction = {"character":key, "count":character_dict[key]}
            dict_list.append(diction)  #adds one dictionary per character to list
            dict_list.sort(key=sorter, reverse = True)#return list of dicts with 2 pairs each ex/ [{character:a, count:1}]
    return dict_list          


