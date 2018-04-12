def find_min(l):
    c=[]
    for a in l:
        for b in a:
            c.append(b)
    return min(c)

if __name__ == "__main__":
    v = [ [ 11,12,3], [6, 8, 4], [ 17, 2, 18, 14] ]
    print("Min of list v: {}".format(find_min(v)) )
    u = [ [ 'car', 'tailor', 'ball' ], ['dress'], ['can', 'cheese', 'ring' ], [ 'rain', 'snow', 'sun' ] ]
    print("Min of list u: {}".format(find_min(u)) )