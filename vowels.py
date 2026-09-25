# Count Vowels and Consonants

# Description: Take a word or sentence as input, look at each character one by one, and count how many vowels (a, e, i, o, u) and consonants it contains.

# What it practices: You will use a loop to traverse the string and a multi-branch conditional (if-elif-else) to check if the character matches specific letters while ignoring spaces or punctuation.

vowel = []
consonant = []
special = []
sentence = input("Enter a Sentence")
sentence = sentence.lower()
for ch in sentence:
    
    if ch in ('a' ,'e' ,'i','o','u'):
        vowel.append(ch)
    elif not ch.isalpha():
        special.append(ch)
    else:
        consonant.append(ch)
        
print(len(vowel))
print(len(consonant))
