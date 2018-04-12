def parse_line(line):
    if line.count('/')>=3:
        line1=line.rsplit('/',3)
        if line1[-1].isdigit() and line1[-2].isdigit() and line1[-3].isdigit():
            line2=int(line1[-3]),int(line1[-2]),int(line1[-1]),line1[0].rstrip()
            return line2
        else:
            return None

print(parse_line("    Here is some random text, like 5/4=3.    /12/3/4")) 
