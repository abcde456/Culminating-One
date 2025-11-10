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
    print(fileText)

    with open("clean.txt", "w") as f:
        f.write(fileText)
    
    return fileText
