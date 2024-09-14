
def main() :    
    path = "books/frankenstein.txt"
    text =print_the_text(path)
    words = word_counter(text)
    chars = character_counter(text)
    #print(text)
    report(path,words,chars)
   
    
def report(p,w,c):
    print(f"--- REPORT OF {p} ---\n {w} words found in this document\n")
    for key,value in c:
            print(f"The '{key}' character was found {value} times")
    print("--- END REPORT ---")


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
        elif char.isalpha()==True:
            counter[char]=1
    
        #sorting operation
    sorted_counter= sorted(counter.items(),reverse=True, key=lambda pair:pair[1] )

    return sorted_counter


main()
