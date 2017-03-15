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

def repeatedSquare(number,power,mod):
    halfPower=power/2
    powers=[]
    powerOfTwo=[]
    posistionFinder=[]
    current=1
    value=number
    while current<power:
        value=value%mod
        powers.append(value)
        powerOfTwo.append(current)
        posistionFinder.append(current)
        current=current*2
        value=value*value%mod
        # print  ""+str(number)+"^"+str(current),"=",value,"mod",mod
    used=[]
    while len(powerOfTwo) !=0:
        num = powerOfTwo.pop()
        if power-num>=0:
            power=power-num
            used.append(num)
    answer=1
    for x in used:
        pos = posistionFinder.index(x)
        answer =answer*powers[pos]%mod
    return answer

def rsaEncrypt(publicKeyR,message):
    message = repeatedSquare(message, publicKeyR[1],publicKeyR[0])
    return message

def rsaDecrypt(privateKeyR,message):
    message = repeatedSquare(message,privateKeyR[1],privateKeyR[0])
    return message

#Q1
encoded = VigenereEncode('LETSSAILFORTHESPANISHMAIN','PIECESOFEIGHT')
#q2
decoded= VigenereDecode('ZVTVKGVBLNWYJVCLBOOHSSKFIGWYOEDNZ','GOLDCOINS')
#q3
encoded = VigenereDecode('IXYVAGYZLHMRCLAGUGXEQSMFXAZTHFCKNSGXINVHWDOOUPVUNYIZFMKYTOVKKEADYZPZGXWJFVSXGMXAZMHQTRPYGIXTESRVIGWWSLTHXIZIDPEVSSDRHIKKGDTYHWICSYTOIWPUBZNFVEZCHWWGHUAJBBXIJTGLRJHGLHXRNJANPNPZW\
ZYCIPHPYOANIPHOBKKRPYJHVTTEHROJYQCDTRDOWUKGCEEPLVNZSRCMTOUY\
LHWNHXGHNMWJEMHCIOHKNIHXSOTMDRSCBQYZYNU','KPKWETQKAODLZMERBOCAPNEERINWHQYBUOQUWTXMKIIBLNISOQAFRQHFHBE\
YXUPDMIMHEJNURXYQCXMULOVEKKXZZQWUUIBVSLMDJYQGBEVBIXDSJVXVPM\
YAAZROGEBGWIEVHLADXKRUIUYZDNCJTTKXDCHKNWGDNCKQGCBZVZNJPOFDY\
WWYRDMKFHKXFMFRGLMKHRWHFRJVNSGAQJHNCBYGSCEOPDVRRPPFWLOGUSRH\
ZRIIAKYGZBJVPPQLRMMFGFBXTSMBJFLBOAWBKCD')
answer = VigenereDecode('YAGNKAIHHXBZDQPTWHMSHWINSAZDWTJXNRTWAISMEPXCAKFGSPINWPZTEAK\
MFOLSKKRYGHYGCELHQHCOUFFMBDWGHVUGYEWHJYOUDTJJJKLHYLPENAOOUK\
HOXIFSDSUNACTFCPGKLTAINMULRBNXBUMTCMYPAXLQDLAJMFPSDKEKEOKNR\
RHQPXDKXMHEPWJBINLDIZTOYPQCIAMBXLIJZDKQRVOFTNRQNGIYOOBSXKZE\
BHCLYNUTALHFXZVNZNFJZGOSBKCPLEKFOKIEWYX',encoded)
# Q4i
repeatedSquare(17,54,139)
# q4ii
repeatedSquare(2345,65531,265189)
# q4iii
repeatedSquare(4733459,65537,75968647)
#q5i
# Cipher = Message^e mod n (in this case e=privateKey[1] and n=privateKey[0])
# q5ii
rsaEncrypt((76282747,65537),654733)
#q6i
# Message = Cipher^privateKey mod n.
print rsaDecrypt((9436709, 3497603),1684446.)
