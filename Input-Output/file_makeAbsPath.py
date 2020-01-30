import os

fName = "Hello.txt"
# Need to use \\ to ignore escape character \
fPath = "C:\\Users\\Ryan Wilson\\Documents\\TechAcademyRepos\\The Tech Academy Basic Python Projects\\"

abPath = os.path.join(fPath, fName)
print(abPath)
