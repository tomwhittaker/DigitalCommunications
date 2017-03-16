import math
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

def rsaSignature(privateKeyS,message):
    signature= repeatedSquare(message,privateKeyS[1],privateKeyS[0])
    return signature

def lookForPrimeFactor(number):
    x=2
    while x<math.sqrt(number):
        if number%x==0:
            return x
        x=x+1



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
#q6ii
rsaDecrypt((9436709, 3497603),1684446)
#q7i
# 'decrypt' message with own privateKey, encrypt both message and signature,send both
#q7ii
message=337722
signature=rsaDecrypt((9436709,3497603), message)
#q8i
# decrypt both message and signature, encrypt the signature with the senders public key
#q8ii
message = rsaDecrypt((9436709, 3497603),4647068)
signature = rsaDecrypt((9436709, 3497603),526345)
veri = rsaEncrypt((76282747,65537),signature)
#q8iii
#not valid
#q9
#Choose a random number < n and create message m =R^public key mod n send (M,R) and should work
(122269479,53407),58621765
# r=100
# m = repeatedSquare(r, 53407,122269479)
# pair = (m,r)
# print rsaEncrypt((122269479,53407), 100)
# print m
# #q10
# p=lookForPrimeFactor(76282747)
# q=76282747/p
# print p,q
# number=2
# while number !=0:
#     number*65537
for x in range(0,9):
    for y in range(0,9):
        for z in range(0,9):
            pin= str(x)+str(y)+str(z)
            pin=int(pin)
            encryptPin = rsaEncrypt((76282747,65537),pin)
            if str(encryptPin) in str(58621765):
                if len(str(pin))>=3:
                    print pin
