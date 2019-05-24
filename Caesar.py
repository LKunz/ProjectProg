# This file contains functions that implements Caesar cipher algorithm

def CaesarEncrypt(plaintext, key):
    """ Implement Caesar cipher encryption
        
    Parameters:
        plaintext (str): text to be encrypted
        key (int): the key used for shifting
        
    Algorithm:
        Convert letters in plaintext into numbers (A → 0, B → 1, ..., Z → 25)
        Apply following formula E(x) = (x + key) mod 26 (shifting)
        Convert back shifted numbers into new letters
        
    Returns:
        Encrypted version of plaintext
        
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
            tmp = lower.find(char) # Find position of letter in alphabet
            tmp += key # Shift 
            tmp = tmp % len(lower) # Resize into [0,25]
            tmp = lower[tmp] # Find post shift letter
            code += tmp # Add letter to result
        elif char in upper: # Same as above for uppercases
            tmp = upper.find(char)
            tmp += key
            tmp = tmp % len(upper)
            tmp = upper[tmp]
            code += tmp
        else:
            code += char # If not a letter: add char to result
   
    return code


def CaesarDecrypt(ciphertext, key):
    """ Decrypt ciphertext encrypted with Caesar cipher
    
    Parameters:
        ciphertext (str): encrypted text to be decrypted
        key (int): the key used for encoding using CaesarEncrypt()
        
    Algorithm:
        Convert letters into numbers (A → 0, B → 1, ..., Z → 25)
        Apply following formula D(x) = (x - key) mod 26 (shifting back)
        Convert back shifted numbers into letters
        
    Returns:
        Decrypted version of ciphertext
        
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
    
    code = ""
    
    # Decryption (letters only)
    for char in ciphertext: 
        if char in lower: # If char is a letter
            tmp = lower.find(char) # Find position of letter in alphabet
            tmp -= key # Shift back (only difference with CaesarEncrypt)
            tmp = tmp % len(lower) # Resize into [0,25]
            tmp = lower[tmp] # Find post shift letter
            code += tmp # Add letter to result
        elif char in upper:
            tmp = upper.find(char)
            tmp -= key
            tmp = tmp % len(upper)
            tmp = upper[tmp]
            code += tmp
        else:
            code += char # If not a letter: add char to result
   
    return code
