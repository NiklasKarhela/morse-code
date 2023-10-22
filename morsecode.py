morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' ',}


def encrypt(msg):
    #first we will make a lsit of the message so we can opperate a letter at a time.
    msg = list(msg.upper())
    encrypted = []
    #Loop goes through all letters and adds the corresponding morse code to a list
    for letter in msg:
        encrypted.append(morse_code_dict[letter])
    
    #returns the message in morse code
    return " ".join(encrypted)

def decrypt(msg):
    #This snippet of code is here to store the position of the spaces in the message
    msg = list(msg)
    pos = 0
    msg_pos = []

    #this loop stores the position of spaces
    for idx, num in enumerate(msg):
        if num == " " and msg[idx-1] == " " and msg[idx+1] == " ":
            msg_pos.append(pos)
        elif num == " " and msg[idx-1] != " ":
            pos += 1

    #here we make the morse code suttabel for our for loop below
    msg = "".join(msg)
    msg = msg.split()
    decrypted = []

    #this loop adds all letters that correspond to the morse code to a list
    for morse in msg:
        for key in morse_code_dict:
            if morse_code_dict[key] == morse:
                decrypted.append(key)

    #this part adds the spaces to the text
    for index, number in enumerate(msg_pos):
        decrypted.insert((number+index), " ")

    return "".join(decrypted)


msg = input("What do you want to be converted to morse code? ")
msg_morse = encrypt(msg)
print("Your message in morse code: ", encrypt(msg))
print("Your message from the beginning: ", decrypt(msg_morse))
