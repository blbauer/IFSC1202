# scores list
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
# append a line of scoresvalues to the scores list
    scores.append(scorevalues)
# read next line
    line = inputfile.readline()
inputfile.close
# convert the scores to integers
for i in range(len(scores)):
    for j in range(1,len(scores[i])):
        scores[i][j] = int(scores[i][j])
# add the final score column and sum the score in each quarter
for i in range(len(scores)):
    scores[i].append(0)
    for j in range(1,len(scores[i])-1):
        scores[i][5] = scores[i][5] + scores[i][j]
# initialize each quarter and final
q1 = 0
q2 = 0
q3 = 0
q4 = 0
final = 0
# sum each quarter and final
for i in range(len(scores)):
    q1 = q1 + scores[i][1]
    q2 = q2 + scores[i][2]
    q3 = q3 + scores[i][3]
    q4 = q4 + scores[i][4]
    final = final + scores[i][5]
# determine average of each score and final
q1 = q1 / len(scores)
q2 = q2 / len(scores)
q3 = q3 / len(scores)
q4 = q4 / len(scores)
final = final / len(scores)

Team="Team"
Q1 = "Q1"
Q2 = "Q2"
Q3 = "Q3"
Q4 = "Q4"
Final = "Final"
Average = "Average"
# print heading
print(f"{Team:10s}{Q1:>7s}{Q2:>7s}{Q3:>7s}{Q4:>7s}{Final:>7s}")
print("-" * 45)
# print each score
for i in range(len(scores)):
        print(f"{scores[i][0]:10s}{scores[i][1]:7d}{scores[i][2]:7d}{scores[i][3]:7d}{scores[i][4]:7d}{scores[i][5]:7d}")
# print average
print("-" * 45)
print(f"{Average:10s}{q1:7.1f}{q2:7.1f}{q3:7.1f}{q4:7.1f}{final:7.1f}")
