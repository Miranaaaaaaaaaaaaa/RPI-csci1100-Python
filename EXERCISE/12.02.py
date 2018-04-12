def first_day_greater(L1,L2):
    for a in range(min(len(L1),len(L2))):
        if L1[a]>L2[a]:
            return a
    return -1
       
L1 = [ 15.1, 17.3, 12.3, 16.4 ]
L2 = [ 15.0, 17.7, 12.5, 16.9 ]

if __name__ == "__main__":
    L1 = [ 15.1, 17.3, 12.3, 16.4 ]
    L2 = [ 15.0, 17.7, 12.5, 16.9 ]
    print("Test 1: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.6, 17.9, 18.2, 16.5, 12.7 ]
    print("Test 2: {}".format( first_day_greater(L1,L2) ))
    L2 = [ 15.9, 18.8, 11.4 ]
    print("Test 3: {}".format( first_day_greater(L1,L2) ))