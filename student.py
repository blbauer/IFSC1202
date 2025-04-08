a = []
inputfile = open("constitution.txt", "r")
line = inputfile.readline()
while line != "":
	line = line.strip()
	a.append(line)
	line = inputfile.readline()
prompt = input("Enter search term: ")
for k in range(0, len(a)):
	if a[k].find(prompt) != -1:
		for i in range(k, 0, -1):
			if a[i] == "":
				start = i
				break
		for i in range (k, len(a)):
			if a[i] == "":
				end = i
				break
		for m in range(start,end + 1):
			print(f'Line {m}: {a[m]}')
		k = end + 1
prompt = input("Enter search term: ")
for k in range(0, len(a)):
	if a[k].find(prompt) != -1:
		for i in range(k, 0, -1):
			if a[i] == "":
				start = i
				break
		for i in range (k, len(a)):
			if a[i] == "":
				end = i
				break
		for m in range(start,end + 1):
			print(f'Line {m}: {a[m]}')
		k = end + 1
inputfile.close()
		
