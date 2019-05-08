import base62 as b
img=open(input("Images file: "), "rb")
imgEnc=b.decode(b.encodebytes(img.read()))
img.close()
f=open(input("Dangerous file: "), "rb")
fEnc=b.decode(b.encodebytes(f.read()))
f.close()
f.open("diff", "w")
f.write(imgEnc-fEnc)
