# Cars list
scores = []
# open input file for reading
inputfilename = "Exam-Two-Scores.txt"
inputfile = open(inputfilename, 'r')  
# read the imput file
line = inputfile.readline()
# check for end of file
while line != '':
# split the line by commas
    scorevalues = line.split(",")
    scores.append(scorevalues)
    line = inputfile.readline()

for i in range(len(scores)):
    for j in range(1,len(scores[i])):
        scores[i][j] = int(scores[i][j])

for i in range(len(scores)):
    scores[i].append(0)
    for j in range(1,len(scores[i])-1):
        scores[i][5] = scores[i][5] + scores[i][j]

q1 = 0
q2 = 0
q3 = 0
q4 = 0
final = 0
for i in range(len(scores)):
    q1 = q1 + scores[i][1]
    q2 = q2 + scores[i][2]
    q3 = q3 + scores[i][3]
    q4 = q4 + scores[i][4]
    final = final + scores[i][5]
q1 = q1 / len(scores)
q2 = q2 / len(scores)
q3 = q3 / len(scores)
q4 = q4 / len(scores)
final = final / len(scores)

Team="Team"
print(f"{Team:10s}")
for i in range(len(scores)):
        print(f"{scores[i][0]:15s}{scores[i][1]:5d}{scores[i][2]:5d}{scores[i][3]:5d}{scores[i][4]:5d}{scores[i][5]:5d}")
print(" " * 15, f"{q1:4.1f} {q2:4.1f} {q3:4.1f} {q4:4.1f} {final:4.1f}")
