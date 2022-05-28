# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

from re import L




filename = './newtextfile.txt'

def read_file_content(filename):
    # [assignment] Add your code here 
    var = open(filename, 'r')

    content = var.read()


    return content


print (read_file_content(filename))

def count_words():
    text = read_file_content("./story.txt")
    
    newvar = text.split()

    

    for i in newvar:
        
        as_count = i.count("as")
        would_count = i.count("would")


    print(text)
    # [assignment] Add your code here
    result = {'as': newvar.count("as"), "would":newvar.count("would")}

    return result

print(count_words())
