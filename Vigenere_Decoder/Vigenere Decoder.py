import math
from collections import Counter




cipherText = "F94720F94720DC5BD9F775FD74C14661D60FD7F731A968CB0262DD46D6F231B2668E4320DD4ACEF67DA874C74D6E8F46D6B972AF79DE566FC85DD9E979A42E8E7668CA0FDCFC67B86CC1526DCA41CCB97EBB20CD4A65CE5F98FD78BA69DA436C8F47D9EB75AA61DC4720C74ECBB977AF65CB4620C65B98FF63B26D8E5668CA0FDCFC62B467C0026CC642D1ED70A969C14C738F40DEB97CB863C6436EC64CD9F531BE6FC35275DB46D6FE31BC6ECA0262DD40CDFE79A920DA4A658F4CD7EA65FD6FC80268C648D0B976AF61CA4720CC5DC1E965B267DC4370C746DBB975B876C74165DC0FDCF666B320DA4D20D847DDEB74FD74C647798F4CD9F731BF658E5773CA4B98F07FFD73DB41688F4CD7F47CB872CD4B61C30FD9E961B169CD4374C640D6EA31BC738E5065C240CCFC31BE61DD4A20CB46CBE974B373CB50738F4ED6FD31BE6FC35275DB4ACAB965B872C34B6ECE43CBB731946E8E5675DD4194B962A863C60261DF5FD4F072BC74C74D6EDC0FDBEB74BC74CB02618F41DDFC75FD66C15020C14ACFB965A470CB5120C04998FA63A470DA4D67DD4EC8F178BE20DD5B73DB4AD5EA31AA68C741688F42D1F778B069D44720DB47DDB97FB863CB5173C65BC1B97EBB20DD4763DA5DDDB97AB8798E4669DC5BCAF073A874C74D6E8F4CD0F87FB365C25120CE41DCB962A870DE4E798F5BD0FC31B871DB4B76CE43DDF765FD6FC802618F58CAF065A965C00273C648D6F865A872CB0C20EE5B98ED79B820DD436DCA0FCCF07CB82C8E5668CA40CAFC65B463CF4E20CB4ACEFC7DB270C3476EDB5C98F07FFD69C0446FDD42D9ED78B26E8E5668CA40CAE031BC6ECA0263C042C8EC65B8728E5163C64AD6FA74FD73C64D778F5FCAF67CB473CB026FC90FC8EB7EAB69CA4B6EC80FC8EB7EAB61CC4E798F5CDDFA64AF658E4172D65FCCF662A473DA476DDC0398FA79BC6EC94B6EC80FCCF178AE20CF4C63C64AD6ED31BC72DA0269C15BD7B970FD73CD4B65C14CDDB71B8968CB0264CA59DDF57EAD6DCB4C748F40DEB972B26DDE5774CA5D98FA7EB374DC4D6CC34ADCB972B26DC3576EC64CD9ED78B26E8E4C65DB58D7EB7AAE20DE506FC246CBFC62FD65C8446FDD5BD4FC62AE20CF4C648F46D6FC69AD65C05169D94A98FA7EB374CF41748F4DDDED66B865C00270CA40C8F574FD6FDC0263C042C8EC65B872DD026FC10FD7E961B273C756658F5CD1FD74AE20C14420DB47DDB966B272C2462C8F5DDDE97DBC63C74C678F42D7EA65FD6DCF4B6C8F4ED6FD31B061C05B20CA57DBEC63AE69C14C738F58D1ED79FD74CB4E65CC40D5F464B369CD4374C640D6EA3FFD46C15020C24ED6E031BC70DE4E69CC4ECCF07EB3738E5668CA5CDDB972B26EDA4363DB5C98F464AE748E40658F42D9FD74FD73CB4175DD4A98F876BC69C051748F4DD7ED79FD65CF5465DC4BCAF661AD69C04520CE41DCB965B5658E4B6EC54ADBED78B26E8E4D668F46D4F574BA69DA4B6DCE5BDDB97CB873DD4367CA5C96B950A920DE5065DC4AD6ED3DFD68C15565D94ACAB531A968CB0273C043CDED78B26E8E4D668F5CDDFA64AF69DA5B20DF5DD7FB7DB86DDD026CCE48CBB966B86CC20262CA47D1F775FD6FDA4A65DD0FD9EB74BC738E4D668F4CD7F47CA86EC74161DB46D7F762FD74CB4168C140D4F676A42E8E616FC15BDDF461B272CF50798F4CCAE061A96FC95061DF47C1B978AE20DB4C61CD43DDB965B220C34765DB0FCCF174FD72CB5375C65DDDF474B374DD0E20C64198ED79BC748E4B74DC0FCDEA74FD77C1576CCB0FD1F461B273CB0273DA4CD0B962B876CB50658F46D6FA7EB376CB4C69CA41DBFC62FD6FC00274C74A98EA68AE74CB4F20DA5CDDEB62F120CF5120DB4098FC7DB46DC74C61DB4A98F470B3798E4D668F5BD0FC31BF65C04766C65BCBB97EBB20DA476CCA5FCAF672B873DD4B6EC801B2"
clen = len(cipherText)


#re add any leading 0's to ensure eveness (derived from ChatGPT)
if len(cipherText) % 2 != 0:
    cipherText = '0' + cipherText

cipher_bytes = bytes.fromhex(cipherText)


## English ascii-byte frequencies, derived from ChatGPT
english_freq = {
    # space and punctuation
    ord(' '): 0.182884, ord('.'): 0.0060, ord(','): 0.0060,
    ord('!'): 0.0020, ord('?'): 0.0020, ord('\''): 0.0025,
    ord('"'): 0.0025, ord(';'): 0.0010, ord(':'): 0.0010,
    ord('-'): 0.0010, ord('('): 0.0005, ord(')'): 0.0005,

    # lowercase letters (English frequencies)
    ord('a'): 0.065321, ord('b'): 0.012588, ord('c'): 0.022336,
    ord('d'): 0.032829, ord('e'): 0.102666, ord('f'): 0.019830,
    ord('g'): 0.016249, ord('h'): 0.049785, ord('i'): 0.056684,
    ord('j'): 0.000975, ord('k'): 0.005609, ord('l'): 0.033175,
    ord('m'): 0.020265, ord('n'): 0.057120, ord('o'): 0.061595,
    ord('p'): 0.015043, ord('q'): 0.000836, ord('r'): 0.049879,
    ord('s'): 0.053170, ord('t'): 0.075169, ord('u'): 0.022757,
    ord('v'): 0.007961, ord('w'): 0.017038, ord('x'): 0.001409,
    ord('y'): 0.014276, ord('z'): 0.000512,

    # uppercase letter (Infrequent to the point of irrelavancy)
    ord('A'): 0.065321, ord('B'): 0.012588, ord('C'): 0.022336,
    ord('D'): 0.032829, ord('E'): 0.102666, ord('F'): 0.019830,
    ord('G'): 0.016249, ord('H'): 0.049785, ord('I'): 0.056684,
    ord('J'): 0.000975, ord('K'): 0.005609, ord('L'): 0.033175,
    ord('M'): 0.020265, ord('N'): 0.057120, ord('O'): 0.061595,
    ord('P'): 0.015043, ord('Q'): 0.000836, ord('R'): 0.049879,
    ord('S'): 0.053170, ord('T'): 0.075169, ord('U'): 0.022757,
    ord('V'): 0.007961, ord('W'): 0.017038, ord('X'): 0.001409,
    ord('Y'): 0.014276, ord('Z'): 0.000512,
    
    ord('0'): 0.065, ord('1'): 0.110, ord('2'): 0.085,
    ord('3'): 0.075, ord('4'): 0.070, ord('5'): 0.065,
    ord('6'): 0.060, ord('7'): 0.058, ord('8'): 0.060,
    ord('9'): 0.052,
}
# set all other ascii values to 0
for b in range(32, 126):
    if b not in english_freq:
        english_freq[b] = 0.0001
        
        


def main():
    key_length = findKeyLength(cipher_bytes, clen)  #set key length 
    key = findKey(cipher_bytes, key_length)         #assign key 
    key_Bytes = bytes(key)                          #convert key to bytes to use in findplaintext
    ptext = findplaintext(cipher_bytes, key_Bytes)  #assign plaintext
    print(f"Key Length is {key_length}")           
    print(f"The key is  {key_Bytes.hex()}")         #convert key_bytes into hex form
    print("The plaintext is")                       
    print(ptext.decode(errors='ignore'))            #convert ptext into text form using decode
   


#caclulates the ICS value for a given length
def calcICS(length, Cbytes):
    icsarr = []
    for i in range(length):
        sI = Cbytes[i::length]    # divides the cypherbytes into different streams,
        slen = len(sI)            # which each byte being seperated by size length
        if slen <= 1:
            icsarr.append(0)  #if i is at length val, append 0 and go next
            continue 
        f = Counter(sI)     #calculates frequency of each ascii char
        
        topEq = sum( j * (j-1) for j in f.values() )    #calculate the numerator and
        botEq = slen * (slen - 1)                       # denomenator of ICS of length
        
        IcsI  = topEq/botEq         #calculate ISC for each I
        icsarr.append(IcsI)

    return sum(icsarr) / len(icsarr)    #return the average value




#returns the key length
def findKeyLength(Cbytes, clen):
    max_length = 30                 #set a max key length
    icVals = []                 # create a list to store ic values
    for k in range(1,max_length): 
        kVal = calcICS(k, Cbytes)   #call calcICS to obtain ICS values for each key length
        icVals.append((k, kVal))
        
    kMax = max(icVals, key=lambda x: x[1])  #find the max ic value for all key lengths,which becomes our key length
        
    return kMax[0]

#returns the given key in decimal bytes
def findKey(Cbytes, key_length):
    key = []
    
  
    
    
    for i in range(key_length):  #iterate through each byte of key
        keyByte = None
        currQP = -1
        
        s = Cbytes[i::key_length]
    
        for Byte in range(256):
            dec = bytes(c ^ Byte for c in s)        #shit currfent byte by all possible byte values
            
           ## printable = [p for p in dec if 32 <= p <= 126]
           ## if not printable:
           ##     continue
            
            printFreq = Counter(dec)                #counts frequencies of each shifted byte value

            numB = sum(printFreq.values())          #counts total number of values in printFreq (# of bytes in dec)
            
            q = [printFreq.get(i,0)/ numB for i in range(32,126)]   #calculate the frequency dist. of dec using printFreq
            p = [english_freq.get(i,0) for i in range(32,126)]      #calculate the frequency dist. of the english freq dictionary provided
            
            qp = sum(q[i] * p[i] for i in range(len(q)) )           #sum both frequency dist.

            if qp > currQP:                                         #if the new frequency sum is greater than its previous shift, replace it
                currQP = qp
                keyByte = Byte
            
        key.append(keyByte)                     #nested for loop exits with the key byte with the highest qp value, making it the key value for the current byte
    
    return key
    
        
#finds the plaintext in byte form
def findplaintext(Cbytes, k_bytes):
    klen = findKeyLength(Cbytes, clen)      #save the keylength
    mes = bytes([c ^ k_bytes[i % klen] for i, c in enumerate (cipher_bytes)])   #use the xor function to decrypt all bytes in cipher_bytes
    return mes  
    
    
if __name__ == '__main__':
    main()