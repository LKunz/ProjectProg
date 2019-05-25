# This file contains functions that implements Caesar cipher algorithm

def CaesarEncrypt(plaintext, key):
    """ Implement Caesar cipher encryption
        
    Parameters:
        plaintext (str): text to be encrypted
        key (int): the key used for shifting
        
    Algorithm:
        Convert letters in plaintext to numbers (A → 0, B → 1, ..., Z → 25)
        Apply following formula: E(x) = (x + key) mod 26 (shifting)
        Convert back shifted numbers to letters (0 → A, 1 → B, ..., 25 → Z)
        
    Return:
        Encrypted version of plaintext (str)
        
    Example:
        mes = "I love programming"
        key = 1
        CaesarEncrypt(mes, key)
        >>> J mpwf qsphsbnnjoh
    
    Remarks:
        Only letters are encrypted, not numbers or special characters ('?' ' ' 
          or '*' for example)
        
    """
    
    # Define alphabet
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Define output
    code = ""
    
    # Encryption (letters only)
    for char in plaintext: 
        if char in lower: # If char is a letter
            num = lower.find(char) # Find position of letter in alphabet
            num += key # Shift 
            num = num % len(lower) # Resize into [0,25]
            shifted = lower[num] # Find post shift letter
            code += shifted # Add letter to result
        elif char in upper: # Same as above for uppercases
            num = upper.find(char)
            num += key
            num = num % len(upper)
            shifted = upper[num]
            code += shifted
        else:
            code += char # If not a letter: add char to result
   
    return code


def CaesarDecrypt(ciphertext, key):
    """ Decrypt ciphertext encrypted with Caesar cipher
    
    Parameters:
        ciphertext (str): encrypted text to be decrypted
        key (int): the key used for encryption
        
    Algorithm:
        Convert letters to numbers (A → 0, B → 1, ..., Z → 25)
        Apply following formula D(x) = (x - key) mod 26 (shifting back)
        Convert back shifted numbers to letters (0 → A, 1 → B, ..., 25 → Z)
        
    Return:
        Decrypted version of ciphertext (str)
        
    Example:
        mes = "J mpwf qsphsbnnjoh"
        key = 1
        CaesarDecrypt(mes, key)
        >>> I love programming
    
    Remarks:
        Only letters are decrypted, not numbers or special characters ('?' ' ' 
          or '*' for example)
        
    """
    
    # Define alphabet
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Define output
    code = ""
    
    # Decryption (letters only)
    for char in ciphertext: 
        if char in lower: # If char is a letter
            num = lower.find(char) # Find position of letter in alphabet
            num -= key # Shift back (only difference with CaesarEncrypt)
            num = num % len(lower) # Resize into [0,25]
            shifted = lower[num] # Find post shift letter
            code += shifted # Add letter to result
        elif char in upper:
            num = upper.find(char)
            num -= key
            num = num % len(upper)
            shifted = upper[num]
            code += shifted
        else:
            code += char # If not a letter: add char to result
   
    return code
