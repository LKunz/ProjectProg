# This file contains functions that implements the RSA algortihm
# Inspiration: https://gist.github.com/JonCooperWorks/5314103

# Import packages
import random

# Function to compute the gcd (greatest common divisor)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Function that implements the Extended Euclidean algorithm
# (see : https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm)
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


# Function to compute multiplicative inverse
def multiplicative_inverse(e, phi):
    g, x, y = egcd(e, phi)
    if g != 1:
        raise Exception('Error: modular inverse does not exist')
    else:
        return x % phi

    
# Function to test if a number is prime
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    """ Generate private and public keys from p and q
        
    Parameters:
        p (int): 1st prime number
        q (int): 2nd prime number
        
    Algorithm:
        Compute n
        Compute e and d using previously defined functions
        
    Returns:
        public_key, private_key (tuple) : both keys
        
    Example:
        p = 17
        q = 19
        public_key, private_key = generate_keypair(p, q)
        print(public_key, private_key)
        >>> (209, 323) (113, 323)
        
    Remarks:
        The keys can change since e is genareted randomly
        
    """
    
    # Test if p and q are prime numbers
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both p and q must be prime')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    # Compute n
    n = p * q

    # Compute phi
    phi = (p-1) * (q-1)

    # Compute e using Euclid's Algorithm
    min_bound = max(p,q)
    e = random.randrange(min_bound, phi)
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(min_bound, phi)
        g = gcd(e, phi)
    
    # Compute d using Extended Euclid's Algorithm
    d = multiplicative_inverse(e, phi)
    
    # Return public and private keys
    # Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def make_blocks(text, n, size=3):
    """
    Make blocks from text 
    
    Parameters:
        text (str): text from which to make blocks
        n (int): n from RSA algortihm - we pass it as argument to avoid error
          in encoding blocks
        size (int): size of each block we want to create
        
    Algorithm:
        Use (shifted) ASCII to match all characters in 
          text to a number in [00,99]
        Divide number into blocks of length size
        
    Returns:
        Blocks version of text
        
    Example:
        message = "I love programming"
        blocks = make_blocks(message,'1000')
        print(blocks)
        >>> [410, 76, 798, 669, 8, 82, 797, 182, 657, 777, 737, 871]
    
    """
    
    # Define output
    blocks = ""
    
    # Check parameters (for encryption to work)
    if size <= 1:
        raise Exception('p and q are too small')
    elif size >= len(str(n)):
        raise Exception('p and q are too small')
    # Encode characters into blocks    
    else: 
        for i in text:
            tmp = str(ord(i) - 32) # To be in good range (<3 numbers)
            if (len(tmp) == 1): # Add zero at the start
                tmp = '0' + tmp
            blocks += tmp
        
        blocks = [int(blocks[i * (size):(i + 1) * (size)]) \
                  for i in range((len(blocks) + size - 1) // (size) )]
        
    return blocks
        

def make_text(blocks, size=3):
    """
    Recover text from block of defined size
    
    Parameters:
        blocks (list): list of integers to convert to text
        size (int): size of each block we want to convert
        
    Algorithm:
        Merge blocks
        Use (shifted) ASCII to match all resulting integers to characters
        
    Returns:
        text version of blocks
        
    Example:
        blocks = [410, 76, 798, 669, 8, 82, 797, 182, 657, 777, 737, 871]
        text = make_text(blocks, size=3)
        print(text)
        >>> I love programming
    
    Remarks:
        The size must be the same as in function make_blocks for the algorithm
          to work properly
    
    """
    
    # Define outputs
    text = ""
    text_tmp = ""
    
    # Conversion
    for i in range(len(blocks)):
        tmp = str(blocks[i])
        if i < (len(blocks)-1): # Avoid error at the end
            while (len(tmp) < size):
                tmp = '0' + tmp
        
        text_tmp += tmp
            
    text_tmp = [int(text_tmp[i * (2):(i + 1) * (2)]) for i in range((len(text_tmp) + 2 - 1) // (2) )]
    
    for i in text_tmp:
        text += chr(i+32) # Shifted match
    
    return text

# Same blocks and same key as before
blocks = [410, 76, 798, 669, 8, 82, 797, 182, 657, 777, 737, 871]
text = make_text(blocks, size=3)
print(text)


def EncryptRSA(plaintext, pub_key):
    """ Implement RSA encryption
        
    Parameters:
        plaintext (str): text to be encrypted
        pub_key (tuple): the public key (e, n)
        
    Algorithm:
        Implement RSA agorithm
        See: https://people.csail.mit.edu/rivest/Rsapaper.pdf for more info
        
    Returns:
        Encrypted version of plaintext (list of blocks)
        
    Example:
        public_key = (3379, 4267) # Created with generate_keypair(p, q)
        plain = "I love programming"
        cipher = EncryptRSA(plain, public_key)
        print(cipher)
        >>> [2881, 2501, 3552, 471, 1175, 3968, 2848, 2697,
             1025, 3309, 2987, 1611]
        
    Remarks:
        All characters are encrypted (including spaces, ponctuation, etc.)
        
    """
    
    # Get e and n from public key
    e, n = pub_key
    
    # Convert plaintext into blocks
    blocks = make_blocks(plaintext, n)
    
    # Convert blocks using formula (C = M^e mod n)
    cipher = [(block ** e) % n for block in blocks]
    
    # Return list of encrypted blocks
    return cipher


def DecryptRSA(cipher, priv_key):
    """ Implement RSA decryption
        
    Parameters:
        cipher (list): cipher to be decrypted
        priv_key (tuple): the private key (d, n)
        
    Algorithm:
        Implement RSA agorithm
        See: https://people.csail.mit.edu/rivest/Rsapaper.pdf for more info
        
    Returns:
        Decrypted version of chiphertext (str)
        
    Example:
        private_key = (3849, 4267) # Created with generate_keypair(p, q)
        cipher = [1855, 1181, 373, 2952, 4173, 2247, 168, 3303, 2182, 3320, 2306, 922, 1]
        plain = DecryptRSA(cipher, private_key)
        print(plain)
        >>> I love programming!
    
    """
    
    # Get d and n from private key
    d, n = priv_key
    
    # Apply formula (M = C^d mod n)
    plain_blocks = [(block ** d) % n \
                    for block in cipher]
    
    # Convert into text
    plaintext = make_text(plain_blocks)
                            
    # Return plaintext (string)
    return plaintext