# Week 2 Problem 5 - "Caesar Cipher"
# Link - https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/

# inputs:
# n = 11
# s = middle-Outz
# k = 2

def caesarCipher(s, k, n):
    useq = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    lseq = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        
    es = list(s)
    for i in range(n):
        if es[i] in lseq:
            si = lseq.index(es[i])  
            es[i] = lseq[(si+k)%26]
        
        elif es[i] in useq:
            si = useq.index(es[i])  
            es[i] = useq[(si+k)%26]
        
    es = "".join(es)
    return es

# output = "okffng-Qwvb"