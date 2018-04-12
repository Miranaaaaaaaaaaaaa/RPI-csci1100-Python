from PIL import Image
im1=Image.open('1.jpg')
im2=Image.open('2.jpg')
im3=Image.open('3.jpg')
im4=Image.open('4.jpg')
im5=Image.open('5.jpg')
im6=Image.open('6.jpg')

def resizep(im):
    a,b=im.size
    a=int((256/b)*a)
    return a
im1= im1.resize((resizep(im1),256))
im2= im2.resize((resizep(im2),256))
im3= im3.resize((resizep(im3),256))
im4= im4.resize((resizep(im4),256))
im5= im5.resize((resizep(im5),256))
im6= im6.resize((resizep(im6),256))
im= Image.new('RGB', (1000,360),'white')
z=31
im.paste(im1, (z, 20))
z+=1*(resizep(im1)+10)
im.paste(im2, (z, 100))
z+=1*(resizep(im2)+10)
im.paste(im3, (z, 20))
z+=1*(resizep(im3)+10)
im.paste(im4, (z, 100))
z+=1*(resizep(im4)+10)
im.paste(im5, (z, 20))
z+=1*(resizep(im5)+10)
im.paste(im6, (z, 100))
im.save('def.jpg')
im.show()