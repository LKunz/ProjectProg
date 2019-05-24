# This file contains functions that implements a polyalphabetic substitution cipher


def SymmetricEncrypt(plaintext, key):
    """ Implement an example of Symmetric encryption
        Goal : avoid decryption using frequency analysis
        
    Parameters:
        plaintext (str): text to be encrypted
        key (str): the key used for encryption
        
    Algorithm:
        Convert plaintext and key into numbers (position in alphabet) 
          starting from 0 to 25
        Add letters in plaintext and letters in key (using blocks)
        Convert resulting code back into letters
        
    Returns:
        Encrypted version of plaintext (upper cases)
        
    Examples:
        text = "I love  programming"
        key = "code"
        SymmetricEncrypt(text, key)
        >>> K ZRZG DUSIFDQOWQK
        
        mes = "I love  programming"
        key = "b" 
        SymmetricEncrypt(mes, key) 
        >>> J MPWF  QSPHSBNNJOH
        # Here we get a simple Caesar chiper with only one letter as key
        
    Remarks:
        Only letters are encrypted. Special characters, punctuation and numbers
          are not
        Special characters, punctuation and numbers are removed from key for
          encoding
        
    """
    
    # Define output
    ciphertext = ""
    
    # Define alphabet
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    
    # Make sequences uppercase
    #plaintext = plaintext.upper()
    key = key.upper()
    
    # Convert letters in plaintext into position number in upper or lower
    letters = []
    for letter in plaintext:
        if letter in upper:
            tmp = upper.find(letter) # Get position in alphabet
            letters.append(tmp)
        elif letter in lower:
            tmp = lower.find(letter)
            letters.append(tmp)
        else:
            letters.append(letter) # If not a letter
    
    # Convert letters in key into position number in upper
    keys = []
    for k in key:
        if k in upper:
            tmp = upper.find(k) # Get position in alphabet
            keys.append(tmp)
        else:
            pass # if not a letter
    
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
                    tmp = (l + k) % len(upper)
                    res.append(tmp)
                else:
                    pass
                
    # Convert back into letters 
    j = 0
    for i in letters:
        if type(i) == int:
            tmp = res[j]
            ciphertext += upper[tmp]
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
        
    Returns:
        Decrypted version of ciphertext (upper cases)
        
    Examples: (A REFAIRE)
        mes = "K ZRZG DUSIFDQOWQK"
        key = "CODE"
        SymmetricDecrypt(mes, key)
        >>> I LOVE PROGRAMMING
        
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
    
    # Make sequences uppercase
    #plaintext = plaintext.upper()
    key = key.upper()
    
    # Convert letters in ciphertext into position number in upper or lower
    letters = []
    for letter in ciphertext:
        if letter in upper:
            tmp = upper.find(letter) # Get position in alphabet
            letters.append(tmp)
        elif letter in lower:
            tmp = lower.find(letter)
            letters.append(tmp)
        else:
            letters.append(letter) # If not a letter
    
    # Convert letters in key into position number in upper
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
                
    # Convert back into letters 
    j = 0
    for i in letters:
        if type(i) == int:
            tmp = res[j]
            plaintext += upper[tmp]
            j += 1
        else:
            plaintext += i

    
    return plaintext