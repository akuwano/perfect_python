
s = 'あ'
b = s.encode('utf-8')
print(s)
print(b)


#b = b'あ'
s2 = b.decode('utf-8')
print(s2)

s3 = str(b)
print(s3)
