# This file contains functions that implements a monoalphabetic substitution cipher

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
        Encrypt plaintext using the key by replacing each letter by its randomly
          generated letter.
        
    Returns:
        Encrypted version of plaintext
        
    Example:
        text = "I love programming"
        key, ciphertext = SubstitutionEncrypt(text)
        print(key)
        >>> {'A': 'H', 'B': 'J', 'C': 'a', 'D': 'p', 'E': 'J', 'F': 'r', 
        'G': 'C', 'H': 'n', 'I': 's', 'J': 'O', 'K': 'k', 'L': 'U', 'M': 'c', 
        'N': 'h', 'O': 'P', 'P': 'y', 'Q': 'U', 'R': 'G', 'S': 'Q', 'T': 'D', 
        'U': 't', 'V': 'y', 'W': 'd', 'X': 'j', 'Y': 'L', 'Z': 'x', 'a': 'l', 
        'b': 'a', 'c': 'L', 'd': 'z', 'e': 'D', 'f': 'e', 'g': 'h', 'h': 's', 
        'i': 'C', 'j': 'F', 'k': 'B', 'l': 't', 'm': 'p', 'n': 'W', 'o': 'U', 
        'p': 'C', 'q': 'h', 'r': 'O', 's': 'b', 't': 'B', 'u': 'j', 'v': 'W', 
        'w': 'q', 'x': 'y', 'y': 'i', 'z': 'I'}
        print(ciphertext)
        >>> s tUWD COUhOlppCWh
    
    Remarks:
        Only letters (lower case and uppercase) are encrypted, not numbers 
          or special characters ('?' ' ' or '*' for example)
        The key is generated randomly. It thus changes everytime you run the
          code
        
    """
    
    # Enter characters included in algorithm
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    # Define output
    ciphertext = ""
    
    # Generate key randomly based on characters in letters
    numbers = [-1]
    if key == {}:
        for l in letters:
            tmp = -1
            while tmp in numbers: # Ensure not twice same output    
                tmp = random.randint(0,len(letters)-1) # Generate random number
            numbers.append(tmp)
            key[l] = letters[tmp] # Assign random letter
    
    # Encryption (only characters in letters)       
    for l in plaintext:
        if l in letters:
            ciphertext += key[l] 
        else:
            ciphertext += l
            
    return key, ciphertext

def SubstitutionDecrypt(ciphertext, key):
    """ Implement monoalphabetic Substitution decryption
        
    Parameters:
        ciphertext (str): text to be decrypted
        key (dic): the key used for encryption
        
    Algorithm:
        Use the key to convert ciphertext into plaintext by assigning each
          letter of the ciphertext to its counterparty in the key
        
    Returns:
        Decrypted version of ciphertext
        
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
    for l in ciphertext:
        if l in values: # If has been encrypted
            plaintext += decryption_key[l]
        else:
            plaintext += l # If has not been encrypted
    
    return plaintext