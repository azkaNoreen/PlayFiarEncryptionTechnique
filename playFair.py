def checkIntegrity(text):
    
    #remove white spaces
    removedSpacesText=text.replace(" ","")
    
    #check to take only alphabtic data , no special symbol
    while not (removedSpacesText.isalpha()):
        removedSpacesText=input("Please Enter Only alphabets")

    #if plain text contain J convert it to I
    finalText=removedSpacesText.replace('j','i')   
    
    # convert to lowercase only
    lowerText=finalText.lower()
    return lowerText 
    
def checkUnique(string):
    n=len(string)
    chars=[False] * 123
    
    for i in range(n):
        if(chars[ord(string[i])]==True):
            return False
        chars[ord(string[i])]=True
    
    return True
    
def checkKeyIntegrity(key):
    checkedKey=checkIntegrity(key)   
    #Enter only unique character for the key
    while not checkUnique(checkedKey):
        checkedKey=input("Please Enter Unique alphabets for the key: ")
    return checkIntegrity(checkedKey) 
#add x if pair are becoming same
def Dummy(text):
    if len(text)%2==0:
        for i in range(0,len(text),2):
            if text[i]==text[i+1]:
                text=text[0:i+1]+"x"+text[i+1:]
                text=Dummy(text)
    else:
        for i in range(0,len(text)-1,2):
            if text[i]==text[i+1]:
                text=text[0:i+1]+"x"+text[i+1:]
                text=Dummy(text)

    return text
def DummyFillAndPairs(text):
    
    #if same character pair, add x with first value 
    text=Dummy(text)
    #check length after removing same pair ,add dummy if odd
    k=len(text)
    if not k%2==0:
        text=text+'z' 
    #Finally, do pairing now
    pairs = []
    pair = 0
    for i in range(2, len(text), 2):
        pairs.append(text[pair:i])
 
        pair = i
    pairs.append(text[pair:])
    return pairs
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

table=[[0 for x in range(5)] for y in range(5)]

def makeTable(key,alphabets):
    notKey=[]

    # find non key alphabets from alphabets 
    for alpha in alphabets:
        if alpha not in key:
            notKey.append(alpha)
    #fill table
    n=len(key)
    c=0
    notKeyCounter=0
    position=-1
    for i in range(5):
        for j in range(5):
            position=position+1
            if position<n:
                table[i][j]=key[c]
                c=c+1
            else:
                table[i][j]=notKey[notKeyCounter]
                notKeyCounter=notKeyCounter+1
    return table
def search(table,alpha):
    for i in range(5):
        for j in range(5):
            if table[i][j]==alpha:
                return i,j
def encrypt(etable,pairedText):
    cipher=""
    for pair in pairedText:
        firstAlphaPosi,firstAlphaPosj=search(etable,pair[0])
        secondAlphaPosi,secondAlphaPosj=search(etable,pair[1])
        #same row
        if firstAlphaPosi==secondAlphaPosi:
            cipher=cipher+(etable[firstAlphaPosi][(firstAlphaPosj+1)%5])
            cipher=cipher+(etable[firstAlphaPosi][(secondAlphaPosj+1)%5])
        elif firstAlphaPosj==secondAlphaPosj:
            cipher=cipher+(etable[(firstAlphaPosi+1)%5][firstAlphaPosj])
            cipher=cipher+(etable[(secondAlphaPosi+1)%5][firstAlphaPosj])
        else:
            cipher=cipher+(etable[firstAlphaPosi][secondAlphaPosj])
            cipher=cipher+(etable[secondAlphaPosi][firstAlphaPosj])
        
    return cipher
def dencrypt(etable,pairedText):
    plainText=""
    for pair in pairedText:
        firstAlphaPosi,firstAlphaPosj=search(etable,pair[0])
        secondAlphaPosi,secondAlphaPosj=search(etable,pair[1])
        #same row
        if firstAlphaPosi==secondAlphaPosi:
            plainText=plainText+(etable[firstAlphaPosi][(firstAlphaPosj-1)%5])
            plainText=plainText+(etable[firstAlphaPosi][(secondAlphaPosj-1)%5])
        elif firstAlphaPosj==secondAlphaPosj:
            plainText=plainText+(etable[(firstAlphaPosi-1)%5][firstAlphaPosj])
            plainText=plainText+(etable[(secondAlphaPosi-1)%5][firstAlphaPosj])
        else:
            plainText=plainText+(etable[firstAlphaPosi][secondAlphaPosj])
            plainText=plainText+(etable[secondAlphaPosi][firstAlphaPosj])
        
    return plainText
def takeAndValidateData(choice):
    Text = input(f"Enter Text to {choice}:")
    CText=DummyFillAndPairs(checkIntegrity(Text))
    Key = input("Enter Key:")
    CKey=checkKeyIntegrity(Key)
    etable=makeTable(CKey,alpha)
    
    return CText,CKey,etable
def Encryption(choice):
    PlainText,UKey,PlayFairTable=takeAndValidateData(choice)
    playfaircipher=encrypt(PlayFairTable,PlainText)
    return playfaircipher   
def Dencryption(choice):
    PlainText,UKey,PlayFairTable=takeAndValidateData(choice)
    playfaircipher=dencrypt(PlayFairTable,PlainText)
    return playfaircipher 
if __name__ == "__main__":

    print("Welcome to the Play Fair Encryption Technique ")
    print("Enter your choice,")
    print("1. Encryption")
    print("2. Decryption")

    while True:
        Choice= input()
        if Choice=="1":
            print("Encrypted text is: "+Encryption("Encrypt"))
            break
        elif Choice=="2":
            print("Decrypted text is: "+Dencryption("Decrypt"))
            break
        else:
            print("Please Enter Valid choice")
            continue
