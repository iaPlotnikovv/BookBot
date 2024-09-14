
def main() :    
    path = "./books/frankenstein.txt"
    text =print_the_text(path)
    counted_words = word_counter(text)
    counted_char = character_counter(text)
   # print(text)
    print(f"in this text {counted_words} words!..\n..and i've counted every character for you! Why? Just for fun! U R WELCOME!!!\n{counted_char}")
    

def print_the_text(path):
    with open(path) as f:       
        return f.read()
    
def word_counter(text):
    text = text.split()
    return len(text)

def character_counter(text):
    counter = {}
    for char in text:
        char = char.lower()
        if char in counter:                
            counter[char]+=1
        else:
            counter[char]=1
    return counter


main()
