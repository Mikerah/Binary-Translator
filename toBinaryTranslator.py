# This program translated text to binary

translated_string = []

response = raw_input("Is the text in a file (Y/N)?")

if response.lower() == "y":
    filename = raw_input("What is the filename with the extension: ")
    input = open(filename, 'w')
    
    for i in filename:
        translated_string.append(format(ord(i), 'b'))
else:
    string_to_translate = raw_input("Enter a sentence: ")
    
    for i in string_to_translate:

        translated_string.append(format(ord(i),'b'))
 
print " ".join(translated_string) 
# print "The translated string is in a text file called toBinary."    
output = open('toBinary.txt', 'w')
output.write("".join(translated_string))
output.close()