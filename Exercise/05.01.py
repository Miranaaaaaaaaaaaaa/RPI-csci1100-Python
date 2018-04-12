def convert2fahren (c):
    fahren=c*1.8+32
    return fahren
c1=0
c2=32
c3=100
fahren1=convert2fahren(c1)
fahren2=convert2fahren(c2)
fahren3=convert2fahren(c3)
print(c1,"->",fahren1)
print(c2,"->",fahren2)
print(c3,"->",fahren3)