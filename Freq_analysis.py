# This file contains a function that implements a basic frequency analysis
# Required: nltk.tokenize, matplotlib.pyplot

def Freq(text, target, hist=False):
    """ Implement frequency analysis of text
        
    Parameters:
        text (str): text to be analysed
        hist (bool): if True, plot histogram of frequencies
        target (str): the target on which to make the analysis. Should be
          either 'words' or 'characters'
        
    Algorithm:
        Tranform all letters to lowercases
        Compute frenquency of each characters or word  
        
    Return:
        freq (dic): dictionary of frequencies
        
    Examples:
        text = "Hello world! aaaa"
        Freq(text, hist=False)
        >>> {'a': 4, 'd': 1, 'e': 1, 'h': 1, 'l': 3, 'o': 2, 'r': 1, 'w': 1}
        
        text = "I love programming and data science! :)"
        print(Freq(text, 'words', hist=False))
        >>> {'i': 1, 'love': 1, 'programming': 1, 'and': 1, 'data': 1, 
            'science': 1}
    """
    
    # Make all letters lowercase
    text = text.lower()

    # Create list of tokens 
    if target not in ['words', 'characters']:
        raise Exception('Error: target')
    elif (target == 'words'):
       # Split into words
       from nltk.tokenize import word_tokenize
       tokens = word_tokenize(text)
       # Remove all tokens that are not alphabetic
       words = [word for word in tokens if word.isalpha()]
    else:
        # Define characters that we want the frequency of (can be changed)
        letters = "abcdefghijklmnopqrstuvwxyz"
        # Remove spaces and punctuation (all characters not in letters)
        for letter in text:
            if letter not in letters:
                text = text.replace(letter, "")
        # Sort text 
        words = "".join(sorted(text)) 
        
    # Create dictionary of letter/word frequencies
    freq = {}
    for item in words:
        if item in freq:
            freq[item] += 1 # Increment
        else:
            freq[item] = 1 # Initialization
    
    # Plot histogram     
    if hist == True:
        import matplotlib.pyplot as plt
        plt.bar(range(len(freq)), list(freq.values()), align="center")
        plt.xticks(range(len(freq)), list(freq.keys()))
        plt.xlabel("Character")
        plt.ylabel("Frequency")
        plt.show()
        plt.close()
    else:
        pass

    return freq