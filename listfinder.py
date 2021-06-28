longword_list = ["migrate", "variable", "list", "file", "django", "python", "terminal", "exponential", "float", "dictionary"]

def longword(longword_list):
    lword = ""
    for x in range (len(longword_list)):
        if (len(longword_list[x]) > len(lword)):
            lword = longword_list[x]
    print("longest word is ", lword)

print(longword(longword_list))