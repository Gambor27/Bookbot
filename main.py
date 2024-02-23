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
    sort_characters(character_count)
    return character_count

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
    count = count_words(book_text)
    character_list_sorted = character_count(book_text)
    num_lines = 0
    header = f'--Information about Frankenstein--\n{count} words in book\n\nCharacter Breakdown:'
    print(character_list_sorted)
    print(header)
    for char in character_list_sorted:
        if char == '\n':
            num_lines = character_list_sorted[char]
        count = character_list_sorted[char]
        print(f'The {char} character was found {count} times.')
    print(f'There are {num_lines} in the book total.')

        
main()