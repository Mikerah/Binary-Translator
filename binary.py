# Binary Translation module

def toBinFrStr(file):

    translated_string = []
    for i in file:
        translated_string.append(format(ord(i), 'b'))
        
    return " ".join(translated_string)
    
def toStrFrBin(file):

    translated_string = []
    file_to_trans_list = file.split(" ")
    file_to_trans_dec = []
    
    for i in file_to_trans_list:
        file_to_trans_dec.append(int(i,2))
        
    for j in file_to_trans_dec:
        translated_string.append(chr(j))
        
    return "".join(translated_string)
        
if __name__ == '__main__':

    string = raw_input("> ")
    response = raw_input("To binary or text (b/t): ")
    if response.lower() == 'b':
        output = toBinFrStr(string)
        print output
    else:
        output = toStrFrBin(string)
        print output