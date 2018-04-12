hd=input("Enter Dale's height: ")
print(hd)
hd=int(hd)
he=input("Enter Erin's height: ")
print(he)
he=int(he)
hs=input("Enter Sam's height: ")
print(hs)
hs=int(hs)

def read_height(hd,he,hs):
    if hd>he and hd>hs:
        if he>hs:
            return('Dale\nErin\nSam')
        elif he<hs:
            return('Dale\nSam\nErin')
    elif he>hd and he>hs:
        if hd>hs:
            return('Erin\nDale\nSam')
        elif hd<hs:
            return('Erin\nSam\nDale')
    elif hs>hd and hs>he:
        if hd>he:
            return('Sam\nDale\nErin')
        elif he>hd:
            return('Sam\nErin\nDale')

print(read_height(hd,he,hs))