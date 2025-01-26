def main():
    path = "books/frankenstein.txt"
    text = texto(path)
    count = num_words(text)
    chars = num_character(text)
    char_list = dic_to_list(chars)
    char_list.sort(reverse = True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for item in char_list:
        print(f"The '{item['char']}' character was found '{item['num']}' times")
    
    
def texto(path):
    with open(path) as f:
        return f.read()

def num_words(text):
    words = text.split()
    return len(words)    
    
def num_character(text):
    char_times = {}
    lower_string = text.lower()
    for char in lower_string:
        if char in char_times:
            char_times[char] += 1
        else:
            char_times[char] = 1
    return char_times

def dic_to_list(char_times):
    char_list = []
    for char, count in char_times.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    return char_list

def sort_on(char_list):
    return char_list["num"]

main()
