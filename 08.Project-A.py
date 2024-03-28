import requests
# Read the US Constitution from the Internet
response = requests.get('https://www.usconstitution.net/const.txt')
# Get the text string of the response
USConstString = response.text
# Split the string by newline character into a list
USConstList = USConstString.split("\n")
# Prompt for a search term
search = input("Enter search term: ")
while search !="":
#   initialize the line number of the beginning and ending sections
    begsection = 0
    endsection = 0
#   Loop thourgh the text
    for i in range(len(USConstList)):
#   Check to see if the search value exists in the line
        if USConstList[i].find(search) != -1:
#           Search value found - loop backwards from the current line until you have a blank line
            for j in range(i,0,-1):
                if USConstList[j] == "":
                    startsection = j
                    break
#           Loop forward from the current line until you have a blank line
            for j in range(i,len(USConstList)):
                if USConstList[j] == "":
                    endsection = j + 1
                    break
#           Print the line numbers and section that contains the search term   
            for j in range(startsection, endsection):
                print("Line {}: {}".format(j, USConstList[j]))
            print()
#           No need to print the section twice if the search term occurs twice
#           Reset the current line to the end of the section    
            i = endsection
#   Prompt for a new search term
    search = input("Enter search term: ")