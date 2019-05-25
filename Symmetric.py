# This file contains functions that implement a polyalphabetic substitution cipher

def SymmetricEncrypt(plaintext, key):
    """ Implement an example of Symmetric encryption
        Goal : avoid decryption using frequency analysis
        
    Parameters:
        plaintext (str): text to be encrypted
        key (str): the key used for encryption
        
    Algorithm:
        Convert plaintext and key to numbers (position in alphabet) 
          starting from 0 to 25
        Add letters in plaintext and letters in key (using blocks)
        Convert resulting code back to letters
        
    Return:
        Encrypted version of plaintext (upper cases) (str)
        
    Examples:
        text = "I love  programming"
        key = "code"
        SymmetricEncrypt(text, key)
        >>> K ZRZG DUSIFDQOWQK
        
        mes = "I love  programming"
        key = "b" 
        SymmetricEncrypt(mes, key) 
        >>> J MPWF  QSPHSBNNJOH
        # Here we get a simple Caesar cipher with only one letter as key
        
    Remarks:
        Only letters are encrypted. Special characters, punctuation and 
          numbers are not
        Special characters, punctuation and numbers are removed from key 
          for encrypting
        
    """
    
    # Define output
    ciphertext = ""
    
    # Define alphabet
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    
    # Make key uppercase
    key = key.upper()
    
    # Convert letters in plaintext to position number in upper or lower
    letters = []
    for letter in plaintext:
        if letter in upper:
            num = upper.find(letter) # Get position in alphabet
            letters.append(num)
        elif letter in lower:
            num = lower.find(letter)
            letters.append(num)
        else:
            letters.append(letter) # If not a letter
    
    # Convert letters in key to position number in upper
    keys = []
    for k in key:
        if k in upper:
            num = upper.find(k) # Get position in alphabet
            keys.append(num)
        else:
            pass # if not a letter
    
    # Strip letters from non letter characters
    numbers = []
    for letter in letters:
        if type(letter) == int:
            numbers.append(letter)
        else:
            pass
    
    # Apply agorithm
    res = []
    for i, l in enumerate(numbers):
            for j, k in enumerate(keys):
                mod = i % len(keys)
                if (mod == j):
                    tmp = (l + k) % len(upper)
                    res.append(tmp)
                else:
                    pass
                
    # Convert back to letters 
    j = 0
    for i in letters:
        if type(i) == int:
            letter = res[j]
            ciphertext += upper[letter]
            j += 1
        else:
            ciphertext += i

    
    return ciphertext


def SymmetricDecrypt(ciphertext, key):
    """ Decrypt cipher encrypted with SymmetricEncrypt
        
    Parameters:
        ciphertext (str): text to be decrypted
        key (str): the key used for encryption
        
    Algorithm:
        Convert ciphertext and key into numbers (position in alphabet) 
          starting from 0 to 25
        Substract back letters in ciphertext and letters in key (using blocks)
        Convert resulting code back into letters
        
    Return:
        Decrypted version of ciphertext (upper cases) (str)
        
    Examples:
        mes = "K ZRZG DUSIFDQOWQK"
        key = "CODE"
        SymmetricDecrypt(mes, key)
        >>> I LOVE PROGRAMMING
        
        cipher = "J MPWF  QSPHSBNNJOH"
        key = "b" 
        SymmetricDecrypt(cipher, key)
        >>> I LOVE  PROGRAMMING
        # Here we get a simple Caesar cipher with only one letter as key
        
    Remarks:
        Only letters are decrypted. Special characters, punctuation and numbers
          are not
        Special characters, punctuation and numbers are removed from key for
          encoding
        
    """
    
    # Define output
    plaintext = ""
    
    # Define alphabet
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    
    # Make key uppercase
    key = key.upper()
    
    # Convert letters in ciphertext to position number in upper or lower
    letters = []
    for letter in ciphertext:
        if letter in upper:
            num = upper.find(letter) # Get position in alphabet
            letters.append(num)
        elif letter in lower:
            num = lower.find(letter)
            letters.append(num)
        else:
            letters.append(letter) # If not a letter
    
    # Convert letters in key to position number in upper
    keys = []
    for k in key:
        if k in upper:
            tmp = upper.find(k) # Get position in alphabet
            keys.append(tmp)
        else:
            pass
    
    # Strip letters from non letter characters
    numbers = []
    for l in letters:
        if type(l) == int:
            numbers.append(l)
        else:
            pass
    
    # Apply agorithm
    res = []
    for i, l in enumerate(numbers):
            for j, k in enumerate(keys):
                mod = i % len(keys)
                if (mod == j):
                    tmp = (l - k) % len(upper)
                    res.append(tmp)
                else:
                    pass
                
    # Convert back to letters 
    j = 0
    for i in letters:
        if type(i) == int:
            tmp = res[j]
            plaintext += upper[tmp]
            j += 1
        else:
            plaintext += i

    
    return plaintext