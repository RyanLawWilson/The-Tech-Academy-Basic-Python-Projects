'''
For this drill, you will need to write a script that will
check a specific folder on the hard drive, verify whether
those files end with a “.txt” file extension and if they do,
print those qualifying file names and their corresponding
modified time-stamps to the console.


Your script will need to use Python 3 and the OS module. 

Your script will need to use the listdir() method from the
OS module to iterate through all files within a specific directory.

Your script will need to use the path.join() method from the
OS module to concatenate the file name to its file path, forming an absolute path.

Your script will need to use the getmtime() method from
the OS module to find the latest date that each text file
has been created or modified.

Your script will need to print each file ending with a “.txt”
file extension and its corresponding mtime to the console.
'''

import os
import time

# Displays all of the txt files in directory
def showDirectoryContents():
    # dircetory to be checked for txt files
    directory = "C:\\Users\\Ryan Wilson\\Documents\\TechAcademyRepos\\The Tech Academy Basic Python Projects\\Input-Output\\Drill1"

    print(directory)

    numOfTxtFiles = 0
    for i in os.listdir(directory):
        fileName = i.split('.')[0]
        fileType = i.split('.')[1]
        absolutePath = os.path.join(directory, i)
        
        # Only print if it's a text file
        if fileType == "txt":
            numOfTxtFiles += 1
            # os.path.getmtime() gets the seconds since January 1, 1970.
            epochTime = os.path.getmtime(absolutePath)
            # time.strftime() converts epoch time to readable time
            modifiedTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epochTime))
            with open(i, 'r') as f:
                data = f.read()
                print("\n===== {}\n=== mtime: {}s\n=== converted: {}\n{}\n".format(i, epochTime, modifiedTime, data))
                f.close()

    # Prints text based on number of txt files in the folder.            
    if (numOfTxtFiles > 0):
        print("Total number of .txt files: {}".format(numOfTxtFiles))
    else:
        print("There are no .txt files in this folder!")

if __name__ == "__main__":
    showDirectoryContents()




