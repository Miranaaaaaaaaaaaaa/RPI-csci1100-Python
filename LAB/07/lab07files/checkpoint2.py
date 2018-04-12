
def get_line(fname,parno,lineno):
    li=[]
    pa=[]    
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
fname=str(fname)+'.txt'
parno=int(input('Please enter the paragraph number ==> '))
lineno=int(input('Please enter the line number ==> '))

print(get_line(fname,parno,lineno))

                