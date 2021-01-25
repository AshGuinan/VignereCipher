#Ais Guinan 2020
#Vignere Cipher Encoding and Decoding, Inspired by Crypto Classes 2021

#List accepted characters
dictionary = [c for c in (chr(i) for i in range(32,127))]
#grab how long this list is
dictionary_length = len(dictionary)

#the function itself - take in text, a key and a mode
def vign(txt='', key='', mode='d'):
    if not txt:
        #if no text is provided, prompt and end
        #TO DO: Loop until text or quit prompt provided?
        print ('Needs text.')
        return
    if not key:
        #if no key, prompt and end
        print ('Needs key.')
        return
    if mode not in ('d', 'e'):
        #Check if mode has been provided correctly
        print ('Type must be "d" or "e".')
        return
    if any(t not in dictionary for t in key):
        #dictionary contains only ascii characters, so we check key input is good.
        print ('Invalid characters in the key. You must only use ASCII symbols.')
        return

    results = ''
    key_length = len(key)

#We calculate the result cipher text here!

    for i, l in enumerate(txt):
        if l not in dictionary:
            results += l
        else:
            dictionary_index = dictionary.index(l)

            k = key[i % key_length]
            key_index = dictionary.index(k)
            if mode == 'd':
                key_index *= -1

            code = dictionary[(dictionary_index + key_index) % dictionary_length]

            results += code
#print out the results
    print (results)
    return results

#Grab inputs from the user
print('Hello!')
text = input("Enter your text: ")
key = input("Enter your key: ")
mode = input("Press D to Decrypt or E to Encrypt: ")
#Run the function!
vign(text, key, mode)