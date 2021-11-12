def encrypt(text, s):
    result = ""

    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result+=chr((ord(char) + s-65)%26+65)
        else:
            result+=chr((ord(char) + s-97)%26+97)
    return result
def decrypt(d, s1):
    res = ""

    for n in range(len(d)):
        char = d[n]
        if char.isupper():
            res+=chr((ord(char) + s1-65)%26+65)
        else:
            res+=chr((ord(char) + s1-97)%26+97)
    return res

text = input("Enter the Password :")
s = 4
print("_"*255)
print("_"*255)
print("Cipher   : " + encrypt(text, s))
print("_"*255)
d=encrypt(text , s)
s1 = -4
print("_"*255)
print("Decipher : " + decrypt(d, s1))
print("_"*255)