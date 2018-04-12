from PIL import Image
def make_square(im):
    a,b = im.size
    a=int(a)
    b=int(b)
    if a>b:
        im=im.crop((0,0,b,b))
        return im
    elif b>a:
        im=im.crop((0,0,a,a))
        return im
    else:
        im=im.crop((0,0,a,b))
        return im