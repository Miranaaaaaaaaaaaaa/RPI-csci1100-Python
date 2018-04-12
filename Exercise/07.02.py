def add_tuples(tuple1, tuple2, tuple3):
    first = tuple1[0] + tuple2[0] + tuple3[0]
    second = tuple1[1] + tuple2[1] + tuple3[1]
    return (first, second)

print(add_tuples( (1,4), (8,3), (14,0) ))
print(add_tuples( (3,2), (11,1), (-2,6) ))