import string

def cleanTxt(fileName):
    translator = str.maketrans('', '', string.punctuation)

    fileText = ""

    try:
        with open(fileName) as f:
            fileText = f.read()
    except FileNotFoundError:
        return "ERROR: File not found"


    fileText = fileText.strip().replace(" ", "").translate(translator).upper()
    tempText = fileText

    x = 0
    fileText = ""
    for i in tempText:
        if(x > 4):
            x = 0
            fileText += " "
            fileText += i
        else:
            fileText += i
        x += 1
        print(x)

    print(fileText)

    with open("clean.txt", "w") as f:
        f.write(fileText)
    
    return fileText

cleanTxt("test.txt")