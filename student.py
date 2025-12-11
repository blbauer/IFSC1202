class Student:
    def __init__(self, firstname, lastname, tnumber, scores):
        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores

    def RunningAverage(self):
        valid_scores = [float(score) for score in self.Grades if score.strip()]
        if not valid_scores:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        # Treat missing scores as zero
        processed_scores = [float(score) if score.strip() else 0.0 for score in self.Grades]
        if not processed_scores:
            return 0.0
        return sum(processed_scores) / len(processed_scores)

    def LetterGrade(self):
        average = self.TotalAverage()
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"

def main():
    print(f"{'First Name':<12} {'Last Name':<12} {'ID Number':<12} {'Running Average':<12} {'Semester Average':<12} {'Letter Grade':<12}")
    print(f"{'-'*12:<12} {'-'*12:<12} {'-'*12:<12} {'-'*16:<12} {'-'*16:<12} {'-'*12:<12}")

    try:
        with open("10.Project Student Scores.txt", "r") as file:
            for line in file:
                parts = line.strip().split(',')
                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                scores = parts[3:]

                student = Student(firstname, lastname, tnumber, scores)

                running_avg = student.RunningAverage()
                total_avg = student.TotalAverage()
                letter_grade = student.LetterGrade()

                print(f"{student.FirstName:<12} {student.LastName:<12} {student.TNumber:<12} {running_avg:^16.2f} {total_avg:^16.2f} {letter_grade:^12}")
    except FileNotFoundError:
        print("Error: StudentScores.txt not found. Please create the file.")

if __name__ == "__main__":
    main()