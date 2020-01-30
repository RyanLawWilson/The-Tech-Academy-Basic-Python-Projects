import os


def writeData():
    data = "Hello World"
    with open('test.txt', 'a') as f:
        f.write(data)
        f.close()


def openFile():
    # with is kinda like while
    with open('test.txt', 'r') as f:
        data = f.read()
        print(data)
        f.close()







if __name__ == "__main__":
    writeData()
    openFile()
