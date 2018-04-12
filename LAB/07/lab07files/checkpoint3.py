def parse_line(line):
    line = line.strip()
    if line.count('/')>=3:
        line1=line.rsplit('/',3)
        if line1[-1].isdigit() and line1[-2].isdigit() and line1[-3].isdigit():
            line2=int(line1[-3]),int(line1[-2]),int(line1[-1]),line1[0].rstrip()
            return line2
        else:
            return None

def get_line(fname,parno,lineno):
    li=[]
    pa=[]  
    fname=str(fname)+'.txt'
    file=open(fname,'r')
    for line in file:
        if line!='\n':
            li.append(line)
        else:
            pa.append(li) 
            li=[]
    while pa.count([])>0:
        pa.remove([])
    return pa[parno-1][lineno-1]

fname=int(input('Please enter the file number ==> '))
parno=int(input('Please enter the paragraph number ==> '))
lineno=int(input('Please enter the line number ==> '))

print(get_line(fname,parno,lineno))

c=open('program.py','w')
while True:  
    
    a=get_line(fname,parno,lineno)
    b=parse_line(a)
    fname=b[0]
    parno=b[1]
    lineno=b[2]
    if b[0]==0 and b[1]==0 and b[2]==0:
        break
    c.write(b[3])
    c.write('\n')
    
c.close()