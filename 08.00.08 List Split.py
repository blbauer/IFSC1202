s = "a, b, c"
a = s.split(",")
for i in range(len(a)):
    a[i]=a[i].strip()
for i in range(len(a)):
	print (a[i])