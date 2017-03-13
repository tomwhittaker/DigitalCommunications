def VigenereEncode(message,key):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = createFullKey(message,key)
    encoded=''
    for x in range(0,len(key)):
        pos=alphabet.index(key[x])
        newAlphabet=alphabet[pos:]+alphabet[:pos]
        pos=alphabet.index(message[x])
        encoded=encoded+newAlphabet[pos]
    return encoded


def createFullKey(message,key):
    messageL=len(message)
    keyL = len(key)
    div=messageL/keyL
    newKey=key*div
    spare=messageL%keyL
    add=key[:spare]
    newKey=newKey+add
    return newKey

def VigenereDecode(message,key):
    alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = createFullKey(message,key)
    encoded=''
    for x in range(0,len(key)):
        pos=alphabet.index(key[x])
        newAlphabet=alphabet[pos:]+alphabet[:pos]
        pos=newAlphabet.index(message[x])
        encoded=encoded+alphabet[pos]
    return encoded


encoded = VigenereDecode('ZZHQRPCOYRPGQOPZPBEHVXHAYWJO','YOHOHO')

if encoded == 'BLACKBEARDISSAILINGTOJAMAICA':
    print "works"
