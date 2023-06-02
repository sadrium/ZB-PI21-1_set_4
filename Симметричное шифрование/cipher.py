def vernam(text, key):
    answer = ''
    p = 0
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

                      
KEY = 'cvwopslweinedvq9fnasdlkfn2'

plainText = input('Enter text to encrypt: ')

encodedText = vernam(plainText, KEY)
print('Encoded text:', encodedText)

decodedText = vernam(encodedText, KEY)
print('Decoded text:', decodedText)
