def linear_search( x, L ):
    count=0
    for value in L:
        if value == x:
            count+=1
    if count != 0:
        i1 = L.index(x)
        return i1
    elif count == 0:
        l=L.copy()
        l.append(x)
        l.sort()
        i2 = l.index(x)
        return i2

if __name__ == "__main__":
    #  Get the name of the file containing data
    fname = input('Enter the name of the data file => ')
    print(fname)

    #  Open and read the data values
    in_file = open(fname,'r')
    values = []
    for line in in_file:
        v = float(line)
        values.append(v)

    #  Search for each value requested by the user until -1 is entered
    x = 0
    while x != -1:
        x = float(input("Enter a value to search for ==> "))
        print(x)
        if x != -1:
            loc = linear_search(x, values )
            print(loc)