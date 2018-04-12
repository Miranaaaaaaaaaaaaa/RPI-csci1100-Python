word = input("Word => ")
print(word)
columns = int(input('#columns => '))
print(columns)
row = int(input('#rows => '))
print(row)

normal_line = "*** " * columns
line_b = "*** " * (columns//2) + "CS1 " + "*** " * (columns//2)
line_c1 = "*** " * (columns//2) + " ^  " + "*** " * (columns//2)
line_c2 = ((columns//2) - 1) * "*** " + " /  " + "*** " + " \\  " + ((columns//2) - 1) * "*** "
line_c3 = ((columns//2) - 1) * "*** " + " |  " + "*** " + " |  " + ((columns//2) - 1) * "*** "
line_cword = ((columns//2) - 1) * "*** " + " |  " + "CS1 " + " |  " + ((columns//2) - 1) * "*** "
line_c4 = ((columns//2) - 1) * "*** " + " \\  " + "*** " + " /  " + ((columns//2) - 1) * "*** "
line_c5 = "*** " * (columns//2) + " v  " + "*** " * (columns//2)

print('Your word is:',word)
print("")
print('(a)')
print((normal_line + "\n")*row)
print('(b)')
print((normal_line + "\n") * (row//2) + line_b + "\n" + (normal_line+"\n") * (row//2))
print("(c)")
print(line_c1 + "\n" + line_c2 + "\n" + (line_c3 + "\n") * ((row-5)//2) + line_cword + "\n" + (line_c3 + "\n") * ((row-5)//2) + line_c4 + "\n" + line_c5)