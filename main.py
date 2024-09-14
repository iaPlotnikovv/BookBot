
def main() :    
    path = "./books/frankenstein.txt"
    text =print_the_text(path)
    print(text)
    

def print_the_text(path):
    with open(path) as f:       
        return f.read()
    

main()
