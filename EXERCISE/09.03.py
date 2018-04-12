val=[]
end_found=False
c=0
i=0
while not end_found: 
        x=int(input('Enter a value (0 to end): '))
        print(x)
        if x==0:
                end_found=True
        else:
                val.append(x)
                a=max(val)
                b=min(val)                
                c+=val[i]
                avg=c/len(val)
                i+=1                

print('Min:',b)
print('Max:',a)
print('Avg: {0:.1f}'.format(avg))