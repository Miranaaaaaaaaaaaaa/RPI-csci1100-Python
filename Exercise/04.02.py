r1 = 5
r2 = 32
import math
pi = math.pi
a1 = pi*r1**2
a2 = pi*math.pow(r2,2)
a3 = round(a2,2)
out_string = 'Area 1 = {0:.2f}'.format(a1)
print(out_string,"\n", "Area 2 = ",a3,sep="")


