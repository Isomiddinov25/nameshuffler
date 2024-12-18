def capitalize_word(word):
    if len(word) == 0:
        return word  
    return word[0].upper() + word[1:]


print(capitalize_word("hello"))  
print(capitalize_word("Hello")) 
print(capitalize_word("a"))      