string_to_translate = raw_input("Enter a sentence in binary: ")
string_to_translate_list = string_to_translate.split(" ")
string_to_translate_dec = []
translated_string = []

for i in string_to_translate_list:

    string_to_translate_dec.append(int(i, 2))
    
for i in string_to_translate_dec:

    translated_string.append(chr(i))
    
# print "".join(translated_string)

print "The translated string is in a text file called toText."    
output = open('toText.txt', 'w')
output.write("".join(translated_string))
output.close()