import getpass


def string_to_hexa():
    s = raw_input("Please enter the string text: ")
    print s.encode("hex")


def hexa_to_string():
    s = raw_input("Please enter the hexa text: ")
    print s.decode("hex")


def Cipher():
    p = raw_input("Please enter the plain text: ")
    k = getpass.getpass('Please enter the key:')
    n = 2
    p_terms = [p[i:i + n] for i in range(0, len(p), n)]
    k_terms = [k[i:i + n] for i in range(0, len(k), n)]
    c_terms = []
    i = 0

    for p_hexa in p_terms:
        # Hay otra forma de hacer xor?
        c_bin = hex(int(p_hexa, 16) ^ int(k_terms[i], 16))[2:].zfill(2)
        c_terms.append(c_bin)
        i += 1
        if i == len(k_terms):
            i = 0
    print ('Ciphered Text : ' + '\n' + ''.join(c_terms))


def Decipher():
    c = raw_input("Please enter the ciphered text: ")
    k = getpass.getpass('Please enter the key:')
    n = 2
    c_terms = [c[i:i + n] for i in range(0, len(c), n)]
    k_terms = [k[i:i + n] for i in range(0, len(k), n)]
    p_terms = []
    i = 0
    for c_hexa in c_terms:
        # Hay otra forma de hacer xor?
        p_bin = hex(int(c_hexa, 16) ^ int(k_terms[i], 16))[2:].zfill(2)
        p_terms.append(p_bin)
        i += 1
        if i == len(k_terms):
            i = 0
    print ('Plain Text :' + '\n' + ''.join(p_terms))

while(True):
    print (
        "\n Posible Actions: \n " +
        "1. Cipher \n 2. Decipher \n 3. Exit \n " +
        "4. String to Hexa \n 5. Hexa to String")
    ans = raw_input("\n What would you like to do? ")
    if(ans == '1' or ans == 'cipher'):
        Cipher()
    elif(ans == '2' or ans == 'decipher'):
        Decipher()
    elif(ans == '3' or ans == 'exit'):
        break
    elif(ans == '4'):
        string_to_hexa()
    elif(ans == '5'):
        hexa_to_string()
    else:
        print("No valid choice!")
