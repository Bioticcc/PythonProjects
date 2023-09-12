message = 'txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!'
key = 'friends'
def decryption(message, key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    letter_to_index = dict(zip(alpha, range(len(alpha))))
    index_to_letter = dict(zip(range(len(alpha)), alpha))
    #making the key the same length as the message - WORKS! X DOESNT WORK! ADD SPACES CORRECTLY >:(
    keyL = ''
    key_index = 0

    for char in message:
        if char.isalpha():
            keyL += key[key_index % len(key)]
            key_index = (key_index + 1) % len(key)
        else:
            keyL += ' '
        
     #turning each of the two inputs into their respective index forms - WORKS! 
    letter_to_index = dict(zip(alpha, range(len(alpha))))
    index_to_letter = dict(zip(range(len(alpha)), alpha))
    #the math :( - doesnt work???? X WORKS!
    decrypted = ''
    i = 0
    for char in message:
        if char.isalpha():
            number = ((letter_to_index[char]) + (letter_to_index[keyL[i]])) % len(alpha)
            decrypted += (index_to_letter[number])
            i += 1
        else:
            decrypted += char
            i += 1
    debug = print(keyL + '\n' + message + '\n' + str(letter_to_index))
    return decrypted
    
print(decryption(message, key))
