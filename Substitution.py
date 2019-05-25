# This file contains functions that implement a monoalphabetic substitution cipher

import random

def SubstitutionEncrypt(plaintext, key={}):
    """ Implement monoalphabetic Substitution encryption
        
    Parameters:
        plaintext (str): text to be encrypted
        key (dic): the key used for encryption (can be passed as argument or
          generated automaticaly)
        
    Algorithm:
        If not specified, generate a key of the form {'A':'S', 'B':'f',
          ..., 'y':'J','z':'Q'} by randomly shuffeling and assigning 
          uppercase and lowercase letters to others
        Encrypt plaintext using the key by replacing each letter by its 
          randomly generated counterpart
        
    Return:
        key (dic)
        Encrypted version of plaintext (str)
        
    Example:
        text = "I love programming"
        key, ciphertext = SubstitutionEncrypt(text)
        print(key)
        print(ciphertext)
        >>> {'A': 'H', 'B': 'J', 'C': 'a', 'D': 'p', 'E': 'J', 'F': 'r', 
        'G': 'C', 'H': 'n', 'I': 's', 'J': 'O', 'K': 'k', 'L': 'U', 'M': 'c', 
        'N': 'h', 'O': 'P', 'P': 'y', 'Q': 'U', 'R': 'G', 'S': 'Q', 'T': 'D', 
        'U': 't', 'V': 'y', 'W': 'd', 'X': 'j', 'Y': 'L', 'Z': 'x', 'a': 'l', 
        'b': 'a', 'c': 'L', 'd': 'z', 'e': 'D', 'f': 'e', 'g': 'h', 'h': 's', 
        'i': 'C', 'j': 'F', 'k': 'B', 'l': 't', 'm': 'p', 'n': 'W', 'o': 'U', 
        'p': 'C', 'q': 'h', 'r': 'O', 's': 'b', 't': 'B', 'u': 'j', 'v': 'W', 
        'w': 'q', 'x': 'y', 'y': 'i', 'z': 'I'}
        s tUWD COUhOlppCWh
    
    Remarks:
        Only letters (lower case and uppercase) are encrypted, not numbers 
          or special characters ('?' ' ' or '*' for example)
        If not specified, the key is generated randomly. It thus changes everytime you run the
          code
        
    """
    
    # Enter characters included in algorithm (for generating key)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # Define output
    ciphertext = ""
    
    # Generate key randomly based on characters in letters
    numbers = [-1]
    if key == {}:
        for letter in letters:
            num = -1
            while num in numbers: # Ensure not twice same output    
                num = random.randint(0,len(letters)-1) # Generate random number
            numbers.append(num)
            key[letter] = letters[num] # Assign random letter
    
    # Get letters to be encrypted
    letter_keys = key.keys()
    
    # Encryption (only characters in keys)       
    for letter in plaintext:
        if letter in letter_keys:
            ciphertext += key[letter] 
        else:
            ciphertext += letter
            
    return key, ciphertext


def SubstitutionDecrypt(ciphertext, key):
    """ Implement monoalphabetic Substitution decryption
        
    Parameters:
        ciphertext (str): text to be decrypted
        key (dic): the key used for encryption
        
    Algorithm:
        Use the key to convert ciphertext into plaintext by assigning each
          letter of the ciphertext to its counterparty in the key
        
    Return:
        Decrypted version of ciphertext (str)
        
    Example:
        text = "s tUWD COUhOlppCWh"
        key = {'A': 'H', 'B': 'J', 'C': 'a', 'D': 'p', 'E': 'J', 'F': 'r', 
        'G': 'C', 'H': 'n', 'I': 's', 'J': 'O', 'K': 'k', 'L': 'U', 'M': 'c', 
        'N': 'h', 'O': 'P', 'P': 'y', 'Q': 'U', 'R': 'G', 'S': 'Q', 'T': 'D', 
        'U': 't', 'V': 'y', 'W': 'd', 'X': 'j', 'Y': 'L', 'Z': 'x', 'a': 'l', 
        'b': 'a', 'c': 'L', 'd': 'z', 'e': 'D', 'f': 'e', 'g': 'h', 'h': 's', 
        'i': 'C', 'j': 'F', 'k': 'B', 'l': 't', 'm': 'p', 'n': 'W', 'o': 'U', 
        'p': 'C', 'q': 'h', 'r': 'O', 's': 'b', 't': 'B', 'u': 'j', 'v': 'W', 
        'w': 'q', 'x': 'y', 'y': 'i', 'z': 'I'}
        plaintext = SubstitutionDecrypt(text)
        print(plaintext)
        >>> I love programming
    
    Remarks:
        Only letters (lower case and uppercase) are decrypted, not numbers 
          or special characters ('?' ' ' or '*' for example)
        
    """
    
    # Define output
    plaintext = ""
    
    # Get values of key
    values = key.values()
    
    # Inverse encryption key to get decryption key
    decryption_key = {v: k for k, v in key.items()}
    
    # Decryption 
    for letter in ciphertext:
        if letter in values: # If has been encrypted
            plaintext += decryption_key[letter]
        else:
            plaintext += letter # If has not been encrypted
    
    return plaintext
