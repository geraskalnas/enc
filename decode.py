import base62 as b
diff=open("diff")
k=diff.read()
img=open(input("Image file:"), "rb")
imgEnc=b.decode(b.encodebytes(img.read()))
img.close()
f=open("eli", "wb")
f.write(b.decodebytes(b.encode(imgEnc-k)))
f.close()
