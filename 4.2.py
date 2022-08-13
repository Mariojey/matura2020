


file = open("pary.txt", "r")
fileW = open("wyniki4.txt", "a+" )
text_lines = file.read().splitlines()
file.close()

tab_word = ""

for i in text_lines:
    tab_word = i.split(" ")[1]
    #pobranie elementu io indexie 1
    l_string_char = "" #najdłuższy ciąg znaków
    c_string_char = "" #autalnie badany ciąg znaków
    for a in range(len(tab_word)):
        if len(c_string_char) == 0 or c_string_char[0] == tab_word[a]:
            c_string_char += tab_word[a]
        else:
            if len(c_string_char) > len(l_string_char):
                l_string_char = c_string_char
            c_string_char = ""
            c_string_char += tab_word[a]
    if len(c_string_char) > len(l_string_char):
        l_string_char = c_string_char
    if len(l_string_char) == 0:
        l_string_char = c_string_char
    #print(l_string_char + " " + str(len(l_string_char)))
    fileW.write(l_string_char + " " + str(len(l_string_char)) + '\n')