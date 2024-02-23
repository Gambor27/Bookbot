def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    make_report(file_contents)
    
    
def get_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    words = book_text.split()
    return len(words)

def character_count(book_text):
    character_count = {}
    book_lowercase = book_text.lower()
    for character in book_lowercase:
        if character in character_count:
            character_count[character] += 1
        else:
            character_count[character] = 1
    sorted_data = sort_characters(character_count)
    return sorted_data

def sort_key(dict):
    return dict["count"]

def sort_characters(dict):
    list_of_characters = []
    for character in dict:
        entry = {"char" : character, "count" : dict[character]}
        list_of_characters.append(entry)
    list_of_characters.sort(reverse=True, key=sort_key)
    return list_of_characters

def make_report(book_text):
    word_count = count_words(book_text)
    character_list_sorted = character_count(book_text)
    num_lines = 0
    header = f'--Information about Frankenstein--\n{word_count} words in book\n\nCharacter Breakdown:'
    footer = f'--End Of Report--'
    print(header)
    for character in character_list_sorted:
        char = character['char']
        char_count = character['count']
        if char == '\n':
            num_lines = character['count']
        elif char == " ":
            print(f'There are {char_count} spaces in the book.')
        else:
            print(f'The {char} character was found {char_count} times.')
    print(f'There are {num_lines} lines in the book total.')
    print(footer)
        
main()